#!/usr/bin/env python3
"""
P2 -- archetype lenses: wire the lenses into the P1 confidence-gated escalation round.
All-or-nothing + newline-aware. Dry-run by default; --apply writes atomically.

Target: orchestrator/tribunal_transversal.py
Run from the repo ROOT (where this file is delivered):
    python apply_p2_lenses.py            # dry-run (verifies every anchor, writes nothing)
    python apply_p2_lenses.py --apply    # applies the 4 anchored edits atomically

Prereqs already on disk (written via mi-filesystem):
    orchestrator/archetype_lenses.py        (pure lens catalog + helpers)
    orchestrator/test_archetype_lenses.py   (offline regression, 10 checks)
"""
import sys

LF = chr(10)
CRLF = chr(13) + chr(10)
TARGET = "orchestrator/tribunal_transversal.py"

EDITS = [
    # 1) import the pure lens helpers (right after the schema import)
    (
'''from schema import RuntimeContext, AgentVerdictOutput, UnifiedVerdictOutput, Finding, compute_confidence, should_escalate
from prompt_engine import PromptEngine''',
'''from schema import RuntimeContext, AgentVerdictOutput, UnifiedVerdictOutput, Finding, compute_confidence, should_escalate
from archetype_lenses import select_lenses, build_lens_directive
from prompt_engine import PromptEngine'''
    ),
    # 2) escalation round -> lens-driven (one archetype lens per FOR-ESC-* agent)
    (
'''    def _run_escalation_round(self, document, ctx, unified, round_no, max_esc_agents):
        """Bounded extra forensic pass over the verdict-driving findings. Distinct agent ids
        (FOR-ESC-*) so cross-agent corroboration counts them as independent. Degrades
        gracefully (errors captured) so offline/no-API runs never crash."""
        n_esc = min(self.budget.remaining_agents(), max(0, int(max_esc_agents)))
        roles = (ctx.forense_agents or [])[:n_esc]
        if not roles:
            return []
        if unified.fatal_findings:
            driving = unified.fatal_findings
        elif unified.serious_findings:
            driving = unified.serious_findings
        elif unified.moderate_findings:
            driving = unified.moderate_findings
        else:
            driving = unified.latent_findings
        focus = " | ".join(getattr(f, "title", "") for f in driving[:5]) or "low-corroboration verdict"
        directive = ("ESCALATION ROUND %d: confidence is LOW. Independently re-examine the "
                     "verdict-driving findings and corroborate or refute them with evidence: %s"
                     % (round_no, focus))
        results = []
        with ThreadPoolExecutor(max_workers=max(1, len(roles))) as executor:
            futures = {}
            for i, role in enumerate(roles):
                agent_id = "FOR-ESC-%s" % str(i + 1).zfill(2)
                prompt = self.engine.build_forense_prompt(
                    agent_id, role, ctx, directive,
                    handoff_window=self.config.get("tribunal", {}).get("handoff_window", 8000)
                )
                futures[executor.submit(self._call_agent, agent_id, "FORENSE", role, prompt, document)] = (agent_id, role)
            for future in as_completed(futures):
                agent_id, role = futures[future]
                try:
                    result = future.result(timeout=120)
                    result["role"] = role
                    result["escalation"] = True
                    results.append(result)
                    self._log("%s (escalation) -- verdict: %s" % (agent_id, result.get("preliminary_verdict", "N/A")))
                except Exception as e:
                    self._log("%s (escalation) failed: %s" % (agent_id, e))
                    results.append({"agent_id": agent_id, "role": role,
                                    "agent_type": "FORENSE", "error": str(e), "escalation": True})
        return results''',
'''    def _run_escalation_round(self, document, ctx, unified, round_no, max_esc_agents):
        """Bounded extra forensic pass over the verdict-driving findings. Each FOR-ESC-*
        agent is driven by a distinct archetype lens (P2 -- abstract adversarial
        perspectives, never real persons). Distinct agent ids (FOR-ESC-*) so cross-agent
        corroboration counts them as independent. Degrades gracefully (errors captured,
        lens optional) so offline/no-API runs never crash."""
        n_esc = min(self.budget.remaining_agents(), max(0, int(max_esc_agents)))
        roles = (ctx.forense_agents or [])[:n_esc]
        if not roles:
            return []
        if unified.fatal_findings:
            driving = unified.fatal_findings
        elif unified.serious_findings:
            driving = unified.serious_findings
        elif unified.moderate_findings:
            driving = unified.moderate_findings
        else:
            driving = unified.latent_findings
        focus = " | ".join(getattr(f, "title", "") for f in driving[:5]) or "low-corroboration verdict"
        lenses = select_lenses(len(roles))  #--- P2: one archetype lens per escalation agent (deterministic)
        results = []
        with ThreadPoolExecutor(max_workers=max(1, len(roles))) as executor:
            futures = {}
            for i, role in enumerate(roles):
                agent_id = "FOR-ESC-%s" % str(i + 1).zfill(2)
                lens = lenses[i] if i < len(lenses) else None
                directive = build_lens_directive(lens, round_no, focus)
                prompt = self.engine.build_forense_prompt(
                    agent_id, role, ctx, directive,
                    handoff_window=self.config.get("tribunal", {}).get("handoff_window", 8000)
                )
                futures[executor.submit(self._call_agent, agent_id, "FORENSE", role, prompt, document)] = (agent_id, role, lens)
            for future in as_completed(futures):
                agent_id, role, lens = futures[future]
                lens_id = (lens or {}).get("id")
                try:
                    result = future.result(timeout=120)
                    result["role"] = role
                    result["escalation"] = True
                    result["lens"] = lens_id
                    results.append(result)
                    self._log("%s (escalation, lens=%s) -- verdict: %s" % (agent_id, lens_id, result.get("preliminary_verdict", "N/A")))
                except Exception as e:
                    self._log("%s (escalation, lens=%s) failed: %s" % (agent_id, lens_id, e))
                    results.append({"agent_id": agent_id, "role": role,
                                    "agent_type": "FORENSE", "error": str(e), "escalation": True, "lens": lens_id})
        return results'''
    ),
    # 3) escalation transparency dict -> record applied lenses
    (
'''        esc.update({"triggered": rounds > 0, "rounds": rounds,
                    "confidence_after": unified.confidence})
        self._transparency["escalation"] = esc''',
'''        esc.update({"triggered": rounds > 0, "rounds": rounds,
                    "confidence_after": unified.confidence,
                    "lenses": sorted({o.get("lens") for o in all_outputs
                                      if isinstance(o, dict) and o.get("escalation") and o.get("lens")})})
        self._transparency["escalation"] = esc'''
    ),
    # 4) transparency report escalation line -> show lenses applied
    (
'''  Escalation:  {'YES' if escalation.get('triggered') else 'NO'} | rounds: {escalation.get('rounds', 0)} | {escalation.get('confidence_before', 'N/A')} -> {escalation.get('confidence_after', 'N/A')}{(' | ' + str(escalation.get('reason'))) if escalation.get('reason') else ''}''',
'''  Escalation:  {'YES' if escalation.get('triggered') else 'NO'} | rounds: {escalation.get('rounds', 0)} | {escalation.get('confidence_before', 'N/A')} -> {escalation.get('confidence_after', 'N/A')}{(' | ' + str(escalation.get('reason'))) if escalation.get('reason') else ''}{(' | lenses: ' + ', '.join(escalation.get('lenses') or [])) if escalation.get('lenses') else ''}'''
    ),
]


def detect_nl(text):
    return CRLF if CRLF in text else LF


def main():
    apply = "--apply" in sys.argv
    try:
        with open(TARGET, "r", encoding="utf-8", newline="") as fh:
            raw = fh.read()
    except FileNotFoundError:
        print("ABORT: %s not found. Run from the repo ROOT." % TARGET)
        sys.exit(2)

    nl = detect_nl(raw)

    if "from archetype_lenses import" in raw:
        print("SKIP: already applied (archetype_lenses import present). No changes.")
        sys.exit(0)

    work = raw
    for idx, (old, new) in enumerate(EDITS, 1):
        old_nl = old.replace(LF, nl)
        new_nl = new.replace(LF, nl)
        count = work.count(old_nl)
        if count != 1:
            print("ABORT edit %d: anchor found %d times (expected exactly 1). No file written." % (idx, count))
            sys.exit(1)
        work = work.replace(old_nl, new_nl, 1)
        print("OK   edit %d: anchor matched (1x)." % idx)

    print("=" * 52)
    if apply:
        with open(TARGET, "w", encoding="utf-8", newline="") as fh:
            fh.write(work)
        print("APPLIED: %s updated (%d edits, newline=%r)." % (TARGET, len(EDITS), nl))
    else:
        print("DRY-RUN OK: %d/%d anchors matched. Re-run with --apply to write." % (len(EDITS), len(EDITS)))


if __name__ == "__main__":
    main()
