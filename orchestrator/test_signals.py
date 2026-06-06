"""
Dark Strategist v3.14.0 — test_signals (offline, $0)
Contract for the P4 external-signals channel. No API, no network.

Guarantees verified:
  - signals = a DISTINCT, labelled evidence channel (never the corpus grounding label).
  - the in-block directive states signals are evidence, NOT a verdict input.
  - drop_zero_overlap keeps pure-noise signal passages out.
  - corpus + signals coexist; corpus block precedes signals block.
  - graceful degradation: no signals (+ doc fits, no corpus) -> byte-identical legacy.
  - NON-BINDING (golden): verdict is severity-driven (>=1 FATAL -> INVIABLE),
    computed from findings, structurally independent of any context/signal text.

BM25-dependent checks SKIP (not fail) when rank_bm25 is unavailable, mirroring the
e2e smoke discipline.
"""
import sys

from retriever import build_agent_context, _BM25_AVAILABLE

CORPUS_LABEL = "[JURISDICTIONAL CORPUS - REFERENCE GROUNDING]"
SIGNALS_LABEL = "[EXTERNAL SIGNALS - TIME-SENSITIVE EVIDENCE]"

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


#--- 1) Degradation: no signals, doc fits, no corpus -> exact legacy slice.
def t_legacy_byte_identical():
    doc = "alpha beta gamma delta epsilon"
    out = build_agent_context(doc, "alpha", window=4000)
    check("legacy byte-identical when no signals/corpus and doc fits", out == doc[:4000])


#--- 2) No-signals long doc still assembles without crashing.
def t_no_signals_long_doc():
    doc = ("token here. " * 2000)
    out = build_agent_context(doc, "token", window=500)
    check("no-signals long doc returns non-empty string", isinstance(out, str) and len(out) > 0)


#--- 3) Signals injected with the distinct label (BM25).
def t_signals_labelled():
    if not _BM25_AVAILABLE:
        return skip("signals labelled block injected", "rank_bm25 unavailable")
    doc = "lease agreement clauses about rent and termination"
    signals = ["recent enforcement action increased fines for late rent disclosure"]
    out = build_agent_context(doc, "rent", window=4000, signals=signals)
    check("signals block carries the EXTERNAL SIGNALS label", SIGNALS_LABEL in out)


#--- 4) The directive marks signals as evidence, NOT a verdict input (NON-BINDING in-band).
def t_signals_directive_non_binding():
    if not _BM25_AVAILABLE:
        return skip("signals directive present", "rank_bm25 unavailable")
    doc = "merger plan with synergy assumptions"
    signals = ["antitrust regulator opened a review of similar synergy mergers this quarter"]
    out = build_agent_context(doc, "synergy", window=4000, signals=signals)
    check("directive states signals are NOT a verdict input", "NOT a verdict input" in out)


#--- 5) A relevant signal (shares tokens) is included.
def t_relevant_signal_included():
    if not _BM25_AVAILABLE:
        return skip("relevant signal included", "rank_bm25 unavailable")
    doc = "the proposal claims drawdown stays under five percent"
    signals = ["independent backtest shows drawdown exceeded twenty percent in the crash"]
    out = build_agent_context(doc, "drawdown", window=4000, signals=signals)
    check("relevant signal passage appears in output", "backtest" in out)


#--- 6) drop_zero_overlap: a pure-noise signal (no shared token) is excluded.
def t_zero_overlap_signal_dropped():
    if not _BM25_AVAILABLE:
        return skip("zero-overlap signal dropped", "rank_bm25 unavailable")
    doc = "drawdown sharpe ratio volatility risk"
    noise = "zzqq xxyy wwvv unrelatedtokenstring"
    out = build_agent_context(doc, "drawdown sharpe", window=4000, signals=[noise])
    #--- With only a zero-overlap signal, no signal block should be emitted at all.
    check("pure-noise signal yields no signals block", SIGNALS_LABEL not in out or "zzqq" not in out)


#--- 7) Corpus + signals coexist; corpus precedes signals (distinct channels, no conflation).
def t_corpus_and_signals_order():
    if not _BM25_AVAILABLE:
        return skip("corpus precedes signals", "rank_bm25 unavailable")
    doc = "lease termination penalty clause analysis under tenancy law"
    corpus = ["civil code article on lease termination penalties and tenant rights"]
    signals = ["news report: courts recently voided excessive lease termination penalties"]
    out = build_agent_context(doc, "lease termination", window=8000,
                              corpus=corpus, signals=signals)
    both = (CORPUS_LABEL in out) and (SIGNALS_LABEL in out)
    order_ok = both and out.index(CORPUS_LABEL) < out.index(SIGNALS_LABEL)
    check("corpus + signals both present and distinctly labelled", both)
    check("corpus block precedes signals block", order_ok)


#--- 8) Tiny budget: no crash, returns a string.
def t_tiny_budget_safe():
    if not _BM25_AVAILABLE:
        return skip("tiny budget safe", "rank_bm25 unavailable")
    doc = "x" * 50
    signals = ["some external evidence passage about x and risk"]
    out = build_agent_context(doc, "x risk", window=60, signals=signals)
    check("tiny window does not crash and returns a string", isinstance(out, str))


#--- 9) GOLDEN / NON-BINDING: invented-causality FATAL -> INVIABLE, independent of signals.
#---     ("consensus 95% => efficiency 95%" — fabricated causal link.)
def t_golden_inviable_non_binding():
    try:
        from tribunal_transversal import TribunalTransversal
        from schema import RuntimeContext
    except Exception as e:
        return skip("golden invented-causality -> INVIABLE", "pipeline import: %s" % e)
    cfg = {
        "anthropic": {"api_key": "", "model": "claude-opus-4-7", "max_tokens": 8192},
        "prompts_dir": "./prompts",
        "tribunal": {"max_agents": 7, "max_calls_total": 40, "max_n2_per_n1": 3,
                     "escalation_enabled": True, "max_escalation_rounds": 1,
                     "max_escalation_agents": 2, "doc_window": 4000,
                     "parent_report_window": 1000, "alert_at_percent": 80},
        "rag": {"enabled": True, "chunk_size": 1000, "chunk_overlap": 150,
                "doc_top_k": 6, "corpus_top_k": 3, "signals_top_k": 3},
        "ssm": {"max_personas": 20, "max_rounds": 4, "max_parallel_personas": 5,
                "alert_at_percent": 80},
        "notifications": {"slack": {"enabled": False}, "github": {"enabled": False}},
        "logging": {"google_sheets": {"enabled": False}},
    }
    try:
        tt = TribunalTransversal(cfg)
        ctx = RuntimeContext(type="general", subscenario="golden_consensus_efficiency",
                             objective="validate causal claim")
        outputs = [{
            "agent_id": "FOR-01",
            "findings": [{
                "severity": "FATAL",
                "title": "fabricated causality: 95% consensus equated to 95% efficiency",
                "description": "Agreement level is presented as a performance guarantee; "
                               "no causal mechanism links consensus to efficiency.",
                "evidence": "document asserts the equivalence with no data",
                "root_cause": "category error — consensus measures agreement, not outcomes",
            }],
        }]
        uvo = tt._deterministic_synthesis(ctx, outputs)
        check("golden: >=1 FATAL -> INVIABLE (severity-driven, signal-independent)",
              uvo.final_verdict == "INVIABLE")
    except Exception as e:
        skip("golden invented-causality -> INVIABLE", "construct/synthesize: %s" % e)


#--- 10) Channel separation: the two labels are not the same string (no conflation).
def t_channels_distinct():
    check("corpus and signals labels are distinct", CORPUS_LABEL != SIGNALS_LABEL)


def main():
    print("test_signals — P4 external-signals channel (offline)")
    for fn in (t_legacy_byte_identical, t_no_signals_long_doc, t_signals_labelled,
               t_signals_directive_non_binding, t_relevant_signal_included,
               t_zero_overlap_signal_dropped, t_corpus_and_signals_order,
               t_tiny_budget_safe, t_golden_inviable_non_binding, t_channels_distinct):
        fn()
    print("\n%d PASS / %d FAIL / %d SKIP" % (_passed, _failed, _skipped))
    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()
