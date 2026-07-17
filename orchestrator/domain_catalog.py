"""
Dark Strategist — Domain Catalog Loader
Version: 1.0.0 (v3.24.0 — GAP #1 fix, decision (a))

Closes GAP #1 (cert-surface <-> runtime): extracts the BINDING severity /
Failure Catalog block from a domain variant .md file under prompts/, so the
runtime Forense N1 prompts (built by PromptEngine) actually receive the
domain-specific severity rules (e.g. Legal RULE LG08/LG09 hard gates)
instead of only the generic MASTER_TEMPLATE.

FORENSE-ONLY INJECTION (deliberate — do not "restore" this to both layers):
  Agentes de Rol never receive this block. Their output contract has no
  severity/findings fields at all, so a severity rulebook is inapplicable
  there. More importantly, the Tribunal's two N1 layers are blind peers by
  design: priming the Rol layer with the Forense layer's taxonomy makes
  simulated actors reason like auditors, which artificially suppresses genuine
  ROL<->FORENSE clashes, shrinks conflicts_detected, and inflates confidence
  downstream — the same failure family as LW-2 / LW-5. Enforced by
  test_domain_catalog_all19.py (injection-surface checks).

DESIGN — explicit marker convention, not heading-slice:
  The injectable block in each variant .md MUST be delimited by ONE OR MORE
  (possibly non-contiguous) marker pairs:
      <!-- CATALOG:START -->
      ... binding severity rules / Failure Catalog tables only ...
      <!-- CATALOG:END -->
  Multiple pairs are concatenated in document order (Legal uses 2 disjoint
  pairs: GEOFENCE+Domain Rules, then — skipping the non-binding Severity x
  Likelihood section and the 7-Levels analysis framework — the Sub-Area
  Failure Catalog tables). Rationale: heading-based slicing ("from ##
  SEVERITY TAXONOMY to ## WAR ROOM") is fragile — a future heading
  rename/reorder silently breaks extraction with no error, AND it cannot skip
  an unwanted section sitting between two wanted ones without over- or
  under-capturing. Explicit markers are auditable (JARP can see the exact
  boundary in the file) and fail SAFE: no markers found = "" (no injection),
  never a partial/wrong slice. Fail-safe is NOT fail-silent — see ANOMALY
  WARNING below.

MIGRATION STATUS (v3.24.0):
  All 19 domain variant files under prompts/ carry the marker convention.
  P01 General has no dedicated variant file and no DOMAIN_PROMPT_FILE entry,
  so it returns "" by design. The fallback path stays load-bearing: any future
  domain, or any file that loses or renames its markers, returns "" —
  identical to v3.23.0 behavior, zero regression — rather than a partial or
  wrong slice. Migrating a future domain is a content-only change (add the
  marker lines to that one file); no code change required.

ANOMALY WARNING (v3.24.0 — fail-safe must not mean fail-silent):
  Two conditions both produce "" and must NOT be conflated:
    (1) domain has no DOMAIN_PROMPT_FILE entry (P01 General) -> expected and
        silent. There is nothing to inject and nothing is wrong.
    (2) domain DECLARES a catalog file but it cannot be read, or yields no
        marker content -> ANOMALY. That domain's binding severity rules
        (e.g. Legal LG08/LG09) silently fail to reach the Forense N1 prompts
        and the tribunal falls back to generic model judgement, leaving no
        trace in the verdict or the transparency report.
  Case (2) now warns on stderr. Rationale: the v3.24.0 cert claims "the
  injection happens". A "" that cannot be told apart from success makes that
  claim unverifiable on every run after the certifying one — which is the
  same class of defect GAP #1 itself was: a surface declared binding that the
  runtime may not actually consume. The fallback stays (never crash the
  tribunal); it just stops being mute.
  Historic live trigger (s39, FIXED in v3.24.0): the './prompts' default
  resolved against the CWD, so invoking main.py from orchestrator/ - the CWD
  its own usage block documents - yielded "" for all 19 domains. main.py now
  anchors the default to the repo (Path(__file__).parent.parent / "prompts");
  DS_PROMPTS_DIR still overrides. The warning stays: a wrong DS_PROMPTS_DIR, a
  moved prompts/ dir, or a lost marker pair still produce "" and must not be
  mute.

UPSTREAM OF THIS MODULE (LW-8, v3.24.0):
  Case (1) below - "General declares no catalog, expected and silent" - is
  true of THIS module but was load-bearing for a defect one layer up. In
  `--document` mode ContextBuilder resolved the domain from the FILENAME STEM,
  so a Legal document named `mindmate_tos.txt` landed on the General sink and
  reached case (1): "" returned, silently, correctly, and the LG08/LG09 hard
  gates never applied. The filename decided whether the gates ran. Fixed
  upstream: ContextBuilder now falls back to document-content resolution on
  the General sink only (never overriding a stem match, so LW-1 routing is
  byte-identical), and RuntimeContext.domain_resolution declares the
  provenance in the transparency report. This module is unchanged: General
  having no catalog was never the lie - claiming the document was General was.

SCOPE OF WHAT GOES INSIDE THE MARKERS (per variant, decided during migration):
  Include:  severity taxonomy, GEOFENCE / tier-shift rules, "Domain Rules"
            (e.g. LG01-LG09), Failure Catalog tables (auto-severity mappings).
  Exclude:  Phase 0 intake protocol, BLOCK 0-7 output-format instructions,
            Severity x Likelihood non-binding triage metadata, WAR ROOM
            sub-agent orchestration, AI disclaimer block.
  Reason for exclusion: those sections either describe a competing output
  contract (BLOCK 0-7) that conflicts with the runtime's JSON schema
  (schema.Finding / UnifiedVerdictOutput, parsed via json.loads in
  tribunal_transversal.py::_call_agent), or are handled by a different
  runtime component already (SubAgentSpawner routing, AFO synthesis output).
  Injecting them would risk the model emitting BLOCK-format prose instead of
  the required JSON -> _call_agent falls back to
  {"raw_output": text, "preliminary_verdict": "UNKNOWN"} -> silent regression.
  This is exactly why "inject the whole file" (the naive version of fix (a))
  was rejected in favor of marker-scoped extraction.
"""

import re
import sys
from pathlib import Path

from catalogs import DOMAIN_PROMPT_FILE

_MARKER_RE = re.compile(
    r"<!--\s*CATALOG:START\s*-->(.*?)<!--\s*CATALOG:END\s*-->",
    re.DOTALL,
)

# Process-lifetime cache: variant files are static per deployment; avoids
# re-reading + re-parsing the same file on every N1 call within a session.
_cache: dict = {}


def _warn(msg: str) -> None:
    """
    Reports a catalog ANOMALY (see ANOMALY WARNING in the module docstring).
    stderr, not stdout, so it never contaminates the verdict text or the
    transparency report on a piped run. load_domain_catalog caches before
    returning, so each (domain, prompts_dir) warns at most once per process:
    loud enough to be seen, quiet enough not to spam the N1 loop.
    """
    print(f"[DOMAIN_CATALOG] WARNING: {msg}", file=sys.stderr)


def load_domain_catalog(domain: str, prompts_dir: str) -> str:
    """
    Returns the extracted binding-rules block for `domain`, or "" when:
      - domain has no entry in DOMAIN_PROMPT_FILE (e.g. "General")
        -> expected, silent;
      - the mapped file cannot be read under prompts_dir -> ANOMALY, warns;
      - the file is readable but yields no CATALOG marker content
        -> ANOMALY, warns.
    Never raises — a missing catalog must degrade to v3.23.0 behavior (no
    injection), not crash the tribunal. But a DECLARED catalog that fails to
    load is reported: silence would make the v3.24.0 injection claim
    unverifiable at runtime.
    """
    key = (domain, str(prompts_dir))
    if key in _cache:
        return _cache[key]

    filename = DOMAIN_PROMPT_FILE.get(domain)
    if not filename:
        #--- No catalog declared for this domain (P01 General): expected, silent.
        _cache[key] = ""
        return ""

    path = Path(prompts_dir) / filename
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        _warn(
            f"domain {domain!r} declares catalog file {filename!r} but it could "
            f"not be read at {path} ({exc.__class__.__name__}). NO INJECTION: "
            f"this domain's binding severity rules will NOT reach the Forense N1 "
            f"prompts; severity falls back to generic model judgement. Check "
            f"prompts_dir (config key 'prompts_dir' / env DS_PROMPTS_DIR; the "
            f"default is anchored to <repo>/prompts since v3.24.0, so this "
            f"usually means DS_PROMPTS_DIR is set wrong or prompts/ moved)."
        )
        _cache[key] = ""
        return ""

    blocks = [m.strip() for m in _MARKER_RE.findall(text)]
    catalog = "\n\n".join(b for b in blocks if b)
    if not catalog:
        _warn(
            f"domain {domain!r} maps to {filename!r} but no CATALOG:START/END "
            f"marker pair yielded content at {path}. NO INJECTION: this domain's "
            f"binding severity rules will NOT reach the Forense N1 prompts. "
            f"Verify the markers survived the last edit to that file."
        )
    _cache[key] = catalog
    return catalog


def build_catalog_block(domain: str, prompts_dir: str) -> str:
    """
    Wraps the extracted catalog (if any) in the injection block consumed by
    PromptEngine's MASTER_TEMPLATE — Forense N1 only. ROLE_AGENT_TEMPLATE
    does not receive it (see FORENSE-ONLY INJECTION in the module docstring).
    Returns "" (no block at all — clean template, no dangling header) when
    the domain has no catalog, so MASTER_TEMPLATE output stays byte-identical
    to v3.23.0 for those domains.
    """
    catalog_text = load_domain_catalog(domain, prompts_dir)
    if not catalog_text:
        return ""

    return (
        "DOMAIN-SPECIFIC FAILURE CATALOG (BINDING — apply verbatim when assigning severity)\n"
        "The following rules are authoritative for severity classification in this\n"
        "domain. They govern HOW you assign FATAL/SERIOUS/MODERATE/LATENT to the\n"
        "findings you report below. They do NOT define your output format — your\n"
        "output format is the OUTPUT FORMAT (JSON) section below, unchanged. Ignore\n"
        "any phase, intake, or output-format instructions implied by this block; it\n"
        "is a severity-rules reference only.\n\n"
        f"{catalog_text}\n\n"
        "END DOMAIN-SPECIFIC FAILURE CATALOG"
    )
