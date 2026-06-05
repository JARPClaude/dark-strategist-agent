"""
Dark Strategist v3.0.0 — Schema
Pydantic models for structured agent output.
Replaces free-text parsing with validated, comparable verdicts.
"""

from pydantic import BaseModel, Field
from typing import Optional


class Finding(BaseModel):
    """A single forensic finding from any agent."""
    severity: str = Field(description="FATAL | SERIOUS | MODERATE | LATENT")
    title: str = Field(description="Short title of the finding")
    description: str = Field(description="What is wrong and why")
    evidence: str = Field(description="Specific reference to document content or absence")
    root_cause: str = Field(description="Underlying structural cause — not symptom")
    escalation_note: Optional[str] = Field(
        default=None,
        description="If severity escalated via Rule 09 — explain why"
    )


class AgentVerdictOutput(BaseModel):
    """
    Structured output from any N1 Agente Forense or N2 Sub-agente.
    Enables programmatic comparison across tribunal agents.
    """
    agent_id: str = Field(description="Agent identifier e.g. AF-01, UNIT-QUANT")
    agent_type: str = Field(description="ROL | FORENSE | SUB_AGENT_PERMANENT | SUB_AGENT_TEMPORARY")
    domain: str = Field(description="Detected domain")
    subscenario: str = Field(description="Specific subscenario e.g. XAUUSD, alquiler_departamento")
    regime: str = Field(description="Analysis regime: standard | adversarial | breakout | crisis")

    findings: list[Finding] = Field(
        default_factory=list,
        description="All findings ordered by severity: FATAL first"
    )

    preliminary_verdict: str = Field(
        description="INVIABLE | VIABLE WITH CRITICAL CORRECTIONS | VIABLE WITH ADJUSTMENTS | SOLID UNDER PRESSURE"
    )
    confidence: str = Field(description="HIGH | MODERATE | LOW")
    key_risks: list[str] = Field(default_factory=list, description="Top 3-5 risks in plain language")
    omissions_detected: list[str] = Field(
        default_factory=list,
        description="Elements expected but absent from the document"
    )
    recommendation: str = Field(description="Primary action recommendation in one sentence")

    # Tribunal Transversal metadata
    simulation_quality: Optional[str] = Field(
        default=None,
        description="For FORENSE agents only: quality assessment of ROL simulation they audited"
    )
    inconsistencies_with_peers: list[str] = Field(
        default_factory=list,
        description="Findings that contradict other agents in the tribunal"
    )

    @property
    def fatal_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "FATAL")

    @property
    def serious_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "SERIOUS")

    @property
    def moderate_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "MODERATE")

    @property
    def latent_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "LATENT")


class UnifiedVerdictOutput(BaseModel):
    """
    Final unified verdict produced by the AFO Verdict Synthesizer.
    Consolidates all N1 agent outputs.
    """
    session_id: str
    domain: str
    subscenario: str
    regime: str
    tribunal_mode: str
    agents_consulted: int

    # Consolidated findings
    fatal_findings: list[Finding] = Field(default_factory=list)
    serious_findings: list[Finding] = Field(default_factory=list)
    moderate_findings: list[Finding] = Field(default_factory=list)
    latent_findings: list[Finding] = Field(default_factory=list)

    # Conflict analysis
    conflicts_detected: list[str] = Field(
        default_factory=list,
        description=(
            "Structured clash records (factual contradictions between Rol/Forense). "
            "Format: 'CLASH: <what> | ROL says: <x> | FORENSE says: <y> | "
            "PRECEDENCE: <FORENSE|ROL|UNRESOLVED> | REASON: <why>'. "
            "Severity disagreements are escalated, not recorded here."
        )
    )
    multi_agent_confirmed: list[str] = Field(
        default_factory=list,
        description="Findings confirmed by 2+ independent agents — HIGH confidence"
    )

    # Final verdict
    final_verdict: str = Field(
        description="INVIABLE | VIABLE WITH CRITICAL CORRECTIONS | VIABLE WITH ADJUSTMENTS | SOLID UNDER PRESSURE"
    )
    confidence: str = Field(description="HIGH | MODERATE | LOW")
    verdict_reasoning: str = Field(description="Why this verdict — 2-3 sentences max")

    # SSM metadata (if activated)
    ssm_activated: bool = False
    ssm_social_verdict: Optional[str] = None
    ssm_adoption_projection: Optional[int] = None
    ssm_dominant_coalition: Optional[str] = None

    @property
    def severity_summary(self) -> dict:
        return {
            "FATAL": len(self.fatal_findings),
            "SERIOUS": len(self.serious_findings),
            "MODERATE": len(self.moderate_findings),
            "LATENT": len(self.latent_findings),
        }


def compute_confidence(
    agents_consulted: int,
    driver_corroborated: bool,
    driver_finding_count: int,
    unresolved_conflicts: int,
) -> str:
    """
    Deterministic, auditable confidence for a unified verdict (v3.11.0).

    NON-BINDING: this NEVER alters final_verdict (which stays severity-driven:
    >=1 FATAL -> INVIABLE). It only reports how corroborated/contested the verdict
    is. It is an auditability signal, NOT a probability of real-world success and
    NOT an efficiency guarantee.

    Rule:
      LOW   if  <2 agents, OR the verdict hinges on a single uncorroborated
            finding, OR >=2 unresolved clashes.
      HIGH  if  >=3 agents AND 0 unresolved clashes AND the verdict-driving tier
            is empty (clean) or multi-agent-confirmed.
      MODERATE otherwise.
    """
    n = agents_consulted
    if n < 2:
        return "LOW"
    if unresolved_conflicts >= 2:
        return "LOW"
    if driver_finding_count == 1 and not driver_corroborated:
        return "LOW"
    if n >= 3 and unresolved_conflicts == 0 and (driver_finding_count == 0 or driver_corroborated):
        return "HIGH"
    return "MODERATE"


def should_escalate(confidence, rounds_done, max_rounds, remaining_agents, enabled=True):
    """
    Deterministic gate for the confidence-driven escalation round (v3.12.0).

    Escalate iff: enabled AND confidence is LOW AND the round cap is not reached AND
    there is remaining agent budget. NON-BINDING w.r.t. final_verdict — escalation only
    decides whether to spend more deliberation; the verdict stays severity-driven
    (>=1 FATAL -> INVIABLE). Confidence may remain LOW after escalating (honest).
    """
    return bool(
        enabled
        and confidence == "LOW"
        and rounds_done < max_rounds
        and remaining_agents > 0
    )


class RuntimeContext(BaseModel):
    """
    Runtime context object built by ContextBuilder.
    Injected into prompt templates before LLM call.
    """
    # Case classification
    type: str = Field(description="chart | contract | finance | code | medical | etc.")
    subscenario: str = Field(description="Specific subscenario within the type")
    objective: str = Field(description="What the analysis should determine")
    regime: str = Field(default="standard", description="Analysis regime")

    # Auto-resolved by ContextBuilder
    domain: str = Field(default="General")
    regime_description: str = Field(default="Standard analysis — balanced perspective")

    # Active roles (from ROLE_CATALOG)
    rol_agents: list[str] = Field(default_factory=list)
    forense_agents: list[str] = Field(default_factory=list)
    ssm_personas: list[str] = Field(default_factory=list)

    # Tools available for this domain
    tools: list[str] = Field(default_factory=list)

    # Tribunal configuration
    tribunal_size: int = Field(default=1)
    tribunal_label: str = Field(default="SINGLE")

    # SSM configuration
    run_ssm: bool = False
    ssm_scale: str = Field(default="MESO")

    # Jurisdictional corpus selector (v3.8.0) — resolved by ContextBuilder; None = no corpus
    corpus: str | None = Field(default=None)
    # BYO per-case reference corpus (v3.10.0) — operator-supplied file paths; None = no BYO
    corpus_paths: list[str] | None = Field(default=None)
