"""
Dark Strategist — Sub-Agent Spawner
Manages N2 sub-agents (permanent UNITs and temporary).
Temporary sub-agents trigger SUB_AGENT_EXPANSION_RECOMMENDED notification.
Version: 2.8.0

N2 hierarchy:
  Permanent  → UNITs from existing catalog (UNIT-QUANT, UNIT-TECH, etc.)
  Temporary  → Created dynamically for unknown specialized needs
               → Notifies owner via Slack + GitHub + Sheets
"""

import json
import re
from datetime import datetime
from pathlib import Path

import anthropic

from notifier import SlackNotifier, GitHubNotifier


# ─── PERMANENT SUB-AGENT CATALOG (N2) ────────────────────────────────────────

PERMANENT_SUBAGENTS = {
    "UNIT-QUANT": {
        "trigger_signals": ["sharpe", "drawdown", "overfitting", "dcf", "irr", "npv",
                            "ebitda", "p-value", "statistical", "quantitative"],
        "system_prompt": """You are UNIT-QUANT — Quantitative Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: statistical validity, financial model integrity, quantitative risk.
Be concise. Report only findings relevant to your fragment.
Format: [UNIT-QUANT REPORT] followed by findings."""
    },
    "UNIT-INQUISITOR": {
        "trigger_signals": ["contract", "clause", "jurisdiction", "regulatory", "compliance",
                            "liability", "legal", "statute", "regulation", "gdpr"],
        "system_prompt": """You are UNIT-INQUISITOR — Legal Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: legal validity, regulatory compliance, liability exposure.
Apply hostile interpretation standard to every clause.
Format: [UNIT-INQUISITOR REPORT] followed by findings."""
    },
    "UNIT-TECH": {
        "trigger_signals": ["api", "architecture", "database", "security", "vulnerability",
                            "abap", "java", "python", "code", "system", "infrastructure"],
        "system_prompt": """You are UNIT-TECH — Technical Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: technical validity, security, scalability, implementation feasibility.
Format: [UNIT-TECH REPORT] followed by findings."""
    },
    "UNIT-PSYCH": {
        "trigger_signals": ["assumption", "bias", "optimism", "projection", "forecast",
                            "expect", "believe", "confident", "certain", "guarantee"],
        "system_prompt": """You are UNIT-PSYCH — Behavioral Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: cognitive bias, overconfidence, confirmation bias, groupthink signals.
Format: [UNIT-PSYCH REPORT] followed by findings."""
    },
    "UNIT-GEO": {
        "trigger_signals": ["country", "region", "geopolitical", "currency", "exchange",
                            "jurisdiction", "international", "cross-border", "spectrum"],
        "system_prompt": """You are UNIT-GEO — Geopolitical Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: geopolitical risk, regulatory instability, FX exposure, country risk.
Format: [UNIT-GEO REPORT] followed by findings."""
    },
    "UNIT-MARKET": {
        "trigger_signals": ["market", "competition", "cac", "ltv", "churn", "demand",
                            "customer", "revenue", "sales", "pricing", "marketplace"],
        "system_prompt": """You are UNIT-MARKET — Commercial Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: market assumptions, competitive dynamics, unit economics validity.
Format: [UNIT-MARKET REPORT] followed by findings."""
    },
    "UNIT-COMPLIANCE": {
        "trigger_signals": ["control", "audit", "governance", "policy", "procedure",
                            "sod", "segregation", "procurement", "budget", "public"],
        "system_prompt": """You are UNIT-COMPLIANCE — Governance Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: SoD violations, control gaps, audit trail, policy enforceability.
Format: [UNIT-COMPLIANCE REPORT] followed by findings."""
    },
    "UNIT-BIO": {
        "trigger_signals": ["biosecurity", "biomass", "livestock", "crop", "harvest",
                            "agricultural", "aquaculture", "climate", "cold chain"],
        "system_prompt": """You are UNIT-BIO — Field Forensic Sub-Agent.
Analyze ONLY the specific fragment delegated to you.
Focus: biological viability, biosecurity, climate risk, production assumptions.
Format: [UNIT-BIO REPORT] followed by findings."""
    },
}


# ─── SUB-AGENT SPAWNER ────────────────────────────────────────────────────────

class SubAgentSpawner:
    """
    Evaluates N1 reports and spawns N2 sub-agents when specialized analysis needed.
    Permanent sub-agents: from PERMANENT_SUBAGENTS catalog.
    Temporary sub-agents: created dynamically → triggers owner notification.
    """

    def __init__(self, config: dict, prompts_dir: str):
        self.config = config
        self.prompts_dir = Path(prompts_dir)
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.max_n2_per_n1 = config.get("tribunal", {}).get("max_n2_per_n1", 3)

    def evaluate_and_spawn(self, agent_id: str, report: str,
                           document: str, routing: dict) -> list:
        """
        Evaluates an N1 report for sub-agent needs.
        Returns list of sub-agent results used.
        """
        sub_agents_used = []

        # Check if N1 explicitly requested a sub-agent
        requested = self._detect_subagent_requests(report)

        # Auto-detect based on content signals
        auto_detected = self._auto_detect_units(document, report)

        # Combine, deduplicate, respect max limit
        needed = list(dict.fromkeys(requested + auto_detected))[:self.max_n2_per_n1]

        for unit_name in needed:
            if unit_name in PERMANENT_SUBAGENTS:
                result = self._spawn_permanent(agent_id, unit_name, document, report)
            else:
                result = self._spawn_temporary(agent_id, unit_name, document, report, routing)

            if result:
                sub_agents_used.append(result)

        return sub_agents_used

    def _detect_subagent_requests(self, report: str) -> list:
        """Detects explicit UNIT requests in N1 report."""
        units = []
        for unit in PERMANENT_SUBAGENTS.keys():
            if unit in report.upper():
                units.append(unit)
        return units

    def _auto_detect_units(self, document: str, report: str) -> list:
        """Auto-detects needed units based on signal words."""
        content = (document + " " + report).lower()
        detected = []
        for unit_name, unit_data in PERMANENT_SUBAGENTS.items():
            signals = unit_data["trigger_signals"]
            matches = sum(1 for s in signals if s in content)
            if matches >= 3:
                detected.append((unit_name, matches))
        detected.sort(key=lambda x: -x[1])
        return [u[0] for u in detected[:2]]

    def _spawn_permanent(self, parent_id: str, unit_name: str,
                         document: str, parent_report: str) -> dict:
        """Spawns a permanent N2 sub-agent from the catalog."""
        unit_data = PERMANENT_SUBAGENTS[unit_name]
        print(f"  [SPAWNER] {parent_id} → spawning {unit_name} (permanent)")

        try:
            response = self.client.messages.create(
                model=self.config["anthropic"]["model"],
                max_tokens=2048,
                system=unit_data["system_prompt"],
                messages=[{
                    "role": "user",
                    "content": (
                        f"Fragment from parent agent {parent_id} requiring your analysis:\n\n"
                        f"PARENT FINDINGS SUMMARY:\n{parent_report[:1000]}\n\n"
                        f"ORIGINAL DOCUMENT EXCERPT:\n{document[:3000]}\n\n"
                        f"Provide your specialized forensic analysis."
                    )
                }]
            )
            return {
                "unit": unit_name,
                "type": "PERMANENT",
                "parent": parent_id,
                "report": response.content[0].text,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            print(f"  [SPAWNER] {unit_name} failed: {e}")
            return None

    def _spawn_temporary(self, parent_id: str, domain: str,
                         document: str, parent_report: str, routing: dict) -> dict:
        """
        Spawns a temporary N2 sub-agent for an unknown specialized need.
        Triggers SUB_AGENT_EXPANSION_RECOMMENDED notification to owner.
        """
        print(f"  [SPAWNER] {parent_id} → spawning TEMPORARY sub-agent for: {domain}")

        temp_system = f"""You are a TEMPORARY Forensic Sub-Agent specialized in: {domain}.
This is a one-time analysis. Analyze the fragment provided.
Focus on risks, gaps, and failure modes specific to: {domain}.
Format: [TEMP-{domain.upper()} REPORT] followed by findings.
Be thorough — this report will be reviewed to create a permanent sub-agent."""

        try:
            response = self.client.messages.create(
                model=self.config["anthropic"]["model"],
                max_tokens=2048,
                system=temp_system,
                messages=[{
                    "role": "user",
                    "content": (
                        f"Analyze this document fragment for {domain}-specific risks:\n\n"
                        f"{document[:3000]}"
                    )
                }]
            )
            report = response.content[0].text

            # Extract key verification points from temporary report
            key_points = self._extract_key_points(report)

            # Notify owner
            self._notify_temporary_expansion(domain, key_points, parent_id, routing)

            return {
                "unit": f"TEMP-{domain.upper()}",
                "type": "TEMPORARY",
                "parent": parent_id,
                "report": report,
                "key_verification_points": key_points,
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            print(f"  [SPAWNER] TEMPORARY {domain} failed: {e}")
            return None

    def _extract_key_points(self, report: str) -> list:
        """Extracts key findings from temporary sub-agent report."""
        lines = report.split("\n")
        points = []
        for line in lines:
            line = line.strip()
            if line.startswith(("🔴", "🟠", "🟡", "→", "-", "•", "*")):
                clean = line.lstrip("🔴🟠🟡→-•* ").strip()
                if len(clean) > 20:
                    points.append(clean[:200])
            if len(points) >= 5:
                break
        return points

    def _notify_temporary_expansion(self, domain: str, key_points: list,
                                    parent_id: str, routing: dict):
        """Notifies owner via Slack + GitHub when temporary sub-agent is created."""
        suggested_file = f"system_prompt_{domain.lower().replace(' ', '_')}.md"
        expansion_data = {
            "domain": domain,
            "prompt_file": suggested_file,
            "confidence": "MODERATE",
            "is_unknown": True,
            "timestamp": datetime.utcnow().isoformat(),
            "key_verification_points": key_points,
            "session_id": routing.get("session_id", "UNKNOWN"),
            "triggered_by": parent_id,
            "expansion_type": "SUB_AGENT"
        }

        slack_cfg = self.config["notifications"]["slack"]
        github_cfg = self.config["notifications"]["github"]

        if slack_cfg.get("enabled") and slack_cfg.get("webhook_url"):
            self._send_slack_expansion(expansion_data, slack_cfg)

        if github_cfg.get("enabled") and github_cfg.get("token"):
            self._send_github_expansion(expansion_data, github_cfg)

        print(f"  [SPAWNER] SUB_AGENT_EXPANSION_RECOMMENDED dispatched for: {domain}")

    def _send_slack_expansion(self, data: dict, cfg: dict):
        """Sends Slack notification for temporary sub-agent."""
        import requests
        domain = data["domain"]
        points = data.get("key_verification_points", [])
        points_text = "\n".join([f"  → {p}" for p in points]) or "  (none extracted)"

        payload = {
            "channel": cfg["channel"],
            "username": "Dark Strategist — Sub-Agent Monitor",
            "icon_emoji": ":microscope:",
            "blocks": [
                {"type": "header",
                 "text": {"type": "plain_text",
                          "text": "🔬 SUB_AGENT_EXPANSION_RECOMMENDED"}},
                {"type": "section", "fields": [
                    {"type": "mrkdwn", "text": f"*Detected Domain:*\n{domain}"},
                    {"type": "mrkdwn", "text": f"*Triggered By:*\n{data['triggered_by']}"},
                    {"type": "mrkdwn", "text": f"*Type:*\nTemporary Sub-Agent"},
                    {"type": "mrkdwn", "text": f"*Session:*\n{data['session_id']}"},
                ]},
                {"type": "section",
                 "text": {"type": "mrkdwn",
                          "text": f"*Key Verification Points:*\n{points_text}"}},
                {"type": "section",
                 "text": {"type": "mrkdwn",
                          "text": f"*Action Required:*\nCreate permanent `{data['prompt_file']}`"}},
            ]
        }
        try:
            import requests
            requests.post(cfg["webhook_url"],
                         data=json.dumps(payload),
                         headers={"Content-Type": "application/json"},
                         timeout=10)
        except Exception as e:
            print(f"  [SPAWNER] Slack notification failed: {e}")

    def _send_github_expansion(self, data: dict, cfg: dict):
        """Creates GitHub Issue for temporary sub-agent expansion."""
        import requests
        domain = data["domain"]
        points = data.get("key_verification_points", [])
        points_md = "\n".join([f"- {p}" for p in points]) or "_None extracted_"

        title = f"[SUB_AGENT_EXPANSION] New sub-agent domain detected: {domain}"
        body = f"""## SUB_AGENT_EXPANSION_RECOMMENDED

Auto-generated by Dark Strategist Sub-Agent Spawner.

| Field | Value |
|-------|-------|
| **Detected Domain** | {domain} |
| **Triggered By** | {data['triggered_by']} |
| **Session ID** | {data['session_id']} |
| **Type** | Temporary Sub-Agent |
| **Timestamp** | {data['timestamp']} |

### Key Verification Points
{points_md}

### Recommended Action
Create permanent sub-agent: `{data['prompt_file']}`

---
_Auto-generated by Dark Strategist Agent v2.8.0_
"""
        headers = {
            "Authorization": f"token {cfg['token']}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        try:
            import requests
            requests.post(
                f"https://api.github.com/repos/{cfg['owner']}/{cfg['repo']}/issues",
                data=json.dumps({"title": title, "body": body,
                                 "labels": ["sub-agent-expansion", "new-prompt", "auto-generated"]}),
                headers=headers, timeout=15
            )
        except Exception as e:
            print(f"  [SPAWNER] GitHub Issue failed: {e}")
