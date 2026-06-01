# ─── stop-slop — AI Prose Quality Scorer (advisory, score-only) ──────────────
"""
slop_filter — Scores the agent's own narrative prose for AI-writing tells.
SCORE-ONLY: returns a dict, never mutates findings or the verdict. Self-contained
(stdlib only, no LLM, no network) so it runs identically under free or Opus
backends and adds zero cert-surface to synthesis logic.

Five dimensions, 0-10 each (cleaner = higher). Total 0-50.
PASS if score >= 35 (threshold), else REVIEW (advisory flag only).
"""
import re

_BANNED = [
    "delve", "tapestry", "testament to", "navigate the complexities",
    "in today's fast-paced", "it's worth noting", "it is worth noting",
    "plays a crucial role", "plays a vital role", "a myriad of",
    "in the realm of", "at the end of the day", "rich tapestry",
    "ever-evolving", "unlock the potential", "game-changer", "robust solution",
]
_CLICHE = [
    "not only", "but also", "in conclusion", "overall,", "moreover,",
    "furthermore,", "in summary", "it is important to", "needless to say",
]
_HEDGE = [
    "arguably", "perhaps", "it could be argued", "to some extent",
    "relatively", "fairly", "somewhat", "in many ways", "generally speaking",
]


def _deduct(text_lc: str, terms: list, per_hit: float) -> float:
    hits = sum(text_lc.count(t) for t in terms)
    return max(0.0, 10.0 - per_hit * hits)


def score_prose(text: str) -> dict:
    """Return {score, max, threshold, flag, dimensions}. Score-only; no mutation."""
    if not text or not text.strip():
        return {"score": 50, "max": 50, "threshold": 35, "flag": "PASS",
                "dimensions": {"empty": True}}

    lc = text.lower()
    words = max(1, len(text.split()))

    em_density = text.count("—") / words * 100
    d_emdash = 10.0 if em_density <= 1.5 else max(0.0, 10.0 - (em_density - 1.5) * 2)
    triples = len(re.findall(r",\s*\w+[\w\s]*,\s*(?:and|or)\s+\w+", lc))

    dims = {
        "banned_phrases": round(_deduct(lc, _BANNED, 2.0), 1),
        "structural_cliche": round(_deduct(lc, _CLICHE, 1.5), 1),
        "hedging": round(_deduct(lc, _HEDGE, 1.5), 1),
        "em_dash": round(d_emdash, 1),
        "rule_of_three": round(max(0.0, 10.0 - triples * 1.5), 1),
    }
    score = round(sum(dims.values()))
    return {"score": score, "max": 50, "threshold": 35,
            "flag": "PASS" if (score >= 35 and min(dims.values()) > 0) else "REVIEW",
            "dimensions": dims}