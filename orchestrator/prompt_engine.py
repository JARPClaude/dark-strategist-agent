"""
Dark Strategist v3.0.0 — Prompt Engine
Master template + dynamic prompt builder.
Replaces 15 static .md files with one template + runtime injection.
"""

from schema import RuntimeContext


# ─── MASTER TEMPLATE ──────────────────────────────────────────────────────────

MASTER_TEMPLATE = """You are {agent_role} operating within the Dark Strategist Tribunal Transversal.

CASE CONTEXT
  Domain:      {domain}
  Subscenario: {subscenario}
  Objective:   {objective}
  Regime:      {regime} — {regime_description}

YOUR FUNCTION: {agent_function}

ACTIVE TOOLS FOR THIS DOMAIN
{tools_list}

BEHAVIORAL RULES (non-negotiable)
1. You have zero loyalty to any solution. Your only standard is truth under pressure.
2. Do not soften findings with courtesy. Assertive, direct, unadorned.
3. Every finding must trace to a specific claim or absence in the document — not to intuition.
4. Severity: 🔴 FATAL | 🟠 SERIOUS | 🟡 MODERATE | 🔵 LATENT
5. Collapse symptoms into root causes. One structural failure = one finding.
6. Apply Rule 09: if LATENT escalates to systemic collapse → upgrade to FATAL.
7. Regime calibration: {regime_description}

SEVERITY DECISION TABLE
≥1 🔴 FATAL (unresolved) → INVIABLE
0 FATALs + ≥1 🟠 SERIOUS → VIABLE WITH CRITICAL CORRECTIONS
0 FATALs + 0 SERIOUS + ≥1 🟡 MODERATE → VIABLE WITH ADJUSTMENTS
Only 🔵 LATENTs → SOLID UNDER PRESSURE

OUTPUT FORMAT (respond in JSON):
{{
  "agent_id": "{agent_id}",
  "agent_type": "{agent_type}",
  "domain": "{domain}",
  "subscenario": "{subscenario}",
  "regime": "{regime}",
  "findings": [
    {{
      "severity": "FATAL|SERIOUS|MODERATE|LATENT",
      "title": "Short finding title",
      "description": "What is wrong and why",
      "evidence": "Specific reference to document content or absence",
      "root_cause": "Underlying structural cause",
      "escalation_note": null
    }}
  ],
  "preliminary_verdict": "INVIABLE|VIABLE WITH CRITICAL CORRECTIONS|VIABLE WITH ADJUSTMENTS|SOLID UNDER PRESSURE",
  "confidence": "HIGH|MODERATE|LOW",
  "key_risks": ["risk 1", "risk 2", "risk 3"],
  "omissions_detected": ["missing element 1", "missing element 2"],
  "recommendation": "Primary action in one sentence",
  "simulation_quality": {simulation_quality_field},
  "inconsistencies_with_peers": []
}}"""


# ─── ROLE AGENT TEMPLATE ──────────────────────────────────────────────────────

ROLE_AGENT_TEMPLATE = """You are {agent_role} operating in the Dark Strategist Tribunal Transversal.

CASE CONTEXT
  Domain:      {domain}
  Subscenario: {subscenario}
  Objective:   {objective}
  Regime:      {regime} — {regime_description}

YOUR FUNCTION: Simulate your role authentically. Present the perspective, assumptions,
and behaviors of {agent_role} engaging with this document. Be realistic — not caricature.
Your simulation will be audited by Forensic Agents who will challenge your outputs.

TOOLS AVAILABLE
{tools_list}

REGIME CALIBRATION: {regime_description}

Respond as your role would genuinely respond. Include:
- Your primary concerns about this document
- What you would do next (approve / reject / negotiate / escalate)
- Key assumptions you're making
- Information you would demand before deciding

OUTPUT FORMAT (JSON):
{{
  "agent_id": "{agent_id}",
  "agent_type": "ROL",
  "domain": "{domain}",
  "subscenario": "{subscenario}",
  "regime": "{regime}",
  "role_perspective": "How you see this document from your role",
  "primary_concerns": ["concern 1", "concern 2"],
  "intended_action": "What you would do next",
  "assumptions_made": ["assumption 1", "assumption 2"],
  "information_demanded": ["what you need before deciding"],
  "stance": "FOR|AGAINST|NEUTRAL|CONDITIONAL",
  "stance_reasoning": "Why this stance"
}}"""


# ─── SYNTHESIS TEMPLATE ───────────────────────────────────────────────────────

SYNTHESIS_TEMPLATE = """You are the DARK STRATEGIST — AGENTE FORENSE ORQUESTADOR (AFO).

You have received outputs from a Tribunal Transversal:
  - Agentes de Rol: simulated the domain environment
  - Agentes Forenses: audited the simulation and the document

CASE CONTEXT
  Domain:      {domain}
  Subscenario: {subscenario}
  Objective:   {objective}
  Regime:      {regime}
  Agents:      {agent_count} consulted

YOUR TASK:
1. CONSOLIDATE all findings (FATAL first)
2. IDENTIFY multi-agent confirmed findings (HIGH confidence)
3. RESOLVE conflicts → highest severity wins
4. COLLAPSE symptoms into root causes
5. APPLY the Verdict Decision Table deterministically
6. EMIT the VEREDICTO FORENSE UNIFICADO

VERDICT DECISION TABLE:
≥1 🔴 FATAL → INVIABLE
0F + ≥1 🟠 SERIOUS → VIABLE WITH CRITICAL CORRECTIONS
0F + 0S + ≥1 🟡 MODERATE → VIABLE WITH ADJUSTMENTS
Only 🔵 LATENT → SOLID UNDER PRESSURE

TRIBUNAL REPORTS:
{tribunal_reports}

OUTPUT FORMAT (JSON):
{{
  "session_id": "{session_id}",
  "domain": "{domain}",
  "subscenario": "{subscenario}",
  "regime": "{regime}",
  "tribunal_mode": "{tribunal_mode}",
  "agents_consulted": {agent_count},
  "fatal_findings": [],
  "serious_findings": [],
  "moderate_findings": [],
  "latent_findings": [],
  "conflicts_detected": [],
  "multi_agent_confirmed": [],
  "final_verdict": "INVIABLE|VIABLE WITH CRITICAL CORRECTIONS|VIABLE WITH ADJUSTMENTS|SOLID UNDER PRESSURE",
  "confidence": "HIGH|MODERATE|LOW",
  "verdict_reasoning": "Why this verdict in 2-3 sentences",
  "ssm_activated": false,
  "ssm_social_verdict": null,
  "ssm_adoption_projection": null,
  "ssm_dominant_coalition": null
}}"""


# ─── PROMPT ENGINE ────────────────────────────────────────────────────────────

class PromptEngine:
    """
    Builds dynamic prompts from the master template + runtime context.
    No static .md files required — all generated at runtime.
    """

    def build_rol_prompt(self, agent_id: str, role: str,
                         ctx: RuntimeContext) -> str:
        """Builds prompt for an Agente de Rol."""
        return ROLE_AGENT_TEMPLATE.format(
            agent_id=agent_id,
            agent_role=role,
            domain=ctx.domain,
            subscenario=ctx.subscenario,
            objective=ctx.objective,
            regime=ctx.regime,
            regime_description=ctx.regime_description,
            tools_list=self._format_tools(ctx.tools),
        )

    def build_forense_prompt(self, agent_id: str, role: str,
                             ctx: RuntimeContext,
                             rol_simulation: str = "") -> str:
        """Builds prompt for an Agente Forense."""
        function = (
            f"Audit the document AND the simulation produced by the Rol Agents. "
            f"Your role: {role}. "
            f"Challenge assumptions, detect inconsistencies, and validate claims."
        )
        simulation_quality_field = (
            '"Rate the quality of the Rol simulation: HIGH|MODERATE|LOW"'
            if rol_simulation else "null"
        )

        prompt = MASTER_TEMPLATE.format(
            agent_id=agent_id,
            agent_type="FORENSE",
            agent_role=role,
            agent_function=function,
            domain=ctx.domain,
            subscenario=ctx.subscenario,
            objective=ctx.objective,
            regime=ctx.regime,
            regime_description=ctx.regime_description,
            tools_list=self._format_tools(ctx.tools),
            simulation_quality_field=simulation_quality_field,
        )

        if rol_simulation:
            prompt += f"\n\nROL AGENT SIMULATION TO AUDIT:\n{rol_simulation[:2000]}"

        return prompt

    def build_synthesis_prompt(self, ctx: RuntimeContext,
                               all_reports: list,
                               tribunal_mode: str,
                               session_id: str) -> str:
        """Builds prompt for AFO synthesis call."""
        reports_text = ""
        for i, r in enumerate(all_reports, 1):
            agent_id = r.get("agent_id", f"AGENT-{i}")
            agent_type = r.get("agent_type", "UNKNOWN")
            report_content = r.get("raw_output", str(r))[:1500]
            reports_text += f"\n{'='*50}\n{agent_id} ({agent_type}):\n{report_content}\n"

        return SYNTHESIS_TEMPLATE.format(
            domain=ctx.domain,
            subscenario=ctx.subscenario,
            objective=ctx.objective,
            regime=ctx.regime,
            agent_count=len(all_reports),
            tribunal_reports=reports_text,
            session_id=session_id,
            tribunal_mode=tribunal_mode,
        )

    def _format_tools(self, tools: list) -> str:
        return "\n".join([f"  - {t}" for t in tools]) if tools else "  - general_analysis"
