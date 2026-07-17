"""
Dark Strategist v3.0.0 — Context Builder
Builds and validates the RuntimeContext object for each case.
Replaces manual flag passing with a structured, validated context.
"""

import re

from catalogs import (ROLE_CATALOG, SSM_CATALOG, DOMAIN_MAP, REGIME_MAP,
                      DEFAULT_REGIME, JURISDICTION_CORPUS_MAP,
                      DOMAIN_CONTENT_SIGNALS)
from schema import RuntimeContext


# Separator normalizer for boundary-aware domain resolution (LW-1 fix).
_SEP = re.compile(r'[^a-z0-9]+')


# ─── LW-8 — CONTENT-BASED DOMAIN RESOLUTION (v3.24.0) ────────────────────────
# Pure module-level functions. The ContextBuilder CLASS stays document-free
# (v3.8.0 contract): `build(case)` receives a RESOLVED DOMAIN STRING via
# `case["domain_hint"]` and never sees document text. main.py owns ingestion and
# therefore owns this call. Keeping these here (not in main.py) keeps them
# offline-testable with no argparse in the way.

#--- Decision thresholds. A single stray term must never route a domain.
_CONTENT_MIN_SIGNALS = 3   # distinct signals the winner must carry
_CONTENT_MIN_MARGIN = 2    # distinct-signal lead over the runner-up


def _normalize_for_match(text: str) -> str:
    """
    Normalizes prose to space-delimited tokens and pads it, so that a padded
    needle matches ONLY on whole-word / whole-phrase boundaries.
    Reuses the certified LW-1 `_SEP` semantics — no new normalization is
    introduced, so signal matching and stem matching cannot drift apart.
    """
    return " " + _SEP.sub(" ", text.lower()).strip() + " "


def score_domain_signals(document_text: str) -> dict:
    """
    Pure. Returns {domain: [distinct signals present]} over DOMAIN_CONTENT_SIGNALS.
    Domains with zero hits are omitted. Order-invariant; deterministic.
    """
    if not document_text:
        return {}
    haystack = _normalize_for_match(document_text)
    hits = {}
    for domain, signals in DOMAIN_CONTENT_SIGNALS.items():
        found = sorted({s for s in signals
                        if _normalize_for_match(s) in haystack})
        if found:
            hits[domain] = found
    return hits


def resolve_domain_from_content(document_text: str):
    """
    Pure, deterministic. Returns (domain | None, evidence).

    `domain` is returned ONLY when the leader carries >= _CONTENT_MIN_SIGNALS
    distinct signals AND leads the runner-up by >= _CONTENT_MIN_MARGIN.
    Otherwise None — the evidence is still returned so an undecided outcome is
    reported rather than dropped.

    FAIL-CLOSED, NOT FAIL-BLOCKING: unlike LW-7 (whose trigger was binary —
    agents_consulted==0), this is heuristic. Withholding a verdict because a
    coffee-shop ToS says "minors" would be fail-closed misapplied. The gate is
    better evidence plus observability, never verdict suppression.
    """
    hits = score_domain_signals(document_text)
    if not hits:
        return None, {}
    ranked = sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    top_domain, top_signals = ranked[0]
    runner_up = len(ranked[1][1]) if len(ranked) > 1 else 0
    if len(top_signals) < _CONTENT_MIN_SIGNALS:
        return None, hits
    if len(top_signals) - runner_up < _CONTENT_MIN_MARGIN:
        return None, hits
    return top_domain, hits


# ─── DOMAIN TOOLS ─────────────────────────────────────────────────────────────
DOMAIN_TOOLS = {
    "Trading":      ["price_action", "volume_profile", "order_flow",
                     "sharpe_ratio", "drawdown_analysis", "regime_detection"],
    "Legal":        ["clause_extraction", "jurisdiction_check",
                     "liability_mapping", "enforceability_analysis"],
    "Financial":    ["dcf_analysis", "sensitivity_testing", "cac_ltv_ratio",
                     "burn_rate_analysis", "comparable_selection"],
    "Cloud":        ["architecture_review", "sla_analysis", "cac_ltv_ratio",
                     "vendor_lock_in_assessment", "dr_plan_check"],
    "Code":         ["static_analysis", "security_scanning", "complexity_check",
                     "test_coverage_review", "dependency_audit"],
    "Cybersecurity":["threat_modeling", "privilege_mapping", "sod_analysis",
                     "owasp_check", "audit_trail_review"],
    "Agriculture":  ["yield_benchmarking", "biosecurity_audit", "climate_modeling",
                     "cold_chain_review", "environmental_impact"],
    "Real Estate":  ["cap_rate_analysis", "dcf_real_estate", "zoning_verification",
                     "construction_cost_benchmark", "rate_sensitivity"],
    "Science":      ["power_analysis", "statistical_validity", "reproducibility_check",
                     "conflict_of_interest_audit", "methodology_review"],
    "Medical":      ["protocol_compliance", "adverse_event_review",
                     "regulatory_compliance", "consent_analysis", "liability_mapping"],
    "Media":        ["platform_dependency_analysis", "ip_ownership_check",
                     "cpm_modeling", "audience_ownership_review"],
    "E-Commerce":   ["unit_economics", "cac_ltv_ratio", "return_rate_modeling",
                     "marketplace_risk", "ad_spend_analysis"],
    "Telecom":      ["spectrum_verification", "capex_benchmarking",
                     "churn_modeling", "arpu_analysis", "vendor_concentration"],
    "Public Sector":["procurement_compliance", "budget_benchmarking",
                     "enforcement_mechanism_check", "stakeholder_mapping"],
    "General":      ["logic_validation", "evidence_mapping",
                     "assumption_audit", "risk_identification"],
}


#--- LW-8 (v3.24.0) — human-readable provenance line for the transparency report.
#--- Pure: reads RuntimeContext, returns a string. POST-verdict, report-only,
#--- NON-BINDING — it cannot touch final_verdict, Finding, or any severity.
#--- Same family as v3.15.0 signal-provenance attribution.
_RESOLUTION_NOTE = {
    "declared-type":
        "declared-type — operator pinned the domain via --type. Document content "
        "not consulted (not needed).",
    "subscenario-keyword":
        "subscenario-keyword — matched a keyword in the SUBSCENARIO STRING. In "
        "--document mode that string is the FILENAME STEM, not the document body.",
    "document-content":
        "document-content — resolved from the document itself (stem carried no "
        "usable signal).",
    "general-sink":
        "general-sink — NO DOMAIN COULD BE RESOLVED. General declares no Failure "
        "Catalog, so NO binding severity rules were injected into the Forense N1 "
        "prompts: any domain hard gate (e.g. Legal RULE LG08 minors / RULE LG09 "
        "self-harm crisis) did NOT apply and severity fell back to generic model "
        "judgement. If this document belongs to a catalog-bearing domain, pin it "
        "with --type and re-run.",
    "unknown":
        "unknown — context was not built by ContextBuilder; provenance unavailable.",
}


def describe_domain_resolution(ctx) -> str:
    """Renders `ctx.domain_resolution` + its evidence for the transparency report."""
    how = getattr(ctx, "domain_resolution", "unknown")
    line = _RESOLUTION_NOTE.get(how, _RESOLUTION_NOTE["unknown"])
    signals = getattr(ctx, "domain_signals", None) or {}
    if not signals:
        return line
    evidence = "; ".join(
        f"{dom}: {len(sigs)} [{', '.join(sigs[:6])}{'...' if len(sigs) > 6 else ''}]"
        for dom, sigs in sorted(signals.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    )
    if how == "general-sink":
        #--- The loud case: the document DID carry catalog-domain signals, yet no
        #--- domain cleared the threshold/margin. The omission is now on the record.
        return (line + "\n               Content signals found but undecided — "
                + evidence)
    return line + "\n               Content signals — " + evidence


class ContextBuilder:
    """
    Builds a validated RuntimeContext from user input.
    Resolves domain, regime, roles, tools, and SSM personas automatically.
    """

    def build(self, case: dict) -> RuntimeContext:
        """
        Builds RuntimeContext from a case dict.
        Input:
            {
                "type": "contract",
                "subscenario": "alquiler_departamento",
                "objective": "identify risks",
                "regime": "adversarial"  # optional
            }
        """
        self._validate(case)

        doc_type = case.get("type", "general").lower()
        subscenario = case.get("subscenario", "")
        objective = case.get("objective", "identify risks and failure modes")
        regime_key = case.get("regime", "standard").lower()

        # Resolve domain
        #--- Stem resolution first. LW-1 contract, unchanged, certified.
        domain = self._resolve_domain(doc_type, subscenario)

        #--- LW-8 (v3.24.0) — the stem is weaker evidence than the document.
        #--- In `--document` mode the subscenario IS the filename, so a Legal
        #--- document named `mindmate_tos.txt` fell to the General sink and was
        #--- audited WITHOUT the LG08/LG09 auto-FATAL gates — silently, because
        #--- General declares no catalog and load_domain_catalog returns "" by
        #--- design for it. The content fallback fires ONLY on that sink: it can
        #--- never override a successful stem match, so every resolution that
        #--- worked in v3.23.0 is byte-identical here. Zero regression surface.
        if domain == "General":
            domain_resolution = "general-sink"
        elif DOMAIN_MAP.get(doc_type.lower()):
            domain_resolution = "declared-type"
        else:
            domain_resolution = "subscenario-keyword"

        domain_signals = case.get("domain_signal_evidence") or {}
        if domain == "General":
            hint = case.get("domain_hint")
            if hint:
                domain = hint
                domain_resolution = "document-content"

        # Resolve regime
        regime_data = REGIME_MAP.get(regime_key, DEFAULT_REGIME)

        # Get roles from catalog
        roles = ROLE_CATALOG.get(domain, ROLE_CATALOG["General"])
        rol_agents = roles.get("rol", [])
        forense_agents = roles.get("forense", [])

        # Get SSM personas
        ssm_personas = SSM_CATALOG.get(domain, SSM_CATALOG["General"])

        # Get tools
        tools = DOMAIN_TOOLS.get(domain, DOMAIN_TOOLS["General"])

        return RuntimeContext(
            type=doc_type,
            subscenario=subscenario,
            objective=objective,
            regime=regime_key,
            domain=domain,
            regime_description=regime_data["description"],
            rol_agents=rol_agents,
            forense_agents=forense_agents,
            ssm_personas=ssm_personas,
            tools=tools,
            run_ssm=case.get("run_ssm", False),
            ssm_scale=case.get("ssm_scale", "MESO"),
            corpus=JURISDICTION_CORPUS_MAP.get(domain),
            domain_resolution=domain_resolution,
            domain_signals=domain_signals,
            corpus_paths=case.get("corpus_paths"),
            signals_paths=case.get("signals_paths"),
        )

    def _resolve_domain(self, doc_type: str, subscenario: str) -> str:
        """
        Resolves domain from type (exact match) then subscenario (boundary-aware,
        most-specific-keyword wins, order-invariant).

        LW-1 fix — TWO defects closed:
        (1) substring bleed: the legacy resolver matched DOMAIN_MAP keys as raw
            substrings, so 2-3 char abbreviation keys ("ma", "ops", "hr", "sop")
            false-matched any stem merely containing those letters
            (e.g. "transformation" -> Financial via "ma", "threshold" -> HR).
        (2) order-dependence: the legacy resolver returned the FIRST substring
            match in DOMAIN_MAP insertion order, so routing for multi-domain
            stems was silently coupled to dict layout.

        Resolution contract (deterministic, order-invariant):
          - separators (_ - . spaces) are normalized so stems tokenize cleanly;
          - keys are evaluated MOST-SPECIFIC FIRST: longest keyword wins, with an
            alphabetical tie-break — independent of DOMAIN_MAP insertion order;
          - short abbreviation keys (<=3 chars) match ONLY as whole tokens;
          - compound / multi-word keys (e.g. "real_estate") match as a
            normalized phrase;
          - longer single-word keys match a whole token OR a token prefix, so
            "cyber" still resolves "cybersecurity".
        For genuinely ambiguous multi-domain stems, pin the domain via --type
        (exact-type fast path below). No key is removed.
        """
        # Check type first (exact match — unchanged fast path)
        domain = DOMAIN_MAP.get(doc_type.lower())
        if domain:
            return domain
        # Check subscenario keywords (boundary-aware, most-specific first)
        norm = _SEP.sub(" ", subscenario.lower()).strip()
        tokens = set(norm.split())
        for keyword in sorted(DOMAIN_MAP, key=lambda k: (-len(k), k)):
            mapped_domain = DOMAIN_MAP[keyword]
            kw = _SEP.sub(" ", keyword.lower()).strip()
            if len(kw.replace(" ", "")) <= 3:
                # short abbreviation: whole-token match only (no substring bleed)
                if kw in tokens:
                    return mapped_domain
            elif " " in kw:
                # compound / multi-word key: normalized phrase match
                if kw in norm:
                    return mapped_domain
            else:
                # long single-word key: whole token or token prefix (forgiving)
                if any(t == kw or t.startswith(kw) for t in tokens):
                    return mapped_domain
        return "General"

    def _validate(self, case: dict):
        """Validates required fields in case dict."""
        required = ["type", "subscenario", "objective"]
        missing = [f for f in required if not case.get(f)]
        if missing:
            raise ValueError(
                f"[CONTEXT_BUILDER] Missing required fields: {missing}\n"
                f"Required: type, subscenario, objective\n"
                f"Optional: regime (default: standard), run_ssm, ssm_scale"
            )

    def describe(self, ctx: RuntimeContext) -> str:
        """Human-readable summary of the built context."""
        return f"""
[RUNTIME CONTEXT]
  Domain:      {ctx.domain}  (resolved by: {ctx.domain_resolution})
  Type:        {ctx.type} / {ctx.subscenario}
  Objective:   {ctx.objective}
  Regime:      {ctx.regime} — {ctx.regime_description}
  Rol Agents:  {len(ctx.rol_agents)} ({', '.join(ctx.rol_agents[:2])}...)
  Forense:     {len(ctx.forense_agents)} ({', '.join(ctx.forense_agents[:2])}...)
  SSM Personas:{len(ctx.ssm_personas)}
  Tools:       {len(ctx.tools)} available
  Run SSM:     {ctx.run_ssm} ({ctx.ssm_scale})
"""
