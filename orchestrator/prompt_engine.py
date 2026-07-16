"""
Dark Strategist v3.24.0 — Prompt Engine
Master template + dynamic prompt builder.
Replaces 15 static .md files with one template + runtime injection.

v3.24.0 (GAP #1, decision (a) fix injection): Forense N1 prompts now inject
the domain's BINDING Failure Catalog (extracted via
domain_catalog.build_catalog_block, marker-scoped from prompts/*.md) after the
tools list. All 19 domain variants carry the markers; a domain with no catalog
(P01 General) gets "" -> template output is byte-identical to v3.23.0.

Rol N1 prompts deliberately do NOT receive the catalog: Agentes de Rol
simulate domain actors, their output contract has no severity field, and
priming them with the Forense taxonomy would break the blind-peer separation
between the two N1 layers and suppress ROL<->FORENSE clashes.
See domain_catalog.py for the full rationale and the marker convention.
"""

from schema import RuntimeContext
from domain_catalog import build_catalog_block


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
{domain_catalog_block}
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
3. DETECT and ANNOTATE conflicts — see CLASH RESOLUTION PROTOCOL below. NEVER silently pick a side.
4. COLLAPSE symptoms into root causes
5. APPLY the Verdict Decision Table deterministically
6. EMIT the VEREDICTO FORENSE UNIFICADO

CLASH RESOLUTION PROTOCOL (mandatory — no silent picks):
A finding-severity disagreement (same issue, different severity) resolves to HIGHEST
severity. This is severity escalation, NOT clash.
A clash is a factual contradiction between sources (e.g. a Rol agent claims an actor
would ACCEPT a clause while a Forense agent claims they would REJECT it). For every
clash you MUST emit a structured record in conflicts_detected with this exact shape:
  "CLASH: <what contradicts> | ROL says: <claim> | FORENSE says: <claim> | PRECEDENCE: <FORENSE|ROL|UNRESOLVED> | REASON: <why>"
Source precedence default: FORENSE over ROL (the Forense layer audits the simulation,
so its factual claims override the simulated environment) UNLESS the Rol agent cites
domain ground-truth the Forense lacks — then mark UNRESOLVED and surface it. An
UNRESOLVED clash on a FATAL-adjacent issue lowers confidence to LOW.

VERDICT DECISION TABLE:
≥1 🔴 FATAL → INVIABLE
0F + ≥1 🟠 SERIOUS → VIABLE WITH CRITICAL CORRECTIONS
0F + 0S + ≥1 🟡 MODERATE → VIABLE WITH ADJUSTMENTS
Only 🔵 LATENT → SOLID UNDER PRESSURE

TRIBUNAL REPORTS:
{tribunal_reports}

OUTPUT FORMAT (JSON):
Every element of fatal_findings, serious_findings, moderate_findings, and latent_findings
MUST be a complete finding object with ALL of these fields: severity, title, description,
evidence, root_cause, escalation_note. Do NOT abbreviate MODERATE or LATENT findings, and do
NOT merge findings into multi_agent_confirmed (that field is a list of plain strings).
{{
  "session_id": "{session_id}",
  "domain": "{domain}",
  "subscenario": "{subscenario}",
  "regime": "{regime}",
  "tribunal_mode": "{tribunal_mode}",
  "agents_consulted": {agent_count},
  "fatal_findings": [
    {{
      "severity": "FATAL",
      "title": "Short finding title",
      "description": "What is wrong and why",
      "evidence": "Specific document reference or absence",
      "root_cause": "Underlying structural cause",
      "escalation_note": null
    }}
  ],
  "serious_findings": [
    {{
      "severity": "SERIOUS",
      "title": "Short finding title",
      "description": "What is wrong and why",
      "evidence": "Specific document reference or absence",
      "root_cause": "Underlying structural cause",
      "escalation_note": null
    }}
  ],
  "moderate_findings": [
    {{
      "severity": "MODERATE",
      "title": "Short finding title",
      "description": "What is wrong and why",
      "evidence": "Specific document reference or absence",
      "root_cause": "Underlying structural cause",
      "escalation_note": null
    }}
  ],
  "latent_findings": [
    {{
      "severity": "LATENT",
      "title": "Short finding title",
      "description": "What is wrong and why",
      "evidence": "Specific document reference or absence",
      "root_cause": "Underlying structural cause",
      "escalation_note": null
    }}
  ],
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
    No static .md files required for the base structure — all generated at
    runtime. v3.24.0: domain-specific Failure Catalog content IS read from
    prompts/*.md (marker-scoped, see domain_catalog.py) and injected into the
    Forense N1 prompts only — this is the GAP #1 fix, additive only.
    """

    def __init__(self, prompts_dir: str = "./prompts"):
        self.prompts_dir = prompts_dir

    def _domain_catalog_block(self, domain: str) -> str:
        block = build_catalog_block(domain, self.prompts_dir)
        # Trailing blank line when non-empty keeps template spacing clean;
        # "" when empty so catalog-less domains (P01 General) stay byte-identical.
        return (block + "\n") if block else ""

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
                             rol_simulation: str = "",
                             handoff_window: int = 8000) -> str:
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
            domain_catalog_block=self._domain_catalog_block(ctx.domain),
        )

        if rol_simulation:
            prompt += f"\n\nROL AGENT SIMULATION TO AUDIT:\n{rol_simulation[:handoff_window]}"

        return prompt

    def build_synthesis_prompt(self, ctx: RuntimeContext,
                               all_reports: list,
                               tribunal_mode: str,
                               session_id: str,
                               synthesis_window: int = 1500) -> str:
        """Builds prompt for AFO synthesis call."""
        reports_text = ""
        for i, r in enumerate(all_reports, 1):
            agent_id = r.get("agent_id", f"AGENT-{i}")
            agent_type = r.get("agent_type", "UNKNOWN")
            reports_text += f"\n{'='*50}\n{agent_id} ({agent_type}):\n"

            # Structured handoff: feed parsed findings with provenance, not raw prose
            # (telephone-game fix, v3.4 R1 FUGA#3). Falls back to governed raw clip
            # only when an agent produced no parseable findings.
            findings = r.get("findings", [])
            if isinstance(findings, list) and findings:
                reports_text += f"  preliminary_verdict: {r.get('preliminary_verdict', 'N/A')}\n"
                for f in findings:
                    if not isinstance(f, dict):
                        continue
                    reports_text += (
                        f"  - [{f.get('severity', '?')}] {f.get('title', '')}\n"
                        f"      desc: {f.get('description', '')}\n"
                        f"      evidence: {f.get('evidence', '')}\n"
                        f"      root_cause: {f.get('root_cause', '')}\n"
                    )
                for risk in r.get("key_risks", []):
                    reports_text += f"  key_risk: {risk}\n"
                for omission in r.get("omissions_detected", []):
                    reports_text += f"  omission: {omission}\n"
            else:
                report_content = r.get("raw_output", str(r))[:synthesis_window]
                reports_text += f"{report_content}\n"

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
