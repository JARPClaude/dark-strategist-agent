"""
Dark Strategist — Agente Forense Orquestador (AFO)
Version: 2.9.0

Integrates:
  - Tribunal Adversarial (v2.8.0)
  - Simulación Social Masiva / SSM (v2.9.0)
  - Transparency Report (v2.9.0)
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
from ssm import SimulacionSocialMasiva


# ─── SWARM ACTIVATION SCORE ──────────────────────────────────────────────────

SWARM_ACTIVATION = {
    "SOLID UNDER PRESSURE":             1,
    "VIABLE WITH ADJUSTMENTS":          1,
    "VIABLE WITH CRITICAL CORRECTIONS": 3,
    "INVIABLE":                         5,
    "WAR_ROOM":                         7,
}

TRIBUNAL_LABELS = {
    1: "SINGLE", 3: "TRIBUNAL_LIGHT",
    5: "TRIBUNAL_FULL", 7: "TRIBUNAL_MAX",
}

TRIBUNAL_ASSIGNMENTS = {
    1: ["system_prompt.md"],
    3: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md"],
    5: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md",
        "system_prompt_code.md", "system_prompt_cybersecurity.md"],
    7: ["system_prompt.md", "system_prompt_financial.md", "system_prompt_legal.md",
        "system_prompt_code.md", "system_prompt_cybersecurity.md",
        "system_prompt_cloud.md", "system_prompt_publicsector.md"],
}


class AgenteForenseOrquestador:
    """
    Agente Forense Orquestador (AFO) — Nivel 0.
    Coordinates full pipeline: Tribunal + SSM + Transparency Report.
    """

    def __init__(self, config: dict, prompts_dir: str):
        self.config = config
        self.prompts_dir = Path(prompts_dir)
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.budget = BudgetController(config)
        self.router = DomainRouter(config, prompts_dir)
        self.spawner = SubAgentSpawner(config, prompts_dir)
        self.synthesizer = VerdictSynthesizer(config, prompts_dir)
        self.ssm = SimulacionSocialMasiva(config)
        self.session_id = str(uuid.uuid4())[:8].upper()
        self._transparency = self._init_transparency()

    def _init_transparency(self) -> dict:
        return {
            "session_id": self.session_id,
            "start_time": datetime.utcnow().isoformat(),
            "afo": {"routing": None, "swarm_score": None, "verdict_synthesized": False},
            "tribunal": {"mode": None, "agents": [], "conflicts_resolved": 0},
            "sub_agents": {"permanent": [], "temporary": []},
            "ssm": {"activated": False, "reason": None, "scale": None,
                    "personas": 0, "rounds": 4, "social_verdict": None},
            "budget": {},
            "notifications": {"slack": False, "github": False, "sheets": False},
        }

    def run(self, document: str, forced_tribunal_size: int = None,
            run_ssm: bool = False, ssm_scale: str = "MESO") -> dict:
        """
        Full AFO pipeline:
        1. Routing
        2. Initial audit → Swarm Activation Score
        3. Tribunal (N1 parallel + N2 sub-agents)
        4. Verdict Synthesis
        5. SSM (if verdict qualifies)
        6. Transparency Report
        7. Notifications + Logging
        """
        start_time = time.time()
        self._log("AFO initiated")

        # ── 1. Routing ─────────────────────────────────────────────────────
        self._log("Routing document...")
        routing = self.router.detect_domain(document)
        routing["session_id"] = self.session_id
        self._transparency["afo"]["routing"] = {
            "domain": routing["domain"],
            "prompt": routing["prompt_file"],
            "confidence": routing["confidence"],
            "is_unknown": routing.get("is_unknown", False)
        }
        self._log(f"Domain: {routing['domain']} | Confidence: {routing['confidence']}")

        # ── 2. Initial audit → Swarm Activation Score ──────────────────────
        self._log("Running initial audit for Swarm Activation Score...")
        initial_report = self._run_single_audit(document, routing)
        tribunal_size = forced_tribunal_size or self._calculate_swarm_score(initial_report)
        tribunal_label = TRIBUNAL_LABELS[tribunal_size]
        self._transparency["afo"]["swarm_score"] = {
            "tribunal_size": tribunal_size,
            "tribunal_label": tribunal_label
        }
        self._log(f"Swarm Score → {tribunal_label} ({tribunal_size} agents)")

        # ── 3. Tribunal ────────────────────────────────────────────────────
        if tribunal_size == 1:
            n1_reports = [{"agent_id": "AF-01", "prompt": routing["prompt_file"],
                           "report": initial_report, "sub_agents_used": []}]
        else:
            self._log(f"Launching Tribunal {tribunal_label}...")
            n1_reports = self._run_tribunal(document, tribunal_size, routing)

        self._transparency["tribunal"]["mode"] = tribunal_label
        for r in n1_reports:
            self._transparency["tribunal"]["agents"].append({
                "id": r["agent_id"],
                "prompt": r["prompt"],
                "status": "COMPLETED" if "[AGENT_FAILED" not in r["report"] else "FAILED",
                "sub_agents": len(r.get("sub_agents_used", []))
            })
            for sa in r.get("sub_agents_used", []):
                if sa.get("type") == "PERMANENT":
                    self._transparency["sub_agents"]["permanent"].append(sa["unit"])
                else:
                    self._transparency["sub_agents"]["temporary"].append(sa["unit"])

        # ── 4. Verdict Synthesis ───────────────────────────────────────────
        self._log("Synthesizing verdicts...")
        final_verdict = self.synthesizer.synthesize(
            document=document, n1_reports=n1_reports,
            routing=routing, tribunal_label=tribunal_label,
            session_id=self.session_id
        )
        self._transparency["afo"]["verdict_synthesized"] = True

        # ── 5. SSM ─────────────────────────────────────────────────────────
        ssm_report = ""
        should_run, ssm_reason = self.ssm.should_activate(final_verdict, forced=run_ssm)
        self._transparency["ssm"]["reason"] = ssm_reason

        if should_run:
            self._log(f"SSM activated — {ssm_reason}")
            self._transparency["ssm"]["activated"] = True
            self._transparency["ssm"]["scale"] = ssm_scale
            ssm_report = self.ssm.run(
                document=document,
                domain=routing["domain"],
                tribunal_verdict=final_verdict,
                session_id=self.session_id,
                scale=ssm_scale
            )
            # Extract social verdict for transparency
            for line in ssm_report.split("\n"):
                if "SOCIALLY" in line:
                    self._transparency["ssm"]["social_verdict"] = line.strip()
                    break
            personas_count = self.config.get("ssm", {}).get(
                "max_personas", {"MICRO": 5, "MESO": 10, "MACRO": 20}.get(ssm_scale, 10))
            self._transparency["ssm"]["personas"] = personas_count
        else:
            self._log(f"SSM not activated — {ssm_reason}")

        # ── 6. Transparency Report ─────────────────────────────────────────
        duration = time.time() - start_time
        self._transparency["budget"] = self.budget.summary()
        transparency_report = self._build_transparency_report(duration, ssm_reason)

        # ── 7. Notifications + Logging ─────────────────────────────────────
        slack_sent, github_sent = self._dispatch_notifications(routing, n1_reports)
        self._log_to_sheets(routing, final_verdict, duration, tribunal_label)
        self._transparency["notifications"] = {
            "slack": slack_sent, "github": github_sent, "sheets": True
        }

        self._log(f"Session complete in {duration:.1f}s")

        return {
            "session_id": self.session_id,
            "domain": routing["domain"],
            "tribunal_mode": tribunal_label,
            "agents_deployed": tribunal_size,
            "n1_reports": n1_reports,
            "final_verdict": final_verdict,
            "ssm_report": ssm_report,
            "transparency_report": transparency_report,
            "duration_seconds": round(duration, 2)
        }

    def _build_transparency_report(self, duration: float, ssm_reason: str) -> str:
        t = self._transparency
        sub_perm = list(set(t["sub_agents"]["permanent"]))
        sub_temp = list(set(t["sub_agents"]["temporary"]))
        budget = t["budget"]

        agents_lines = "\n".join([
            f"    {a['id']}  {a['prompt']:<45} {a['status']}  (N2: {a['sub_agents']})"
            for a in t["tribunal"]["agents"]
        ])

        perm_lines = "\n".join([f"    {u}" for u in sub_perm]) if sub_perm else "    None"
        temp_lines = "\n".join([f"    {u}  ← SUB_AGENT_EXPANSION_RECOMMENDED dispatched"
                                for u in sub_temp]) if sub_temp else "    None"

        ssm_block = ""
        if t["ssm"]["activated"]:
            ssm_block = f"""
  SSM STATUS:     ACTIVATED
  Scale:          {t['ssm']['scale']} ({t['ssm']['personas']} personas × {t['ssm']['rounds']} rounds)
  Social Verdict: {t['ssm']['social_verdict'] or 'See REPORTE DE IMPACTO SOCIAL'}"""
        else:
            ssm_block = f"""
  SSM STATUS:     NOT ACTIVATED
  Reason:         {ssm_reason}"""

        notif = t["notifications"]
        notif_lines = (
            f"  Slack:   {'✓ Dispatched' if notif['slack'] else '— Not configured'}\n"
            f"  GitHub:  {'✓ Issue created' if notif['github'] else '— Not configured'}\n"
            f"  Sheets:  {'✓ Logged' if notif['sheets'] else '— Not configured'}"
        )

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DARK STRATEGIST — TRANSPARENCY REPORT
Session: DS-{t['session_id']} | Duration: {round(duration, 1)}s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGENTE FORENSE ORQUESTADOR (AFO)
  Domain detected:    {t['afo']['routing']['domain']}
  Prompt selected:    {t['afo']['routing']['prompt']}
  Confidence:         {t['afo']['routing']['confidence']}
  Unknown domain:     {'YES — DOMAIN_EXPANSION_RECOMMENDED dispatched' if t['afo']['routing']['is_unknown'] else 'NO'}
  Swarm Score:        {t['afo']['swarm_score']['tribunal_label']} ({t['afo']['swarm_score']['tribunal_size']} agents)
  Verdict synthesis:  {'✓ Complete' if t['afo']['verdict_synthesized'] else '✗ Incomplete'}

TRIBUNAL ADVERSARIAL
  Mode:          {t['tribunal']['mode']}
  Blind agents:  YES — agents operated independently
{agents_lines}

SUB-AGENTES FORENSES PERMANENTES (N2)
{perm_lines}

SUB-AGENTES FORENSES TEMPORALES (N2)
{temp_lines}

SIMULACIÓN SOCIAL MASIVA{ssm_block}

BUDGET CONSUMED
  Total calls:   {budget.get('total_calls', 0)}/{budget.get('max_calls', 30)} ({budget.get('budget_used_percent', 0)}%)
  N1 agents:     {budget.get('agents_deployed', 0)}/{budget.get('max_agents', 7)}
  Breakdown:     {budget.get('calls_made', {})}

NOTIFICATIONS
{notif_lines}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    def _run_single_audit(self, document: str, routing: dict) -> str:
        if not self.budget.can_proceed("single"):
            return "[BUDGET_EXCEEDED]"
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
        report_upper = report.upper()
        if "WAR_ROOM" in report_upper:
            return 7
        for verdict, size in SWARM_ACTIVATION.items():
            if verdict in report_upper:
                return size
        return 3

    def _run_tribunal(self, document: str, size: int, routing: dict) -> list:
        prompts = self._select_tribunal_prompts(size, routing)
        results = []
        with ThreadPoolExecutor(max_workers=min(size, self.budget.remaining_agents())) as executor:
            futures = {
                executor.submit(self._run_n1_agent,
                                f"AF-{str(i+1).zfill(2)}", document,
                                prompt, routing): f"AF-{str(i+1).zfill(2)}"
                for i, prompt in enumerate(prompts)
            }
            for future in as_completed(futures):
                aid = futures[future]
                try:
                    results.append(future.result(timeout=300))
                    self._log(f"{aid} completed")
                except Exception as e:
                    self._log(f"{aid} failed: {e}")
                    results.append({"agent_id": aid, "prompt": "unknown",
                                    "report": f"[AGENT_FAILED: {e}]",
                                    "sub_agents_used": []})
        return results

    def _run_n1_agent(self, agent_id: str, document: str,
                      prompt_file: str, routing: dict) -> dict:
        if not self.budget.can_proceed("n1"):
            return {"agent_id": agent_id, "prompt": prompt_file,
                    "report": "[BUDGET_EXCEEDED]", "sub_agents_used": []}
        path = self.prompts_dir / prompt_file
        if not path.exists():
            path = self.prompts_dir / "system_prompt.md"
        system_prompt = path.read_text(encoding="utf-8")
        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=self.config["anthropic"]["max_tokens"],
            system=system_prompt,
            messages=[{"role": "user",
                       "content": f"You are {agent_id} in a Tribunal Adversarial. Audit independently:\n\n{document}"}]
        )
        self.budget.record_call("n1")
        report = response.content[0].text
        sub_agents = self.spawner.evaluate_and_spawn(agent_id, report, document, routing)
        return {"agent_id": agent_id, "prompt": prompt_file,
                "report": report, "sub_agents_used": sub_agents}

    def _select_tribunal_prompts(self, size: int, routing: dict) -> list:
        base = TRIBUNAL_ASSIGNMENTS.get(size, TRIBUNAL_ASSIGNMENTS[3]).copy()
        routed = routing.get("prompt_file", "system_prompt.md")
        if routed not in base:
            base[0] = routed
        return base[:size]

    def _dispatch_notifications(self, routing: dict, n1_reports: list) -> tuple:
        slack_sent, github_sent = False, False
        slack_cfg = self.config["notifications"]["slack"]
        github_cfg = self.config["notifications"]["github"]
        if routing.get("is_unknown"):
            if slack_cfg.get("enabled") and slack_cfg.get("webhook_url"):
                slack_sent = SlackNotifier(slack_cfg["webhook_url"],
                                           slack_cfg["channel"]).send_domain_expansion(routing)
            if github_cfg.get("enabled") and github_cfg.get("token"):
                github_sent = GitHubNotifier(github_cfg["token"], github_cfg["owner"],
                                             github_cfg["repo"]).create_domain_expansion_issue(routing)
        return slack_sent, github_sent

    def _log_to_sheets(self, routing, verdict, duration, tribunal_label):
        sheets_cfg = self.config["logging"]["google_sheets"]
        if not sheets_cfg.get("enabled") or not sheets_cfg.get("spreadsheet_id"):
            return
        try:
            SheetsLogger(sheets_cfg["credentials_file"],
                         sheets_cfg["spreadsheet_id"],
                         sheets_cfg["sheet_name"]).log_execution(
                {**routing, "tribunal_mode": tribunal_label},
                verdict, False, False, duration)
        except Exception as e:
            self._log(f"Sheets skipped: {e}")

    def _log(self, msg: str):
        ts = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[AFO {self.session_id}] {ts} — {msg}")
