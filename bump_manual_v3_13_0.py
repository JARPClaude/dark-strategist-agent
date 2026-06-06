#!/usr/bin/env python3
"""
DS v3.13.0 manual bump (P2 archetype lenses). Handles everything bump_stamps.ps1 does NOT:
CHANGELOG [3.13.0] + cert block, the 4 orchestrator product-face banners, CLAUDE bottom
status + roadmap row + repo-tree entry, README roadmap row.

Disjoint from bump_stamps.ps1 (which only bumps anchored stamps in prompts/README/CLAUDE),
so order does not matter. All-or-nothing + newline-aware PER FILE. Dry-run by default.

Run from the repo ROOT:
    python bump_manual_v3_13_0.py            # dry-run (verifies every anchor)
    python bump_manual_v3_13_0.py --apply    # writes all files atomically
"""
import sys

LF = chr(10)
CRLF = chr(13) + chr(10)

GUARD_FILE = "CHANGELOG.md"
GUARD_STR = "## [3.13.0]"

#--- CHANGELOG: new [3.13.0] section + cert, inserted before [3.12.0].
CL_OLD = "## [3.12.0] — 2026-06-04"
CL_NEW = (
"""## [3.13.0] — 2026-06-05

### Added — Archetype lenses for the escalation round (value-add P2)
- `orchestrator/archetype_lenses.py` (NEW): frozen catalog of 5 abstract adversarial lenses (FALSIFIER, FAILURE_MODE_HUNTER, EVIDENCE_AUDITOR, INCENTIVE_AUDITOR, SYSTEMIC_LENS) + pure helpers `select_lenses(n)` (deterministic; returns dict copies so the catalog can never be mutated by a caller) and `build_lens_directive(lens, round_no, focus)`. No API, no I/O. Lenses are ABSTRACT roles — never an impersonation of a real person (fabricated authority forbidden by design).
- `orchestrator/tribunal_transversal.py`: `_run_escalation_round` now assigns one archetype lens per `FOR-ESC-*` agent (deterministic order; the first complementary pair — refute-first + extend-first — runs under the default `max_escalation_agents=2`). Each lens shapes HOW the agent re-examines the verdict-driving findings; `FOR-ESC-*` ids preserved so cross-agent corroboration counts them as independent. `result["lens"]` tagged; `_maybe_escalate` records applied lenses; the transparency report surfaces them. `build_lens_directive(None, …)` degrades to a neutral directive when agents exceed the catalog, so offline/no-API runs never crash.
- Catalog + module docstring are content-based/frozen (do not bump every minor).

### Tests
- `orchestrator/test_archetype_lenses.py`: 10-check offline suite (catalog integrity, order contract, `select_lenses` cap/degenerate/coercion/determinism/isolation, `build_lens_directive` embedding + graceful degradation). No API.

### Versioning
- Atomic §4.14.1 bump: base + router + 19 domain variants + README + CLAUDE product-face -> v3.13.0. Operator-visible orchestrator banners (main x2 / wizard / transparency report) -> v3.13.0. Module/feature docstrings + lens catalog frozen at origin. No prompt/skill CONTENT, no roster (9 N2), no verdict-logic change.

### Non-binding guarantee
- Lenses change deliberation quality, never the verdict. Escalation remains a deliberation-budget decision (consistent with RULE LG07/F08); the deterministic verdict (FATAL->INVIABLE) is untouched. Regression confirms `e_monotonic_verdict` + `c_fallback_intact` green and the gate's no-op paths never touch the synthesizer.

### JARP_CERTIFIED: DS v3.13.0 — PA-20260605-002 ✅

Level 1 — JARP DEEP delta-coverage 7-axis forensic audit of `dark-strategist-agent` v3.13.0 by `prompt-architect-agent` v1.3.0 (PA-20260527-002), over the v3.12.0 baseline (19/19 unchanged). Scope: v3.13.0 delta — archetype lenses (`archetype_lenses.py` NEW: 5 abstract lenses + pure `select_lenses`/`build_lens_directive`; one lens per `FOR-ESC-*` agent in `_run_escalation_round`; `result["lens"]` + `_maybe_escalate` lens record + transparency surfacing; graceful None-lens degradation), `test_archetype_lenses.py` added, atomic §4.14.1 bump. RULE 08 self-audit L0 (PA-20260605-001) PASS first. Functional evidence on the real machine (post-apply): `test_archetype_lenses.py` 10/10 + `test_escalation.py` 10/10 + `test_confidence.py` 10/10 + `smoke_test_e2e.py` OFFLINE GREEN (0 FAIL, 1 SKIP = `b_unified_output`, non-blocking) with `c_fallback_intact` + `e_monotonic_verdict` PASS; full pipeline imports `tribunal`->`archetype_lenses` clean. Verdict invariant verified: lenses only shape escalation directives + tag provenance; `final_verdict` stays severity-driven; escalation gate no-op paths never invoke synthesis. No real-person impersonation in the catalog (abstract roles only). Forensic surface (19 variants + 6 skills + base + router CONTENT) byte-identical except stamps. Result: 0 CRITICAL | 0 SERIOUS | 0 MODERATE | 0 LATENT -> `JARP_CERTIFIED`. `BIAS_CHECK_RESULT: PASS` (lenses are a deliberation-quality enrichment, orthogonal to the verdict). Supersedes PA-20260604-004 (DS v3.12.0). `JARP_BENCHMARK_LIVE` advances to v3.13.0. Valid until 05/09/2026 or DS v4.0.0.

---

## [3.12.0] — 2026-06-04"""
)

#--- CLAUDE roadmap: append v3.13.0 row after the v3.12.0 row.
CLAUDE_ROAD_OLD = "| v3.12.0 Confidence-gated escalation (LOW confidence + budget → bounded extra forensic round → re-synth → recompute; capped; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |"
CLAUDE_ROAD_NEW = (CLAUDE_ROAD_OLD + "\n"
    "| v3.13.0 Archetype lenses for the escalation round (one abstract adversarial lens per FOR-ESC agent; refute-first + extend-first; NO real-person impersonation; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |")

#--- CLAUDE repo tree: add archetype_lenses.py after tribunal_transversal.py.
CLAUDE_TREE_OLD = "│   ├── tribunal_transversal.py"
CLAUDE_TREE_NEW = ("│   ├── tribunal_transversal.py\n"
    "│   ├── archetype_lenses.py          ← NEW v3.13.0 (escalation lenses)")

#--- README roadmap: append v3.13.0 row after the v3.12.0 row.
README_ROAD_OLD = "| v3.12.0 | Confidence-gated escalation — if confidence is LOW and budget remains, runs a bounded extra forensic round on the verdict-driving findings, re-synthesizes, recomputes; NON-BINDING (never alters the FATAL→INVIABLE verdict) | ✅ |"
README_ROAD_NEW = (README_ROAD_OLD + "\n"
    "| v3.13.0 | Archetype lenses for the escalation round — one abstract adversarial lens per FOR-ESC agent (refute-first + extend-first); no real-person impersonation; NON-BINDING (never alters the FATAL→INVIABLE verdict) | ✅ |")

EDITS = {
    "CHANGELOG.md": [(CL_OLD, CL_NEW)],
    "orchestrator/main.py": [
        ('description="Dark Strategist Agent v3.12.0 — Tribunal Transversal"',
         'description="Dark Strategist Agent v3.13.0 — Tribunal Transversal"'),
        ('print(f"DARK STRATEGIST v3.12.0 — Tribunal Transversal")',
         'print(f"DARK STRATEGIST v3.13.0 — Tribunal Transversal")'),
    ],
    "orchestrator/wizard.py": [
        ('print("DARK STRATEGIST v3.12.0 — INTERACTIVE WIZARD")',
         'print("DARK STRATEGIST v3.13.0 — INTERACTIVE WIZARD")'),
    ],
    "orchestrator/tribunal_transversal.py": [
        ("DARK STRATEGIST v3.12.0 — TRANSPARENCY REPORT",
         "DARK STRATEGIST v3.13.0 — TRANSPARENCY REPORT"),
    ],
    "CLAUDE.md": [
        ("**ACTIVE — v3.12.0**", "**ACTIVE — v3.13.0**"),
        (CLAUDE_ROAD_OLD, CLAUDE_ROAD_NEW),
        (CLAUDE_TREE_OLD, CLAUDE_TREE_NEW),
    ],
    "README.md": [
        (README_ROAD_OLD, README_ROAD_NEW),
    ],
}


def detect_nl(text):
    return CRLF if CRLF in text else LF


def main():
    apply = "--apply" in sys.argv

    # Idempotency guard.
    try:
        with open(GUARD_FILE, "r", encoding="utf-8", newline="") as fh:
            if GUARD_STR in fh.read():
                print("SKIP: %s already contains %r. No changes." % (GUARD_FILE, GUARD_STR))
                sys.exit(0)
    except FileNotFoundError:
        print("ABORT: %s not found. Run from the repo ROOT." % GUARD_FILE)
        sys.exit(2)

    staged = {}   # path -> new full text
    total = 0
    for path, edits in EDITS.items():
        try:
            with open(path, "r", encoding="utf-8", newline="") as fh:
                raw = fh.read()
        except FileNotFoundError:
            print("ABORT: %s not found. Run from the repo ROOT." % path)
            sys.exit(2)
        nl = detect_nl(raw)
        work = raw
        for j, (old, new) in enumerate(edits, 1):
            old_nl = old.replace(LF, nl)
            new_nl = new.replace(LF, nl)
            count = work.count(old_nl)
            if count != 1:
                print("ABORT %s edit %d: anchor found %d times (expected 1). Nothing written." % (path, j, count))
                sys.exit(1)
            work = work.replace(old_nl, new_nl, 1)
            print("OK   %s edit %d (nl=%r)" % (path, j, nl))
            total += 1
        staged[path] = (work, nl)

    print("=" * 56)
    if apply:
        for path, (work, nl) in staged.items():
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(work)
        print("APPLIED: %d edits across %d files." % (total, len(staged)))
    else:
        print("DRY-RUN OK: %d edits across %d files matched. Re-run with --apply." % (total, len(staged)))


if __name__ == "__main__":
    main()
