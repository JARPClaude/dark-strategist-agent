"""
Dark Strategist — test_domain_resolver.py
Offline ($0) regression for ContextBuilder._resolve_domain (LW-1 fix).

LW-1 closed TWO defects in the legacy resolver:
  (1) substring bleed — short abbreviation keys ("ma"/"ops"/"hr"/"sop")
      false-matched any stem containing those letters
      (e.g. "transformation" -> Financial via "ma"), mis-routing real
      documents to the wrong variant / Failure Catalog in --document mode;
  (2) order-dependence — routing for multi-domain stems was coupled to
      DOMAIN_MAP insertion order.

This suite locks the boundary-aware, MOST-SPECIFIC-FIRST, order-invariant
contract:
  - repro pair (transformation vs board_proposal)
  - short-key bleed killed (no false Financial/HR/Operations)
  - short keys still match as whole tokens (M&A / ops / hr / nda)
  - long-key prefix tolerance preserved ("cyber" -> Cybersecurity)
  - compound / phrase keys (real_estate / series_a / market_entry)
  - exact-type fast path intact
  - multi-domain collisions: most-specific (longest) keyword wins,
    independent of dict order
Run from orchestrator/:  python test_domain_resolver.py
"""

import sys
from context_builder import ContextBuilder

cb = ContextBuilder()

# (doc_type, subscenario, expected_domain, note)
CASES = [
    # ── LW-1 core repro ──────────────────────────────────────────────────────
    ("", "strategy_acme_transformation", "Strategy",        "repro: was Financial via 'ma' bleed"),
    ("", "strategy_acme_board_proposal", "Strategy",        "repro: control (was correct by accident)"),
    # ── short-key bleed must be killed ───────────────────────────────────────
    ("", "q3_management_review",         "General",         "'ma' must NOT bleed -> Financial"),
    ("", "annual_summary_2026",          "General",         "'ma' (sum-MA-ry) must NOT bleed"),
    ("", "risk_threshold_config",        "General",         "'hr' (t-HR-eshold) must NOT bleed -> HR"),
    ("", "devops_pipeline_audit",        "General",         "'ops' (devOPS) must NOT bleed -> Operations"),
    # ── short keys still match as WHOLE TOKENS (correct) ─────────────────────
    ("", "project_ma_dd",                "Financial",       "'ma' as standalone token = M&A"),
    ("", "acme_ops_handbook",            "Operations",      "'ops' as standalone token"),
    ("", "hr_policy_2026",               "Human Resources", "'hr' as standalone token"),
    ("", "vendor_nda_draft",             "Legal",           "'nda' as standalone token"),
    # ── long-key prefix tolerance preserved ──────────────────────────────────
    ("", "cybersecurity_audit_acme",     "Cybersecurity",   "'cyber' prefix of token 'cybersecurity'"),
    ("", "data_processing_review",       "Operations",      "'process' prefix of token 'processing'"),
    # ── compound / phrase keys ───────────────────────────────────────────────
    ("", "acme_real_estate_deal",        "Real Estate",     "compound key 'real_estate'"),
    ("", "series_a_funding_memo",        "Startup",         "compound key 'series_a'"),
    ("", "market_entry_latam",           "Strategy",        "compound key 'market_entry' (was Financial via 'ma')"),
    # ── exact-type fast path (unchanged) ─────────────────────────────────────
    ("strategy", "whatever_stub",        "Strategy",        "exact type match short-circuits"),
    ("contract", "anything_stub",        "Legal",           "exact type match short-circuits"),
    # ── plain single-domain words ────────────────────────────────────────────
    ("", "marketing_funnel_plan",        "Marketing",       "was Financial via 'ma' bleed"),
    ("", "trading_backtest_xauusd",      "Trading",         "plain trading stem"),
    # ── multi-domain collisions: most-specific (longest) keyword wins ────────
    ("", "social_media_strategy",        "Strategy",        "media(5) vs strategy(8) -> strategy (most specific)"),
    ("", "saas_unit_economics",          "Startup",         "saas(4) vs unit_economics(13) -> startup (most specific)"),
    ("", "cloud_security_review",        "Cybersecurity",   "cloud(5) vs security(8) -> cybersecurity (most specific)"),
    # ── no-match falls through to General ────────────────────────────────────
    ("", "random_stuff_xyz",             "General",         "no domain token -> General"),
]


def run():
    passed = 0
    failed = 0
    for doc_type, sub, expected, note in CASES:
        got = cb._resolve_domain(doc_type, sub)
        ok = (got == expected)
        if ok:
            passed += 1
        else:
            failed += 1
            label = f"[type={doc_type}] {sub}" if doc_type else sub
            print(f"  FAIL  {label:42} got={got!r:18} expected={expected!r:18} ({note})")
    total = passed + failed
    print(f"\ntest_domain_resolver: {passed}/{total} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
