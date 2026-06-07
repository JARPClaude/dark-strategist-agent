"""
Dark Strategist v3.0.0 — Context Builder
Builds and validates the RuntimeContext object for each case.
Replaces manual flag passing with a structured, validated context.
"""

import re

from catalogs import ROLE_CATALOG, SSM_CATALOG, DOMAIN_MAP, REGIME_MAP, DEFAULT_REGIME, JURISDICTION_CORPUS_MAP
from schema import RuntimeContext


# Separator normalizer for boundary-aware domain resolution (LW-1 fix).
_SEP = re.compile(r'[^a-z0-9]+')


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
        domain = self._resolve_domain(doc_type, subscenario)

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
  Domain:      {ctx.domain}
  Type:        {ctx.type} / {ctx.subscenario}
  Objective:   {ctx.objective}
  Regime:      {ctx.regime} — {ctx.regime_description}
  Rol Agents:  {len(ctx.rol_agents)} ({', '.join(ctx.rol_agents[:2])}...)
  Forense:     {len(ctx.forense_agents)} ({', '.join(ctx.forense_agents[:2])}...)
  SSM Personas:{len(ctx.ssm_personas)}
  Tools:       {len(ctx.tools)} available
  Run SSM:     {ctx.run_ssm} ({ctx.ssm_scale})
"""
