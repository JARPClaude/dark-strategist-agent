"""
Dark Strategist — Verdict Synthesizer
Consolidates N1 Agente Forense reports into a unified final verdict.
Version: 2.8.0

The Synthesizer is the final act of the AFO:
  - Receives all N1 reports (and their N2 sub-agent findings)
  - Identifies conflicts and agreements between agents
  - Applies the deterministic Verdict Decision Table
  - Emits the unified VEREDICTO FORENSE UNIFICADO
"""

from pathlib import Path
from datetime import datetime
import anthropic


SYNTHESIZER_SYSTEM_PROMPT = """You are the DARK STRATEGIST — AGENTE FORENSE ORQUESTADOR (AFO).
You have received independent forensic reports from multiple Agentes Forenses who audited the same document in parallel, blind to each other.

Your role is to:
1. CONSOLIDATE all findings — identify which findings appear across multiple agents (HIGH CONFIDENCE) vs. only one agent (SINGLE SOURCE)
2. RESOLVE CONFLICTS — when agents disagree, apply the most conservative interpretation (highest severity wins)
3. DEDUPLICATE — collapse symptom-level findings into root causes
4. APPLY the Verdict Decision Table deterministically
5. EMIT the VEREDICTO FORENSE UNIFICADO

Verdict Decision Table (non-negotiable):
- ≥1 🔴 FATAL (unresolved) → 🔴 INVIABLE
- 0 FATALs + ≥1 🟠 SERIOUS → 🟠 VIABLE WITH CRITICAL CORRECTIONS
- 0 FATALs + 0 SERIOUS + ≥1 🟡 MODERATE → 🟡 VIABLE WITH ADJUSTMENTS
- Only 🔵 LATENTs → 🟢 SOLID UNDER PRESSURE

Output format:
[AFO SYNTHESIS REPORT]
[SESSION_ID: {id}]
[TRIBUNAL_MODE: {mode}]
[AGENTS_CONSULTED: N]

CONSOLIDATED FINDINGS:
  [List findings with confidence: MULTI-AGENT | SINGLE-SOURCE]

CONFLICTS RESOLVED:
  [List any disagreements between agents and resolution]

VEREDICTO FORENSE UNIFICADO:
  [Final verdict with full reasoning]

[PROTOCOL_STATUS: SYNTHESIS_COMPLETE]"""


class VerdictSynthesizer:
    """
    Synthesizes multiple N1 Agente Forense reports into a unified verdict.
    """

    def __init__(self, config: dict, prompts_dir: str):
        self.config = config
        self.prompts_dir = Path(prompts_dir)
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])

    def synthesize(self, document: str, n1_reports: list,
                   routing: dict, tribunal_label: str,
                   session_id: str) -> str:
        """
        Synthesizes all N1 reports into the final unified verdict.
        """
        if len(n1_reports) == 1:
            # Single mode — no synthesis needed, return directly
            return self._format_single_verdict(
                n1_reports[0]["report"], routing, tribunal_label, session_id
            )

        # Build synthesis prompt with all N1 reports
        synthesis_input = self._build_synthesis_input(
            document, n1_reports, routing, tribunal_label, session_id
        )

        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=self.config["anthropic"]["max_tokens"],
            system=SYNTHESIZER_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": synthesis_input}]
        )

        return response.content[0].text

    def _build_synthesis_input(self, document: str, n1_reports: list,
                               routing: dict, tribunal_label: str,
                               session_id: str) -> str:
        """Builds the input for the synthesis call."""
        reports_text = ""
        for i, report_data in enumerate(n1_reports, 1):
            agent_id = report_data.get("agent_id", f"AF-{str(i).zfill(2)}")
            prompt = report_data.get("prompt", "unknown")
            report = report_data.get("report", "[NO REPORT]")
            sub_agents = report_data.get("sub_agents_used", [])

            reports_text += f"""
{'='*60}
AGENTE FORENSE: {agent_id}
PROMPT USED: {prompt}
SUB-AGENTS DEPLOYED: {len(sub_agents)}
{'='*60}
{report}
"""
            # Include N2 sub-agent reports
            for sub in sub_agents:
                reports_text += f"""
  --- {sub.get('unit', 'UNKNOWN')} ({sub.get('type', '')}) ---
  {sub.get('report', '[NO SUB-AGENT REPORT]')[:1000]}
"""

        return f"""SESSION_ID: {session_id}
TRIBUNAL_MODE: {tribunal_label}
DOMAIN: {routing.get('domain', 'Unknown')}
AGENTS_CONSULTED: {len(n1_reports)}
TIMESTAMP: {datetime.utcnow().isoformat()}

ORIGINAL DOCUMENT (excerpt):
{document[:2000]}

INDEPENDENT FORENSIC REPORTS FROM TRIBUNAL:
{reports_text}

Synthesize all reports above into the VEREDICTO FORENSE UNIFICADO.
Apply the Verdict Decision Table. Conflicts resolve toward highest severity."""

    def _format_single_verdict(self, report: str, routing: dict,
                               tribunal_label: str, session_id: str) -> str:
        """Formats a single-agent verdict with AFO header."""
        return f"""[AFO SYNTHESIS REPORT]
[SESSION_ID: {session_id}]
[TRIBUNAL_MODE: {tribunal_label}]
[AGENTS_CONSULTED: 1]
[DOMAIN: {routing.get('domain', 'Unknown')}]

{report}

[PROTOCOL_STATUS: SINGLE_MODE_COMPLETE]"""
