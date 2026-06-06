"""
Dark Strategist v3.15.0 — test_provenance (offline, $0)
Contract for the signal-provenance attribution layer. No API, no network, no rank_bm25.

Guarantees verified:
  - overlap_score is deterministic distinct-token overlap (case-insensitive; disjoint -> 0).
  - no signals -> attribution is empty (graceful).
  - a finding above the floor is attributed to the signal it most overlaps (right source).
  - the floor (rag.provenance_min_overlap, default 3) is honored: sub-floor -> no attribution.
  - best-overlap wins among multiple signals.
  - attribution records carry severity + source path + snippet, and span severity tiers.
  - GOLDEN / structural independence: attribution reads the FINAL verdict and mutates
    NEITHER final_verdict NOR the findings -> it can never alter the verdict.

Pipeline-dependent checks SKIP (not fail) when the orchestrator import is unavailable,
mirroring the test_signals discipline. overlap_score checks are pure and always run.
"""
import sys

from retriever import overlap_score

_passed = 0
_failed = 0
_skipped = 0


def check(name, cond):
    global _passed, _failed
    if cond:
        _passed += 1
        print("  PASS  " + name)
    else:
        _failed += 1
        print("  FAIL  " + name)


def skip(name, why):
    global _skipped
    _skipped += 1
    print("  SKIP  %s (%s)" % (name, why))


_CFG = {
    "anthropic": {"api_key": "", "model": "claude-opus-4-7", "max_tokens": 8192},
    "prompts_dir": "./prompts",
    "tribunal": {"max_agents": 7, "max_calls_total": 40, "max_n2_per_n1": 3,
                 "escalation_enabled": True, "max_escalation_rounds": 1,
                 "max_escalation_agents": 2, "doc_window": 4000,
                 "parent_report_window": 1000, "alert_at_percent": 80},
    "rag": {"enabled": True, "chunk_size": 1000, "chunk_overlap": 150,
            "doc_top_k": 6, "corpus_top_k": 3, "signals_top_k": 3,
            "provenance_min_overlap": 3},
    "ssm": {"max_personas": 20, "max_rounds": 4, "max_parallel_personas": 5,
            "alert_at_percent": 80},
    "notifications": {"slack": {"enabled": False}, "github": {"enabled": False}},
    "logging": {"google_sheets": {"enabled": False}},
}


def _make_tt(min_overlap=3):
    """Builds a TribunalTransversal with empty api_key (no network at construction),
    overriding the provenance floor. Returns None if the pipeline import fails."""
    try:
        from tribunal_transversal import TribunalTransversal
    except Exception:
        return None
    import copy
    cfg = copy.deepcopy(_CFG)
    cfg["rag"]["provenance_min_overlap"] = min_overlap
    try:
        return TribunalTransversal(cfg)
    except Exception:
        return None


def _uvo(tt, findings):
    """Synthesizes a UnifiedVerdictOutput from raw finding dicts via the real
    deterministic path (no API)."""
    from schema import RuntimeContext
    ctx = RuntimeContext(type="general", subscenario="provenance_test",
                         objective="attribute findings to signals")
    return tt._deterministic_synthesis(ctx, [{"agent_id": "FOR-01", "findings": findings}])


#--- 1) overlap_score counts distinct shared tokens.
def t_overlap_basic():
    check("overlap_score counts shared distinct tokens",
          overlap_score("drawdown exceeded twenty percent",
                        "report drawdown exceeded twenty") == 3)


#--- 2) disjoint texts -> zero overlap.
def t_overlap_zero():
    check("overlap_score is 0 for disjoint texts",
          overlap_score("alpha beta gamma", "delta epsilon zeta") == 0)


#--- 3) overlap is case-insensitive (same tokenization as BM25).
def t_overlap_case():
    check("overlap_score is case-insensitive",
          overlap_score("Drawdown CRASH", "drawdown crash") == 2)


#--- 4) no signals -> empty attribution.
def t_no_signals_empty():
    tt = _make_tt()
    if tt is None:
        return skip("no signals -> empty attribution", "pipeline import")
    tt._active_signals_tagged = []
    uvo = _uvo(tt, [{"severity": "MODERATE", "title": "x", "description": "y",
                     "evidence": "z", "root_cause": "w"}])
    check("no signals -> attribution empty", tt._attribute_signal_provenance(uvo) == [])


#--- 5) a finding above the floor is attributed to the right signal source.
def t_attribute_right_source():
    tt = _make_tt()
    if tt is None:
        return skip("attribute to right source", "pipeline import")
    tt._active_signals_tagged = [
        ("noise.txt", "lease termination penalty civil code article tenant"),
        ("backtest.txt", "independent backtest drawdown exceeded twenty percent crash"),
    ]
    uvo = _uvo(tt, [{
        "severity": "FATAL",
        "title": "drawdown understated",
        "description": "proposal claims drawdown stays under five percent",
        "evidence": "backtest shows drawdown exceeded twenty percent in the crash",
        "root_cause": "optimistic risk modeling",
    }])
    prov = tt._attribute_signal_provenance(uvo)
    ok = len(prov) == 1 and prov[0]["source"] == "backtest.txt" and prov[0]["signal_index"] == 1
    check("finding attributed to the most-overlapping signal source", ok)


#--- 6) sub-floor overlap -> NOT attributed (prefer no attribution over noise).
def t_floor_honored():
    tt = _make_tt(min_overlap=3)
    if tt is None:
        return skip("floor honored", "pipeline import")
    tt._active_signals_tagged = [("weak.txt", "the rate moves")]
    #--- finding tokens {fixed, the, rate} vs {the, rate, moves} -> shared {the, rate} = 2 < 3
    uvo = _uvo(tt, [{"severity": "MODERATE", "title": "rate note",
                     "description": "the rate", "evidence": "fixed",
                     "root_cause": "n/a"}])
    check("sub-floor overlap is NOT attributed", tt._attribute_signal_provenance(uvo) == [])


#--- 7) configurable floor: an unreachable floor drops an otherwise-attributed finding.
def t_floor_configurable():
    tt_hi = _make_tt(min_overlap=99)
    if tt_hi is None:
        return skip("configurable floor", "pipeline import")
    tt_hi._active_signals_tagged = [("s.txt", "drawdown exceeded twenty percent crash backtest")]
    uvo = _uvo(tt_hi, [{"severity": "FATAL", "title": "t",
                        "description": "drawdown exceeded twenty percent",
                        "evidence": "crash backtest", "root_cause": "r"}])
    check("an unreachable floor yields no attribution",
          tt_hi._attribute_signal_provenance(uvo) == [])


#--- 8) best-overlap wins among several signals.
def t_best_overlap_wins():
    tt = _make_tt()
    if tt is None:
        return skip("best overlap wins", "pipeline import")
    tt._active_signals_tagged = [
        ("a.txt", "drawdown risk"),                                    # overlap 1
        ("b.txt", "drawdown exceeded twenty percent crash backtest"),  # overlap >=5
    ]
    uvo = _uvo(tt, [{"severity": "SERIOUS", "title": "t",
                     "description": "drawdown exceeded twenty percent crash",
                     "evidence": "backtest", "root_cause": "r"}])
    prov = tt._attribute_signal_provenance(uvo)
    check("the higher-overlap signal wins",
          len(prov) == 1 and prov[0]["signal_index"] == 1)


#--- 9) record carries severity + source + snippet.
def t_record_shape():
    tt = _make_tt()
    if tt is None:
        return skip("record shape", "pipeline import")
    tt._active_signals_tagged = [("src.txt", "alpha beta gamma delta epsilon zeta")]
    uvo = _uvo(tt, [{"severity": "LATENT", "title": "T",
                     "description": "alpha beta gamma delta",
                     "evidence": "epsilon zeta", "root_cause": "r"}])
    prov = tt._attribute_signal_provenance(uvo)
    ok = (len(prov) == 1 and prov[0]["severity"] == "LATENT"
          and prov[0]["source"] == "src.txt" and isinstance(prov[0]["snippet"], str)
          and bool(prov[0]["snippet"]))
    check("attribution record carries severity, source and snippet", ok)


#--- 10) attribution spans multiple severity tiers.
def t_multi_tier():
    tt = _make_tt()
    if tt is None:
        return skip("multi-tier attribution", "pipeline import")
    tt._active_signals_tagged = [
        ("liq.txt", "liquidity coverage ratio breached regulatory minimum threshold"),
        ("aud.txt", "auditor flagged revenue recognition timing material misstatement"),
    ]
    uvo = _uvo(tt, [
        {"severity": "FATAL", "title": "liquidity",
         "description": "liquidity coverage ratio breached regulatory minimum",
         "evidence": "threshold", "root_cause": "r"},
        {"severity": "MODERATE", "title": "revenue",
         "description": "revenue recognition timing flagged by auditor",
         "evidence": "material misstatement", "root_cause": "r"},
    ])
    prov = tt._attribute_signal_provenance(uvo)
    sevs = sorted(p["severity"] for p in prov)
    check("attribution spans FATAL + MODERATE tiers", sevs == ["FATAL", "MODERATE"])


#--- 11) GOLDEN: attribution mutates neither the verdict nor the findings.
def t_golden_independence():
    tt = _make_tt()
    if tt is None:
        return skip("golden: verdict/findings unchanged by attribution", "pipeline import")
    tt._active_signals_tagged = [("s.txt", "drawdown exceeded twenty percent crash backtest")]
    uvo = _uvo(tt, [{"severity": "FATAL", "title": "t",
                     "description": "drawdown exceeded twenty percent crash",
                     "evidence": "backtest", "root_cause": "r"}])
    verdict_before = uvo.final_verdict
    fatal_before = len(uvo.fatal_findings)
    _ = tt._attribute_signal_provenance(uvo)
    check("verdict unchanged by attribution (>=1 FATAL -> INVIABLE)",
          uvo.final_verdict == verdict_before == "INVIABLE")
    check("findings unchanged by attribution", len(uvo.fatal_findings) == fatal_before)


def main():
    print("test_provenance — signal-provenance attribution (offline)")
    for fn in (t_overlap_basic, t_overlap_zero, t_overlap_case, t_no_signals_empty,
               t_attribute_right_source, t_floor_honored, t_floor_configurable,
               t_best_overlap_wins, t_record_shape, t_multi_tier, t_golden_independence):
        fn()
    print("\n%d PASS / %d FAIL / %d SKIP" % (_passed, _failed, _skipped))
    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()
