"""
Dark Strategist - Offline structural test for the reputational-risk skill (v3.16.0).

Validates, with zero API / zero network:
  - SKILL.md structure + the five named patterns + VERDICT_IMPACT marker
  - SKILLS_CATALOG registration (registry-only, no logic)
  - activation-subset-binding: the active P11/P16/P19 variants carry [reputational-risk:] tags
  - scope discipline: inactive P14/P20 variants are NOT bound in v1.0.0
  - structural no-verdict-impact: the skill is markdown-only; 'reputational' appears in
    orchestrator/*.py only in catalogs.py (registry), never in verdict-computation logic.

Run from orchestrator/:  python test_reputational_risk.py
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ORCH = REPO_ROOT / "orchestrator"
SKILL = REPO_ROOT / "skills" / "reputational-risk" / "SKILL.md"
PROMPTS = REPO_ROOT / "prompts"

_passed = 0
_failed = 0


def check(name, cond):
    global _passed, _failed
    if cond:
        _passed += 1
        print(f"[PASS] {name}")
    else:
        _failed += 1
        print(f"[FAIL] {name}")


# --- load SKILL.md ---
skill_text = SKILL.read_text(encoding="utf-8") if SKILL.exists() else ""

check("SKILL.md exists", SKILL.exists())
check("frontmatter name == reputational-risk", "name: reputational-risk" in skill_text)
check("frontmatter version 1.0.0", "version: 1.0.0" in skill_text)
check(
    "description names the five patterns",
    all(p in skill_text for p in [
        "misrepresentation", "broken-promise", "stakeholder-betrayal",
        "association-contamination", "silence-in-crisis",
    ]),
)
check("VERDICT_IMPACT: NONE declared", "[VERDICT_IMPACT: NONE" in skill_text)
check("activation declares P11/P16/P19", all(d in skill_text for d in ["P11", "P16", "P19"]))

# --- SKILLS_CATALOG registration (registry-only) ---
sys.path.insert(0, str(ORCH))
reg_ok = False
path_ok = False
try:
    from catalogs import SKILLS_CATALOG
    reg_ok = "reputational-risk" in SKILLS_CATALOG
    if reg_ok:
        path_ok = SKILLS_CATALOG["reputational-risk"] == "skills/reputational-risk/SKILL.md"
except Exception as e:  # pragma: no cover
    print(f"  (catalogs import error: {e})")

check("SKILLS_CATALOG registers reputational-risk", reg_ok)
check("SKILLS_CATALOG path correct + file present", path_ok and SKILL.exists())


# --- activation subset binding: active variants carry the tag ---
def variant_has_tag(fname):
    f = PROMPTS / fname
    return f.exists() and "[reputational-risk:" in f.read_text(encoding="utf-8")


check("Media (P11) variant binds reputational rows", variant_has_tag("system_prompt_media.md"))
check("Marketing (P16) variant binds reputational rows", variant_has_tag("system_prompt_marketing.md"))
check("Strategy (P19) variant binds reputational rows", variant_has_tag("system_prompt_strategy.md"))

# --- scope discipline: inactive variants must NOT bind in v1.0.0 ---
check("Public Sector (P14) NOT bound in v1.0.0", not variant_has_tag("system_prompt_publicsector.md"))
check("Startup (P20) NOT bound in v1.0.0", not variant_has_tag("system_prompt_startup.md"))

# --- structural no-verdict-impact: markdown-only skill ---
# 'reputational' may appear in orchestrator/*.py ONLY in catalogs.py (registry entry),
# never in verdict-computation logic.
offenders = []
for py in ORCH.glob("*.py"):
    if py.name in ("catalogs.py", "test_reputational_risk.py"):
        continue
    if "reputational" in py.read_text(encoding="utf-8").lower():
        offenders.append(py.name)

check("no reputational logic in orchestrator verdict modules", offenders == [])

print(f"\n{_passed}/{_passed + _failed} checks passed.")
sys.exit(0 if _failed == 0 else 1)
