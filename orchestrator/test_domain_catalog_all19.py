"""
Offline regression test - CATALOG marker extraction across all 19 migrated
domain variant files (Legal pilot + 18-domain rollout, session s38/"continuar").

No live model calls. Validates, per domain:
  1. load_domain_catalog() returns non-empty binding-rules text.
  2. The extracted text contains at least one domain Rule ID (XX-series).
  3. The extracted text does NOT leak output-format / phase / orchestration
     content that would conflict with the runtime's own JSON output contract
     (the core risk this whole design exists to prevent).
  4. build_catalog_block() wraps the text with the non-binding disclaimer
     header/footer without mutating the rule content itself.
Plus control cases: a catalog-less domain ("General") and a truly unknown key
must return "" (zero-regression fallback).

Plus injection-surface regression guard (v3.24.0 hardening): the catalog must
reach the Forense N1 template ONLY. Injecting it into the Rol template primes
simulated actors with the auditor taxonomy, breaks the blind-peer separation
between the two N1 layers, suppresses ROL<->FORENSE clashes and inflates
confidence downstream (LW-2 / LW-5 failure family).

Plus anomaly-warning guard (v3.24.0): a domain that DECLARES a catalog but
fails to load one must warn on stderr, while a catalog-less domain (General)
stays silent. Without this, the cert claim "the injection happens" is
unverifiable on every run after the certifying one.
"""

import io
import sys
from contextlib import redirect_stderr
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent))
from domain_catalog import load_domain_catalog, build_catalog_block  # noqa: E402
from prompt_engine import (  # noqa: E402
    PromptEngine,
    MASTER_TEMPLATE,
    ROLE_AGENT_TEMPLATE,
)

PROMPTS_DIR = str(Path(__file__).parent.parent / "prompts")

DOMAIN_RULE_PREFIX = {
    "Trading": "Rule 09",
    "Legal": "RULE LG0",
    "Financial": "RULE F0",
    "Cloud": "RULE CL0",
    "Code": "RULE C0",
    "Cybersecurity": "RULE CY0",
    "Agriculture": "RULE A0",
    "Real Estate": "RULE RE0",
    "Science": "RULE S0",
    "Medical": "RULE MD0",
    "Media": "RULE M0",
    "E-Commerce": "RULE EC0",
    "Telecom": "RULE TC0",
    "Public Sector": "RULE PS0",
    "Marketing": "RULE MK0",
    "Operations": "RULE OP0",
    "Human Resources": "RULE HR0",
    "Strategy": "RULE ST0",
    "Startup": "RULE SU0",
}

FORBIDDEN_LEAKS = [
    "## OUTPUT FORMAT",
    "## WAR ROOM",
    "## PHASE 0",
    "MANDATORY INTAKE",
    "## BLOCK 0",
    "## BLOCK 1",
    "json.loads",
]
# Note: bare "BLOCK 0"/"BLOCK 1" (no heading marker) can legitimately appear
# in prose within a binding rule (e.g. Legal's Geofence rule: "Document each
# applied condition in the BLOCK 1 header") -- that is a cross-reference to
# where a finding surfaces, not a competing output-format definition. Only
# an actual "## BLOCK N" heading would mean a full alternate format leaked in.

passed = 0
failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name}")


print(f"Testing {len(DOMAIN_RULE_PREFIX)} migrated domains against {PROMPTS_DIR}\n")

for domain, rule_prefix in DOMAIN_RULE_PREFIX.items():
    print(f"[{domain}]")
    catalog = load_domain_catalog(domain, PROMPTS_DIR)

    check(f"{domain}: catalog non-empty", len(catalog) > 0)
    check(f"{domain}: contains {rule_prefix}", rule_prefix in catalog)

    for leak in FORBIDDEN_LEAKS:
        check(f"{domain}: does NOT leak '{leak}'", leak not in catalog)

    block = build_catalog_block(domain, PROMPTS_DIR)
    check(f"{domain}: build_catalog_block wraps with disclaimer header",
          "DOMAIN-SPECIFIC FAILURE CATALOG (BINDING" in block)
    check(f"{domain}: build_catalog_block preserves rule content",
          rule_prefix in block)
    print()

print("[Control: unmigrated domain]")
empty = load_domain_catalog("General", PROMPTS_DIR)
check("General (no dedicated catalog file) returns ''", empty == "")
empty_block = build_catalog_block("General", PROMPTS_DIR)
check("General build_catalog_block returns ''", empty_block == "")

unknown = load_domain_catalog("NotARealDomain", PROMPTS_DIR)
check("Unknown domain key returns '' (no crash)", unknown == "")

print("\n[Control: injection surface -- FORENSE only, never ROL]")
check("MASTER_TEMPLATE (Forense) carries the catalog placeholder",
      "{domain_catalog_block}" in MASTER_TEMPLATE)
check("ROLE_AGENT_TEMPLATE (Rol) carries NO catalog placeholder",
      "{domain_catalog_block}" not in ROLE_AGENT_TEMPLATE)

_ctx = SimpleNamespace(
    domain="Legal",
    subscenario="contract_review",
    objective="audit",
    regime="STRICT",
    regime_description="strict regime",
    tools=["general_analysis"],
)
_engine = PromptEngine(prompts_dir=PROMPTS_DIR)
_rol_prompt = _engine.build_rol_prompt("ROL-1", "Counterparty Counsel", _ctx)
_for_prompt = _engine.build_forense_prompt("FOR-1", "Forensic Auditor", _ctx)

check("build_rol_prompt does NOT inject the catalog (Legal)",
      "DOMAIN-SPECIFIC FAILURE CATALOG" not in _rol_prompt)
check("build_rol_prompt does NOT leak Legal rule IDs into the simulation",
      "RULE LG0" not in _rol_prompt)
check("build_forense_prompt DOES inject the catalog (Legal)",
      "DOMAIN-SPECIFIC FAILURE CATALOG" in _for_prompt)
check("build_forense_prompt DOES carry Legal rule IDs",
      "RULE LG0" in _for_prompt)

print("\n[Control: (b) anomaly warning -- fail-safe must not be fail-silent]")

#--- Catalog-less domain: nothing declared, nothing wrong -> stays silent.
#--- Fresh prompts_dir keys so the process cache cannot mask the code path.
_buf = io.StringIO()
with redirect_stderr(_buf):
    _r = load_domain_catalog("General", "./__probe_dir_a__")
check("General (no declared catalog) returns ''", _r == "")
check("General (no declared catalog) does NOT warn", _buf.getvalue() == "")

#--- Declared catalog + unreadable dir -> ANOMALY, must be loud.
_buf = io.StringIO()
with redirect_stderr(_buf):
    _r = load_domain_catalog("Legal", "./__probe_dir_b__")
_err = _buf.getvalue()
check("Legal with bad prompts_dir returns '' (no crash)", _r == "")
check("Legal with bad prompts_dir WARNS on stderr",
      "[DOMAIN_CATALOG] WARNING" in _err)
check("warning identifies the affected domain", "'Legal'" in _err)
check("warning states the rules did NOT reach the Forense prompts",
      "will NOT reach the Forense N1" in _err)

print(f"\n{'=' * 60}")
print(f"TOTAL: {passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
