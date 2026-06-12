"""
Dark Strategist v3.18.0 — test_signals_granularity (offline, $0)
Contract for LW-3: the signals channel loads .txt ONE PASSAGE PER LINE, while the
corpus channel keeps the paragraph (\n\n) split. No API, no network.

Pure load-path checks always run. The end-to-end provenance-granularity check
SKIPs (not fails) when the orchestrator import is unavailable (test_provenance discipline).
"""
import os
import sys
import tempfile

from retriever import load_corpus_files

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


def _write(text):
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    return path


#--- 1) DEFAULT mode: consecutive lines (no blank) collapse to ONE passage (legacy preserved).
def t_default_collapses():
    p = _write("signal one alpha\nsignal two beta\nsignal three gamma")
    try:
        check("default .txt collapses consecutive lines to 1 passage",
              len(load_corpus_files(p)) == 1)
    finally:
        os.remove(p)


#--- 2) ATOMIC mode: one passage per non-empty line.
def t_atomic_per_line():
    p = _write("signal one alpha\nsignal two beta\nsignal three gamma")
    try:
        check("atomic .txt yields one passage per line",
              len(load_corpus_files(p, txt_atomic_lines=True)) == 3)
    finally:
        os.remove(p)


#--- 3) ATOMIC mode drops blank lines.
def t_atomic_drops_blanks():
    p = _write("alpha\n\n\nbeta\n   \ngamma\n")
    try:
        check("atomic .txt drops blank/whitespace-only lines",
              load_corpus_files(p, txt_atomic_lines=True) == ["alpha", "beta", "gamma"])
    finally:
        os.remove(p)


#--- 4) CORPUS channel guard: default \n\n split keeps a multi-line clause as ONE passage.
def t_corpus_paragraph_preserved():
    clause = "ARTICLE 12\nThe lessee shall pay rent\nwithin five business days."
    p = _write(clause + "\n\nARTICLE 13\nTermination requires notice.")
    try:
        out = load_corpus_files(p)  # default = corpus behavior
        ok = len(out) == 2 and out[0] == clause and "five business days" in out[0]
        check("corpus .txt keeps multi-line clause as one paragraph passage", ok)
    finally:
        os.remove(p)


#--- 5) REPRO shape: header + blank + 4 consecutive signals.
def t_repro_shape():
    text = ("EXTERNAL SIGNALS header line one.\nEach line is an observation.\n\n"
            "2026-05-30 | Regulatory probe Veld Holdings sanctions ownership.\n"
            "2026-05-12 | Sector study SaaS pivots median realized one three.\n"
            "2026-04-02 | Litigation breach class action non-disclosure aggravating.\n"
            "2026-03-18 | Labor severance disputes equity cliffs settled unvested.")
    p = _write(text)
    try:
        default_n = len(load_corpus_files(p))                       # header + mashed 4 = 2
        atomic_n = len(load_corpus_files(p, txt_atomic_lines=True))  # 2 header + 4 signals = 6
        check("repro: default collapses 4 signals (2 passages), atomic separates (6)",
              default_n == 2 and atomic_n == 6)
    finally:
        os.remove(p)


#--- 6) E2E granularity: two findings over two distinct signal lines get DISTINCT signal_index.
def t_e2e_distinct_index():
    try:
        from tribunal_transversal import TribunalTransversal
        from schema import RuntimeContext
    except Exception:
        return skip("e2e distinct signal_index", "pipeline import")
    cfg = {
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
    try:
        tt = TribunalTransversal(cfg)
    except Exception:
        return skip("e2e distinct signal_index", "pipeline construct")

    p = _write("2026-05-30 | Regulatory probe Veld Holdings sanctions violations beneficial ownership.\n"
               "2026-05-12 | Sector study SaaS pivots median realized one point three twelve months.")
    try:
        #--- replicate run()'s signals-load loop with the LW-3 flag.
        tagged = [(p, passage) for passage in load_corpus_files(p, txt_atomic_lines=True)]
        tt._active_signals_tagged = tagged
        ctx = RuntimeContext(type="general", subscenario="lw3_granularity",
                             objective="attribute findings to signals")
        uvo = tt._deterministic_synthesis(ctx, [{"agent_id": "FOR-01", "findings": [
            {"severity": "FATAL", "title": "regulatory",
             "description": "regulatory probe Veld Holdings sanctions violations",
             "evidence": "beneficial ownership undisclosed", "root_cause": "r"},
            {"severity": "MODERATE", "title": "sector",
             "description": "sector study SaaS pivots median realized",
             "evidence": "one point three twelve months", "root_cause": "r"},
        ]}])
        prov = tt._attribute_signal_provenance(uvo)
        idxs = sorted({pr["signal_index"] for pr in prov})
        ok = len(tagged) == 2 and len(prov) == 2 and idxs == [0, 1]
        check("two findings attribute to two DISTINCT signal lines (LW-3 fixed)", ok)
    finally:
        os.remove(p)


def main():
    print("test_signals_granularity — LW-3 per-line signals load (offline)")
    for fn in (t_default_collapses, t_atomic_per_line, t_atomic_drops_blanks,
               t_corpus_paragraph_preserved, t_repro_shape, t_e2e_distinct_index):
        fn()
    print("\n%d PASS / %d FAIL / %d SKIP" % (_passed, _failed, _skipped))
    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()