"""
Dark Strategist v3.0.0 — Context Builder
Builds and validates the RuntimeContext object for each case.
Replaces manual flag passing with a structured, validated context.
"""

from catalogs import ROLE_CATALOG, SSM_CATALOG, DOMAIN_MAP, REGIME_MAP, DEFAULT_REGIME
from schema import RuntimeContext


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
        )

    def _resolve_domain(self, doc_type: str, subscenario: str) -> str:
        """Resolves domain from type and subscenario."""
        # Check type first
        domain = DOMAIN_MAP.get(doc_type.lower())
        if domain:
            return domain
        # Check subscenario keywords
        subscenario_lower = subscenario.lower()
        for keyword, mapped_domain in DOMAIN_MAP.items():
            if keyword in subscenario_lower:
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
