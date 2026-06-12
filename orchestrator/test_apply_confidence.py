#!/usr/bin/env python3
"""Offline regression for _apply_confidence corroboration (LW-2). No API calls.
Run from orchestrator/.

Instantiates TribunalTransversal via __new__ (skips __init__ -> no anthropic client,
no config build) and injects a minimal config dict. Exercises the REAL _apply_confidence
method end-to-end (not a reimplementation)."""
import sys
from schema import UnifiedVerdictOutput, Finding
from tribunal_transversal import TribunalTransversal

MIN_OV = 4


def _tt(min_ov=MIN_OV):
    tt = TribunalTransversal.__new__(TribunalTransversal)
    tt.config = {"rag": {"corroboration_min_overlap": min_ov}}
    return tt


def _raw(agent, *findings):
    #--- findings: (severity, title, evidence) tuples
    return {"agent_id": agent,
            "findings": [{"severity": s, "title": t, "evidence": e}
                         for (s, t, e) in findings]}


def _uvo(verdict, **tiers):
    def mk(sev, items):
        return [Finding(severity=sev, title=t, description="", evidence=e, root_cause="")
                for (t, e) in items]
    return UnifiedVerdictOutput(
        session_id="TEST", domain="P03", subscenario="x", regime="standard",
        tribunal_mode="TEST", agents_consulted=0,
        fatal_findings=mk("FATAL", tiers.get("fatal", [])),
        serious_findings=mk("SERIOUS", tiers.get("serious", [])),
        moderate_findings=mk("MODERATE", tiers.get("moderate", [])),
        latent_findings=mk("LATENT", tiers.get("latent", [])),
        final_verdict=verdict, confidence="MODERATE", verdict_reasoning="test",
    )


FAILS = 0


def check(name, cond):
    global FAILS
    print(("PASS" if cond else "FAIL"), "-", name)
    if not cond:
        FAILS += 1


def main():
    tt = _tt()

    #--- C1: legacy exact-title still corroborates (strict superset, no regression).
    ao = [_raw("AF-01", ("SERIOUS", "Missing termination clause", "sec 7")),
          _raw("AF-02", ("SERIOUS", "Missing termination clause", "sec 7")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS",
             serious=[("Missing termination clause", "sec 7")])
    tt._apply_confidence(u, ao)
    check("C1 exact-title corroborates (1 confirmed)", len(u.multi_agent_confirmed) == 1)
    check("C1 driver corroborated -> HIGH", u.confidence == "HIGH")
    check("C1 verdict intact", u.final_verdict == "VIABLE WITH CRITICAL CORRECTIONS")

    #--- C2: divergent titles, SAME defect -> now corroborate (the LW-2 bug).
    ao = [_raw("AF-01", ("SERIOUS", "Missing termination clause",
                         "Section 7 has no termination terms")),
          _raw("AF-02", ("SERIOUS", "Termination clause absent",
                         "Section 7 lacks any termination provision")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS",
             serious=[("No termination defined", "Section 7 termination missing")])
    tt._apply_confidence(u, ao)
    check("C2 divergent titles corroborate (1 confirmed)", len(u.multi_agent_confirmed) == 1)
    check("C2 synth<->raw gap crossed -> HIGH", u.confidence == "HIGH")

    #--- C3: shared scaffolding, DIFFERENT defects -> must NOT corroborate (overlap<4).
    ao = [_raw("AF-01", ("SERIOUS", "Missing termination clause", "section 7")),
          _raw("AF-02", ("SERIOUS", "Missing liability clause", "section 12")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS",
             serious=[("Missing termination clause", "section 7")])
    tt._apply_confidence(u, ao)
    check("C3 scaffold does NOT corroborate (0 confirmed)", len(u.multi_agent_confirmed) == 0)
    check("C3 single uncorroborated driver -> LOW", u.confidence == "LOW")

    #--- C4: same text but different severity -> must NOT corroborate.
    ao = [_raw("AF-01", ("FATAL", "Broken invariant X", "alpha beta gamma delta epsilon")),
          _raw("AF-02", ("LATENT", "Broken invariant X", "alpha beta gamma delta epsilon")),
          _raw("AF-03")]
    u = _uvo("INVIABLE", fatal=[("Broken invariant X", "alpha beta gamma delta epsilon")])
    tt._apply_confidence(u, ao)
    check("C4 cross-severity does NOT corroborate", len(u.multi_agent_confirmed) == 0)
    check("C4 verdict INVIABLE intact", u.final_verdict == "INVIABLE")

    #--- C5: single agent -> LOW (n<2).
    ao = [_raw("AF-01", ("SERIOUS", "X", "y"))]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS", serious=[("X", "y")])
    tt._apply_confidence(u, ao)
    check("C5 n<2 -> LOW", u.confidence == "LOW")
    check("C5 agents_consulted=1", u.agents_consulted == 1)

    #--- C6: clean verdict (no findings), n>=3 -> HIGH.
    ao = [_raw("AF-01"), _raw("AF-02"), _raw("AF-03")]
    u = _uvo("SOLID UNDER PRESSURE")
    tt._apply_confidence(u, ao)
    check("C6 clean n>=3 -> HIGH", u.confidence == "HIGH")
    check("C6 no confirmations", len(u.multi_agent_confirmed) == 0)

    #--- C7: >=2 unresolved clashes -> LOW even with a corroborated driver.
    ao = [_raw("AF-01", ("SERIOUS", "Missing termination clause", "sec 7")),
          _raw("AF-02", ("SERIOUS", "Missing termination clause", "sec 7")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS",
             serious=[("Missing termination clause", "sec 7")])
    u.conflicts_detected = ["CLASH: a | PRECEDENCE: UNRESOLVED | REASON: b",
                            "CLASH: c | PRECEDENCE: UNRESOLVED | REASON: d"]
    tt._apply_confidence(u, ao)
    check("C7 >=2 unresolved -> LOW despite corroboration", u.confidence == "LOW")

    #--- C8: raw corroborate by exact title; synth title fully different, evidence bridges.
    ao = [_raw("AF-01", ("MODERATE", "Weak auth",
                         "login lacks rate limiting on endpoint /api/login")),
          _raw("AF-02", ("MODERATE", "Weak auth",
                         "login lacks rate limiting on endpoint /api/login")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH ADJUSTMENTS",
             moderate=[("Bruteforce exposure",
                        "rate limiting absent endpoint /api/login")])
    tt._apply_confidence(u, ao)
    check("C8 synth title differs, evidence bridges -> HIGH", u.confidence == "HIGH")

    #--- C9: multi-finding driver, none corroborated -> MODERATE (verdict-neutral).
    ao = [_raw("AF-01", ("SERIOUS", "A defect one", "aaa bbb ccc"),
                        ("SERIOUS", "B defect two", "ddd eee fff")),
          _raw("AF-02", ("SERIOUS", "Z unrelated", "ggg hhh iii")),
          _raw("AF-03")]
    u = _uvo("VIABLE WITH CRITICAL CORRECTIONS",
             serious=[("A defect one", "aaa bbb ccc"), ("B defect two", "ddd eee fff")])
    tt._apply_confidence(u, ao)
    check("C9 multi-finding none corroborated -> MODERATE", u.confidence == "MODERATE")

    print("=" * 48)
    print("RESULT: %d FAIL / checks complete" % FAILS)
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()