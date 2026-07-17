"""
Dark Strategist v3.24.0 — LW-8 content-based domain resolution tests.

Offline. No API calls. Run from orchestrator/:
    python test_domain_content_resolution.py

Covers:
  A. MONOTONICITY GUARD — the stem ALWAYS wins. Non-regression proof for LW-1
     (PA-20260607-002 / v3.17.0). If this fails, LW-8 broke a certified contract.
  B. Content resolution — a Legal document named like nothing resolves Legal.
  C. ANTI-FALSE-POSITIVE — the refuted `reuse DOMAIN_MAP over prose` hypothesis
     stays dead: "mental health" / "intellectual property" / "user content" /
     "data security" must NOT route a domain on their own.
  D. Whole-word matching — no substring bleed (same defect class as LW-1 #1).
  E. Provenance — every resolution path declares itself; the General sink is
     never silent.
  F. Signal-table integrity — the 13 certified L07 signals, verbatim.
"""

import sys

from catalogs import DOMAIN_CONTENT_SIGNALS, DOMAIN_MAP, DOMAIN_PROMPT_FILE
from context_builder import (ContextBuilder, resolve_domain_from_content,
                             score_domain_signals)
from schema import RuntimeContext

RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond), detail))


def build(case):
    return ContextBuilder().build(case)


def base_case(**kw):
    case = {"type": "general", "subscenario": "doc", "objective": "identify risks"}
    case.update(kw)
    return case


# ── Fixtures ─────────────────────────────────────────────────────────────────

# Shaped after the real _livewatch fixture: an AI companion ToS reachable by
# minors, with a self-harm crisis path. Carries L05 + L07 signals.
TOS_AI_COMPANION = """
    MindMate Terms of Service. By creating an account you accept this EULA.
    The service is a companion AI chatbot. We do not perform age verification
    and do not require parental consent; minors may register freely.
    Users discussing self-harm are not routed to any external crisis protocol.
    We disclaim any warranty regarding mental health outcomes. Our AI governance
    program is described separately. Emotional dependency is a known effect.
"""

# A genuine clinical document. Says "mental health" and "consent" repeatedly.
# Under the refuted DOMAIN_MAP-over-prose hypothesis this routed Medical via the
# `health` key; here it must simply stay undecided (Medical is not in the table).
CLINICAL_NOTE = """
    Clinical protocol for the mental health unit. The attending physician
    obtains informed consent from each patient prior to enrollment. Adverse
    events are reported weekly. Data security controls follow hospital policy.
"""

# A product/marketing strategy doc. Full of exactly the generic words that were
# EXCLUDED from the signal subset: content, security, policy, property, people.
MEDIA_STRATEGY = """
    Q3 content strategy. We will grow the audience across platforms, protect our
    intellectual property, tighten data security, and update the moderation
    policy. Our people will own distribution. Copyright is handled by legal.
"""


# ── A. MONOTONICITY GUARD — the stem ALWAYS wins ─────────────────────────────

ctx = build(base_case(type="contract", subscenario="whatever",
                      domain_hint="Trading",
                      domain_signal_evidence={"Trading": ["a", "b", "c"]}))
check("A1 declared-type beats a content hint",
      ctx.domain == "Legal", f"got {ctx.domain}")
check("A1b provenance is declared-type",
      ctx.domain_resolution == "declared-type", ctx.domain_resolution)

ctx = build(base_case(type="unmapped", subscenario="alquiler_2026",
                      domain_hint="Trading",
                      domain_signal_evidence={"Trading": ["a", "b", "c"]}))
check("A2 subscenario-keyword beats a content hint",
      ctx.domain == "Legal", f"got {ctx.domain}")
check("A2b provenance is subscenario-keyword",
      ctx.domain_resolution == "subscenario-keyword", ctx.domain_resolution)

# Byte-identical routing: every stem that resolved in v3.23.0 still resolves the
# same, with no hint present at all.
_stem_ok = all(
    build(base_case(type="unmapped", subscenario=k)).domain == v
    for k, v in DOMAIN_MAP.items()
)
check("A3 all 83 DOMAIN_MAP stems resolve unchanged with no hint", _stem_ok)


# ── B. Content resolution ────────────────────────────────────────────────────

hint, ev = resolve_domain_from_content(TOS_AI_COMPANION)
check("B1 AI companion ToS resolves Legal by content",
      hint == "Legal", f"got {hint!r} ev={ev}")

ctx = build(base_case(type="general", subscenario="mindmate_tos",
                      domain_hint=hint, domain_signal_evidence=ev))
check("B2 General sink is rescued by the content hint",
      ctx.domain == "Legal", f"got {ctx.domain}")
check("B3 provenance is document-content",
      ctx.domain_resolution == "document-content", ctx.domain_resolution)
check("B4 Legal declares a catalog file (LG08/LG09 can now be injected)",
      DOMAIN_PROMPT_FILE.get(ctx.domain) == "system_prompt_legal.md")
check("B5 evidence is carried into the context",
      ctx.domain_signals.get("Legal"), ctx.domain_signals)
for sig in ("minors", "age verification", "parental consent", "self-harm"):
    check(f"B6 L07 signal {sig!r} detected in the fixture",
          sig in ctx.domain_signals.get("Legal", []))


# ── C. ANTI-FALSE-POSITIVE — the refuted hypothesis stays dead ───────────────

hint, ev = resolve_domain_from_content(CLINICAL_NOTE)
check("C1 clinical note does NOT route a domain on 'mental health' alone",
      hint is None, f"got {hint!r} ev={ev}")

hint, ev = resolve_domain_from_content(MEDIA_STRATEGY)
check("C2 media strategy does NOT route on content/security/property/policy",
      hint is None, f"got {hint!r} ev={ev}")

for generic in ("security", "policy", "title", "board", "consent", "debt",
                "vendor", "subscription", "saas", "patent", "termination",
                "classification"):
    check(f"C3 generic term {generic!r} is excluded from the signal subset",
          generic not in DOMAIN_CONTENT_SIGNALS["Legal"])

check("C4 two signals are below threshold (no route)",
      resolve_domain_from_content("This nda and this msa.")[0] is None)
check("C5 empty document routes nothing",
      resolve_domain_from_content("")[0] is None)
check("C6 None document routes nothing",
      resolve_domain_from_content(None)[0] is None)


# ── D. Whole-word matching — no substring bleed ──────────────────────────────

check("D1 'nda' does not match inside 'agenda'/'Rwanda'",
      not score_domain_signals("The agenda in Rwanda was long."))
check("D2 'tos' does not match inside 'photos'/'custos'",
      not score_domain_signals("We reviewed the photos."))
check("D3 'sow' does not match inside 'sowing'",
      not score_domain_signals("Sowing season starts in May."))
check("D4 hyphenated signal matches its normalized form",
      "self-harm" in score_domain_signals(
          "self-harm and self harm").get("Legal", []))


# ── E. Provenance — the General sink is never silent ─────────────────────────

ctx = build(base_case(type="general", subscenario="mindmate_tos"))
check("E1 no hint -> General sink",
      ctx.domain == "General", ctx.domain)
check("E2 General sink declares itself",
      ctx.domain_resolution == "general-sink", ctx.domain_resolution)
check("E3 General declares NO catalog file (this is the LW-8 blast radius)",
      DOMAIN_PROMPT_FILE.get("General") is None)

hint, ev = resolve_domain_from_content(CLINICAL_NOTE)
ctx = build(base_case(type="general", subscenario="note",
                      domain_hint=hint, domain_signal_evidence=ev))
check("E4 undecided content still reports its evidence on the sink",
      ctx.domain == "General" and ctx.domain_resolution == "general-sink",
      f"{ctx.domain}/{ctx.domain_resolution}")

check("E5 provenance is never left unknown after build()",
      all(build(base_case(type=t, subscenario=s)).domain_resolution != "unknown"
          for t, s in (("contract", "x"), ("general", "y"), ("zz", "alquiler"))))


# ── F. Signal-table integrity ────────────────────────────────────────────────

L07_CERTIFIED = [
    "ai governance", "ai assessment", "algorithmic", "ai vendor", "minors",
    "age verification", "parental consent", "mental health",
    "emotional dependency", "crisis protocol", "self-harm", "companion ai",
    "chatbot safety",
]
for sig in L07_CERTIFIED:
    check(f"F1 certified L07 signal {sig!r} present",
          sig in DOMAIN_CONTENT_SIGNALS["Legal"])

# v3.22.0 changed this signal deliberately (`minor` -> `minors`). Continuity v39
# regressed it to the singular from memory. This test pins the certified form.
check("F2 'minor' (singular, pre-v3.22.0) is NOT in the table",
      "minor" not in DOMAIN_CONTENT_SIGNALS["Legal"])

check("F3 no duplicate signals",
      len(DOMAIN_CONTENT_SIGNALS["Legal"]) ==
      len(set(DOMAIN_CONTENT_SIGNALS["Legal"])))
check("F4 every signal is lowercase and non-empty",
      all(s and s == s.lower() for s in DOMAIN_CONTENT_SIGNALS["Legal"]))
check("F5 every table domain declares a catalog file",
      all(d in DOMAIN_PROMPT_FILE for d in DOMAIN_CONTENT_SIGNALS))
check("F6 'General' is never a routable content domain",
      "General" not in DOMAIN_CONTENT_SIGNALS)


# ── G. Provenance rendering — C2 is only real if the reader sees it ──────────

from context_builder import describe_domain_resolution

ctx = build(base_case(type="general", subscenario="mindmate_tos"))
line = describe_domain_resolution(ctx)
check("G1 general-sink line names the sink", "general-sink" in line, line)
check("G2 general-sink line states NO rules were injected",
      "NO binding severity rules" in line, line)
check("G3 general-sink line names the gates that did not apply",
      "LG08" in line and "LG09" in line, line)
check("G4 general-sink line tells the operator what to do",
      "--type" in line, line)

hint, ev = resolve_domain_from_content(TOS_AI_COMPANION)
ctx = build(base_case(type="general", subscenario="mindmate_tos",
                      domain_hint=hint, domain_signal_evidence=ev))
line = describe_domain_resolution(ctx)
check("G5 document-content line names the source", "document-content" in line, line)
check("G6 document-content line shows the evidence", "Legal:" in line, line)

ctx = build(base_case(type="unmapped", subscenario="alquiler"))
line = describe_domain_resolution(ctx)
check("G7 subscenario-keyword line warns it is the filename stem",
      "FILENAME STEM" in line, line)

ctx = build(base_case(type="contract", subscenario="x"))
check("G8 declared-type line names the operator pin",
      "declared-type" in describe_domain_resolution(ctx))

# Undecided content on the sink must still surface its evidence — the omission
# is declared, never dropped.
hint, ev = resolve_domain_from_content(CLINICAL_NOTE)
ctx = build(base_case(type="general", subscenario="note",
                      domain_hint=hint, domain_signal_evidence=ev))
line = describe_domain_resolution(ctx)
check("G9 undecided sink still reports the signals it saw",
      "undecided" in line and "mental health" in line, line)

check("G10 a bare RuntimeContext reports unknown, never a false claim",
      "unknown" in describe_domain_resolution(RuntimeContext(
          type="t", subscenario="s", objective="o")))


# ── Report ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    passed = sum(1 for _, ok, _ in RESULTS if ok)
    failed = len(RESULTS) - passed
    for name, ok, detail in RESULTS:
        if not ok:
            print(f"  FAIL  {name}  {detail}")
    print(f"\ntest_domain_content_resolution: {passed} PASS / {failed} FAIL")
    sys.exit(1 if failed else 0)
