"""
Dark Strategist — Agente Forense Orquestador (AFO)
Nivel 0: Orquesta el Tribunal Adversarial completo.
Version: 2.8.0

Jerarquía:
  N0 — Agente Forense Orquestador (AFO)     ← este archivo
  N1 — Agentes Forenses (paralelos)
  N2 — Sub-agentes Forenses (bajo demanda)
       ├── Permanentes: UNITs del catálogo
       └── Temporales: creados dinámicamente → notificación al propietario
"""

import json
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import anthropic

from budget_controller import BudgetController
from router import DomainRouter
from sub_agent_spawner import SubAgentSpawner
from verdict_synthesizer import VerdictSynthesizer
from notifier import SlackNotifier, GitHubNotifier
from sheets_logger import SheetsLogger


# ─── SWARM ACTIVATION SCORE ──────────────────────────────────────────────────

SWARM_ACTIVATION = {
    "SOLID UNDER PRESSURE":          1,  # Single mode
    "VIABLE WITH ADJUSTMENTS":       1,  # Single mode
    "VIABLE WITH CRITICAL CORRECTIONS": 3,  # Tribunal Light
    "INVIABLE":                      5,  # Tribunal Full
    "WAR_ROOM":                      7,  # Tribunal Max
}

TRIBUNAL_LABELS = {
    1: "SINGLE",
    3: "TRIBUNAL_LIGHT",
    5: "TRIBUNAL_FULL",
    7: "TRIBUNAL_MAX",
}

# N1 agent assignments per tribunal size
TRIBUNAL_ASSIGNMENTS = {
    1: ["system_prompt.md"],
    3: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md"],
    5: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md",
        "system_prompt_code.md", "system_prompt_cybersecurity.md"],
    7: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md",
        "system_prompt_code.md", "system_prompt_cybersecurity.md",
        "system_prompt_cloud.md", "system_prompt_publicsector.md"],
}


# ─── AFO ─────────────────────────────────────────────────────────────────────

class AgenteForenseOrquestador:
    """
    Agente Forense Orquestador (AFO) — Nivel 0.
    Coordina el Tribunal Adversarial completo y emite el veredicto unificado.
    """

    def __init__(self, config: dict, prompts_dir: str):
        self.config = config
        self.prompts_dir = Path(prompts_dir)
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.budget = BudgetController(config)
        self.router = DomainRouter(config, prompts_dir)
        self.spawner = SubAgentSpawner(config, prompts_dir)
        self.synthesizer = VerdictSynthesizer(config, prompts_dir)
        self.session_id = str(uuid.uuid4())[:8].upper()

    def run(self, document: str, forced_tribunal_size: int = None) -> dict:
        """
        Pipeline completo del AFO:
        1. Routing
        2. Auditoría inicial (single) → Swarm Activation Score
        3. Lanzamiento de Agentes Forenses N1 en paralelo
        4. Sub-agentes N2 bajo demanda por cada N1
        5. Síntesis de veredictos → Veredicto Unificado Final
        """
        start_time = time.time()
        self._log(f"AFO Session {self.session_id} initiated")

        # ── Step 1: Routing ────────────────────────────────────────────────
        self._log("Detecting document domain...")
        routing = self.router.detect_domain(document)
        routing["session_id"] = self.session_id
        self._log(f"Domain: {routing['domain']} | Confidence: {routing['confidence']}")

        # ── Step 2: Initial audit → Swarm Activation Score ────────────────
        self._log("Running initial single audit for Swarm Activation Score...")
        initial_report = self._run_single_audit(document, routing)
        tribunal_size = forced_tribunal_size or self._calculate_swarm_score(initial_report)
        tribunal_label = TRIBUNAL_LABELS[tribunal_size]
        self._log(f"Swarm Activation Score → {tribunal_label} ({tribunal_size} agents)")

        # ── Step 3: Launch N1 agents in parallel ──────────────────────────
        if tribunal_size == 1:
            n1_reports = [{"agent_id": "AF-01", "prompt": "system_prompt.md",
                           "report": initial_report, "sub_agents_used": []}]
        else:
            self._log(f"Launching {tribunal_size} Agentes Forenses in parallel...")
            n1_reports = self._run_tribunal(document, tribunal_size, routing)

        # ── Step 4: Synthesize verdicts ───────────────────────────────────
        self._log("Synthesizing verdicts...")
        final_verdict = self.synthesizer.synthesize(
            document=document,
            n1_reports=n1_reports,
            routing=routing,
            tribunal_label=tribunal_label,
            session_id=self.session_id
        )

        # ── Step 5: Notifications ─────────────────────────────────────────
        self._dispatch_notifications(routing, n1_reports)

        # ── Step 6: Logging ───────────────────────────────────────────────
        duration = time.time() - start_time
        self._log_to_sheets(routing, final_verdict, duration, tribunal_label)

        self._log(f"AFO Session {self.session_id} complete in {duration:.1f}s")

        return {
            "session_id": self.session_id,
            "domain": routing["domain"],
            "tribunal_mode": tribunal_label,
            "agents_deployed": tribunal_size,
            "n1_reports": n1_reports,
            "final_verdict": final_verdict,
            "duration_seconds": round(duration, 2)
        }

    # ─── Internal Methods ─────────────────────────────────────────────────────

    def _run_single_audit(self, document: str, routing: dict) -> str:
        """Runs a single audit with the routed domain prompt."""
        if not self.budget.can_proceed("single"):
            return "[BUDGET_EXCEEDED: single audit blocked]"
        system_prompt = self.router.load_domain_prompt(routing)
        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=self.config["anthropic"]["max_tokens"],
            system=system_prompt,
            messages=[{"role": "user", "content": f"Audit:\n\n{document}"}]
        )
        self.budget.record_call("single")
        return response.content[0].text

    def _calculate_swarm_score(self, report: str) -> int:
        """Determines tribunal size based on severity found in initial audit."""
        report_upper = report.upper()
        if "WAR_ROOM" in report_upper or "[WAR ROOM ACTIVATED]" in report_upper:
            return 7
        for verdict, size in SWARM_ACTIVATION.items():
            if verdict in report_upper:
                return size
        return 3  # Default to Tribunal Light if unclear

    def _run_tribunal(self, document: str, size: int, routing: dict) -> list:
        """Launches N1 Agentes Forenses in parallel."""
        prompts = self._select_tribunal_prompts(size, routing)
        results = []

        max_workers = min(size, self.budget.remaining_agents())
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {}
            for i, prompt_file in enumerate(prompts):
                agent_id = f"AF-{str(i+1).zfill(2)}"
                future = executor.submit(
                    self._run_n1_agent,
                    agent_id=agent_id,
                    document=document,
                    prompt_file=prompt_file,
                    routing=routing
                )
                futures[future] = agent_id

            for future in as_completed(futures):
                agent_id = futures[future]
                try:
                    result = future.result(timeout=300)
                    results.append(result)
                    self._log(f"{agent_id} completed")
                except Exception as e:
                    self._log(f"{agent_id} failed: {e}")
                    results.append({
                        "agent_id": agent_id,
                        "prompt": "unknown",
                        "report": f"[AGENT_FAILED: {str(e)}]",
                        "sub_agents_used": []
                    })

        return results

    def _run_n1_agent(self, agent_id: str, document: str,
                      prompt_file: str, routing: dict) -> dict:
        """Runs a single N1 Agente Forense and spawns N2 sub-agents if needed."""
        if not self.budget.can_proceed("n1"):
            return {"agent_id": agent_id, "prompt": prompt_file,
                    "report": "[BUDGET_EXCEEDED]", "sub_agents_used": []}

        prompt_path = self.prompts_dir / prompt_file
        if not prompt_path.exists():
            prompt_path = self.prompts_dir / "system_prompt.md"
        system_prompt = prompt_path.read_text(encoding="utf-8")

        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=self.config["anthropic"]["max_tokens"],
            system=system_prompt,
            messages=[{
                "role": "user",
                "content": (
                    f"You are {agent_id} in a Tribunal Adversarial. "
                    f"Audit independently and report all findings:\n\n{document}"
                )
            }]
        )
        self.budget.record_call("n1")
        report = response.content[0].text

        # Spawn N2 sub-agents if the N1 detects specialized needs
        sub_agents_used = self.spawner.evaluate_and_spawn(
            agent_id=agent_id,
            report=report,
            document=document,
            routing=routing
        )

        return {
            "agent_id": agent_id,
            "prompt": prompt_file,
            "report": report,
            "sub_agents_used": sub_agents_used
        }

    def _select_tribunal_prompts(self, size: int, routing: dict) -> list:
        """Selects prompt files for tribunal, prioritizing the routed domain."""
        base_prompts = TRIBUNAL_ASSIGNMENTS.get(size, TRIBUNAL_ASSIGNMENTS[3]).copy()
        routed_prompt = routing.get("prompt_file", "system_prompt.md")
        if routed_prompt not in base_prompts:
            base_prompts[0] = routed_prompt
        return base_prompts[:size]

    def _dispatch_notifications(self, routing: dict, n1_reports: list):
        """Notifies owner of unknown domains and temporary sub-agents."""
        slack_cfg = self.config["notifications"]["slack"]
        github_cfg = self.config["notifications"]["github"]

        if routing.get("is_unknown"):
            if slack_cfg.get("enabled") and slack_cfg.get("webhook_url"):
                SlackNotifier(slack_cfg["webhook_url"],
                              slack_cfg["channel"]).send_domain_expansion(routing)
            if github_cfg.get("enabled") and github_cfg.get("token"):
                GitHubNotifier(github_cfg["token"], github_cfg["owner"],
                               github_cfg["repo"]).create_domain_expansion_issue(routing)

    def _log_to_sheets(self, routing: dict, verdict: str,
                       duration: float, tribunal_label: str):
        """Logs execution to Google Sheets."""
        sheets_cfg = self.config["logging"]["google_sheets"]
        if not sheets_cfg.get("enabled") or not sheets_cfg.get("spreadsheet_id"):
            return
        try:
            routing_extended = {**routing, "tribunal_mode": tribunal_label}
            SheetsLogger(
                sheets_cfg["credentials_file"],
                sheets_cfg["spreadsheet_id"],
                sheets_cfg["sheet_name"]
            ).log_execution(routing_extended, verdict, False, False, duration)
        except Exception as e:
            self._log(f"Sheets logging skipped: {e}")

    def _log(self, message: str):
        timestamp = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[AFO {self.session_id}] {timestamp} — {message}")
