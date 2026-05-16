"""
Dark Strategist v3.0.0 — Tribunal Transversal
Replaces Tribunal Adversarial with the two-layer architecture:
  Layer 1: Agentes de Rol — simulate the domain environment
  Layer 2: Agentes Forenses — audit what the Rol agents produced
  AFO: synthesizes both layers into unified verdict

Key difference from v2.x:
  v2.x: Forenses read the document directly
  v3.0: Forenses audit the Rol simulation + the document
"""

import json
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import anthropic

from schema import RuntimeContext, AgentVerdictOutput, UnifiedVerdictOutput, Finding
from prompt_engine import PromptEngine
from budget_controller import BudgetController
from sub_agent_spawner import SubAgentSpawner
from notifier import SlackNotifier, GitHubNotifier
from sheets_logger import SheetsLogger
from ssm import SimulacionSocialMasiva


class TribunalTransversal:
    """
    Agente Forense Orquestador (AFO) — v3.0.0
    Two-layer Tribunal Transversal:
      Layer 1: Agentes de Rol (parallel, blind)
      Layer 2: Agentes Forenses (audit the simulation)
      Synthesis: AFO consolidates → UnifiedVerdictOutput
    """

    def __init__(self, config: dict):
        self.config = config
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.engine = PromptEngine()
        self.budget = BudgetController(config)
        self.spawner = SubAgentSpawner(config, config.get("prompts_dir", "./prompts"))
        self.ssm = SimulacionSocialMasiva(config)
        self.session_id = str(uuid.uuid4())[:8].upper()
        self._transparency = self._init_transparency()

    def run(self, document: str, ctx: RuntimeContext) -> dict:
        """
        Full Tribunal Transversal pipeline.
        Returns dict with final verdict, SSM report, and transparency report.
        """
        start_time = time.time()
        self._log(f"Tribunal Transversal initiated — {ctx.domain} / {ctx.subscenario}")
        self._log(f"Regime: {ctx.regime} | Tribunal: {ctx.tribunal_label}")

        # ── Layer 1: Agentes de Rol ────────────────────────────────────────
        self._log(f"Layer 1: Launching {len(ctx.rol_agents)} Agentes de Rol...")
        rol_outputs = self._run_rol_layer(document, ctx)
        self._transparency["rol_agents"] = [
            {"id": r["agent_id"], "role": r["role"], "stance": r.get("stance", "NEUTRAL")}
            for r in rol_outputs
        ]

        # Build simulation summary for Forense layer
        rol_simulation_summary = self._summarize_rol_outputs(rol_outputs)

        # ── Layer 2: Agentes Forenses ──────────────────────────────────────
        self._log(f"Layer 2: Launching {len(ctx.forense_agents)} Agentes Forenses...")
        forense_outputs = self._run_forense_layer(document, ctx, rol_simulation_summary)
        self._transparency["forense_agents"] = [
            {"id": f["agent_id"], "role": f["role"],
             "verdict": f.get("preliminary_verdict", "UNKNOWN")}
            for f in forense_outputs
        ]

        # ── Synthesis ──────────────────────────────────────────────────────
        self._log("Synthesizing all outputs...")
        all_outputs = rol_outputs + forense_outputs
        unified = self._synthesize(document, ctx, all_outputs)
        self._transparency["afo"]["verdict_synthesized"] = True

        # ── SSM ────────────────────────────────────────────────────────────
        ssm_report = ""
        should_run, ssm_reason = self.ssm.should_activate(
            unified.final_verdict, forced=ctx.run_ssm
        )
        self._transparency["ssm"]["reason"] = ssm_reason

        if should_run:
            self._log(f"SSM activated — {ssm_reason}")
            self._transparency["ssm"]["activated"] = True
            self._transparency["ssm"]["scale"] = ctx.ssm_scale
            ssm_report = self.ssm.run(
                document=document,
                domain=ctx.domain,
                tribunal_verdict=unified.final_verdict,
                session_id=self.session_id,
                scale=ctx.ssm_scale
            )
            for line in ssm_report.split("\n"):
                if "SOCIALLY" in line:
                    self._transparency["ssm"]["social_verdict"] = line.strip()
                    unified.ssm_activated = True
                    unified.ssm_social_verdict = line.strip()
                    break

        # ── Notifications + Logging ────────────────────────────────────────
        duration = time.time() - start_time
        self._transparency["budget"] = self.budget.summary()
        transparency_report = self._build_transparency_report(
            ctx, duration, ssm_reason, unified
        )

        self._log(f"Session complete in {duration:.1f}s")

        return {
            "session_id": self.session_id,
            "domain": ctx.domain,
            "subscenario": ctx.subscenario,
            "regime": ctx.regime,
            "tribunal_mode": ctx.tribunal_label,
            "unified_verdict": unified.model_dump(),
            "final_verdict_text": self._format_verdict(unified),
            "ssm_report": ssm_report,
            "transparency_report": transparency_report,
            "duration_seconds": round(duration, 2),
        }

    # ─── Layer 1: Rol ─────────────────────────────────────────────────────────

    def _run_rol_layer(self, document: str, ctx: RuntimeContext) -> list:
        results = []
        max_workers = min(len(ctx.rol_agents), self.budget.remaining_agents())

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {}
            for i, role in enumerate(ctx.rol_agents):
                agent_id = f"ROL-{str(i+1).zfill(2)}"
                prompt = self.engine.build_rol_prompt(agent_id, role, ctx)
                future = executor.submit(
                    self._call_agent, agent_id, "ROL", role, prompt, document
                )
                futures[future] = (agent_id, role)

            for future in as_completed(futures):
                agent_id, role = futures[future]
                try:
                    result = future.result(timeout=120)
                    result["role"] = role
                    results.append(result)
                    self._log(f"{agent_id} ({role[:30]}) — stance: {result.get('stance', 'N/A')}")
                except Exception as e:
                    self._log(f"{agent_id} failed: {e}")
                    results.append({"agent_id": agent_id, "role": role,
                                    "agent_type": "ROL", "error": str(e)})

        return results

    # ─── Layer 2: Forense ─────────────────────────────────────────────────────

    def _run_forense_layer(self, document: str, ctx: RuntimeContext,
                           rol_simulation: str) -> list:
        results = []
        max_workers = min(len(ctx.forense_agents), self.budget.remaining_agents())

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {}
            for i, role in enumerate(ctx.forense_agents):
                agent_id = f"FOR-{str(i+1).zfill(2)}"
                prompt = self.engine.build_forense_prompt(
                    agent_id, role, ctx, rol_simulation
                )
                future = executor.submit(
                    self._call_agent, agent_id, "FORENSE", role, prompt, document
                )
                futures[future] = (agent_id, role)

            for future in as_completed(futures):
                agent_id, role = futures[future]
                try:
                    result = future.result(timeout=120)
                    result["role"] = role
                    # Spawn N2 sub-agents if needed
                    sub_agents = self.spawner.evaluate_and_spawn(
                        agent_id, str(result), document,
                        {"domain": ctx.domain, "session_id": self.session_id}
                    )
                    result["sub_agents_used"] = sub_agents
                    results.append(result)
                    self._log(f"{agent_id} ({role[:30]}) — verdict: {result.get('preliminary_verdict', 'N/A')}")
                except Exception as e:
                    self._log(f"{agent_id} failed: {e}")
                    results.append({"agent_id": agent_id, "role": role,
                                    "agent_type": "FORENSE", "error": str(e)})

        return results

    # ─── Synthesis ────────────────────────────────────────────────────────────

    def _synthesize(self, document: str, ctx: RuntimeContext,
                    all_outputs: list) -> UnifiedVerdictOutput:
        """Calls AFO synthesis — produces UnifiedVerdictOutput."""
        prompt = self.engine.build_synthesis_prompt(
            ctx, all_outputs, ctx.tribunal_label, self.session_id
        )
        try:
            response = self.client.messages.create(
                model=self.config["anthropic"]["model"],
                max_tokens=self.config["anthropic"]["max_tokens"],
                system="You are the Dark Strategist AFO. Respond only in valid JSON.",
                messages=[{"role": "user", "content": prompt}]
            )
            self.budget.record_call("synthesis")
            text = response.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            data = json.loads(text)
            return UnifiedVerdictOutput(**data)
        except Exception as e:
            self._log(f"Synthesis failed: {e} — using deterministic fallback")
            return self._deterministic_synthesis(ctx, all_outputs)

    def _deterministic_synthesis(self, ctx: RuntimeContext,
                                 all_outputs: list) -> UnifiedVerdictOutput:
        """Fallback synthesis when Claude call fails."""
        all_findings = []
        for output in all_outputs:
            if isinstance(output.get("findings"), list):
                for f in output["findings"]:
                    try:
                        all_findings.append(Finding(**f))
                    except Exception:
                        pass

        fatal = [f for f in all_findings if f.severity == "FATAL"]
        serious = [f for f in all_findings if f.severity == "SERIOUS"]
        moderate = [f for f in all_findings if f.severity == "MODERATE"]
        latent = [f for f in all_findings if f.severity == "LATENT"]

        if fatal:
            verdict = "INVIABLE"
        elif serious:
            verdict = "VIABLE WITH CRITICAL CORRECTIONS"
        elif moderate:
            verdict = "VIABLE WITH ADJUSTMENTS"
        else:
            verdict = "SOLID UNDER PRESSURE"

        return UnifiedVerdictOutput(
            session_id=self.session_id,
            domain=ctx.domain,
            subscenario=ctx.subscenario,
            regime=ctx.regime,
            tribunal_mode=ctx.tribunal_label,
            agents_consulted=len(all_outputs),
            fatal_findings=fatal,
            serious_findings=serious,
            moderate_findings=moderate,
            latent_findings=latent,
            final_verdict=verdict,
            confidence="MODERATE",
            verdict_reasoning="Deterministic synthesis — Claude synthesis call failed.",
        )

    # ─── Helpers ──────────────────────────────────────────────────────────────

    def _call_agent(self, agent_id: str, agent_type: str, role: str,
                    prompt: str, document: str) -> dict:
        """Makes a single Claude API call for any agent type."""
        if not self.budget.can_proceed(agent_type.lower()):
            return {"agent_id": agent_id, "agent_type": agent_type,
                    "error": "BUDGET_EXCEEDED"}

        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=self.config["anthropic"]["max_tokens"],
            system=prompt,
            messages=[{"role": "user",
                        "content": f"Analyze this document:\n\n{document[:4000]}"}]
        )
        self.budget.record_call(agent_type.lower() if agent_type != "FORENSE" else "n1")

        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        try:
            result = json.loads(text)
            result["raw_output"] = text
            return result
        except Exception:
            return {"agent_id": agent_id, "agent_type": agent_type,
                    "raw_output": text, "preliminary_verdict": "UNKNOWN"}

    def _summarize_rol_outputs(self, rol_outputs: list) -> str:
        """Summarizes Rol agent outputs for the Forense layer."""
        summaries = []
        for r in rol_outputs:
            aid = r.get("agent_id", "ROL-?")
            role = r.get("role", "Unknown Role")
            stance = r.get("stance", "NEUTRAL")
            concerns = r.get("primary_concerns", [])
            action = r.get("intended_action", "Not specified")
            summaries.append(
                f"{aid} ({role}): stance={stance}, "
                f"action={action}, "
                f"concerns={'; '.join(concerns[:2])}"
            )
        return "\n".join(summaries)

    def _format_verdict(self, unified: UnifiedVerdictOutput) -> str:
        """Formats unified verdict as human-readable text."""
        severity = unified.severity_summary
        lines = [
            f"\n{'='*60}",
            f"VEREDICTO FORENSE UNIFICADO",
            f"{'='*60}",
            f"Domain:     {unified.domain} / {unified.subscenario}",
            f"Regime:     {unified.regime}",
            f"Tribunal:   {unified.tribunal_mode} ({unified.agents_consulted} agents)",
            f"",
            f"FINDINGS: 🔴 {severity['FATAL']} FATAL | "
            f"🟠 {severity['SERIOUS']} SERIOUS | "
            f"🟡 {severity['MODERATE']} MODERATE | "
            f"🔵 {severity['LATENT']} LATENT",
            f"",
        ]

        for f in unified.fatal_findings:
            lines.append(f"🔴 FATAL — {f.title}")
            lines.append(f"   {f.description}")
            lines.append(f"   Evidence: {f.evidence}")

        for f in unified.serious_findings:
            lines.append(f"🟠 SERIOUS — {f.title}")
            lines.append(f"   {f.description}")

        if unified.conflicts_detected:
            lines.append(f"\nCONFLICTS RESOLVED: {len(unified.conflicts_detected)}")

        if unified.multi_agent_confirmed:
            lines.append(f"MULTI-AGENT CONFIRMED: {len(unified.multi_agent_confirmed)}")

        lines += [
            f"",
            f"VEREDICTO: {unified.final_verdict}",
            f"Confidence: {unified.confidence}",
            f"Reasoning:  {unified.verdict_reasoning}",
            f"{'='*60}",
        ]
        return "\n".join(lines)

    def _build_transparency_report(self, ctx: RuntimeContext, duration: float,
                                   ssm_reason: str,
                                   unified: UnifiedVerdictOutput) -> str:
        t = self._transparency
        rol_lines = "\n".join([
            f"    {a['id']}  {a['role'][:45]}  stance={a['stance']}"
            for a in t.get("rol_agents", [])
        ])
        for_lines = "\n".join([
            f"    {a['id']}  {a['role'][:45]}  verdict={a['verdict']}"
            for a in t.get("forense_agents", [])
        ])
        budget = t.get("budget", {})
        ssm_block = (
            f"\n  STATUS:  ACTIVATED | Scale: {t['ssm']['scale']} | "
            f"Social: {t['ssm'].get('social_verdict', 'See SSM report')}"
            if t["ssm"]["activated"]
            else f"\n  STATUS:  NOT ACTIVATED — {ssm_reason}"
        )

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DARK STRATEGIST v3.0.0 — TRANSPARENCY REPORT
Session: DS-{self.session_id} | Duration: {round(duration,1)}s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGENTE FORENSE ORQUESTADOR (AFO)
  Domain:      {ctx.domain} / {ctx.subscenario}
  Regime:      {ctx.regime} — {ctx.regime_description}
  Tribunal:    {ctx.tribunal_label}
  Synthesized: YES — VEREDICTO FORENSE UNIFICADO

TRIBUNAL TRANSVERSAL — LAYER 1: AGENTES DE ROL
  (Simulated the domain environment)
{rol_lines or '    None'}

TRIBUNAL TRANSVERSAL — LAYER 2: AGENTES FORENSES
  (Audited the simulation + document)
{for_lines or '    None'}

VERDICT SUMMARY
  🔴 FATAL:    {len(unified.fatal_findings)}
  🟠 SERIOUS:  {len(unified.serious_findings)}
  🟡 MODERATE: {len(unified.moderate_findings)}
  🔵 LATENT:   {len(unified.latent_findings)}
  Confirmed by 2+ agents: {len(unified.multi_agent_confirmed)}
  Conflicts resolved:     {len(unified.conflicts_detected)}

SIMULACIÓN SOCIAL MASIVA (SSM){ssm_block}

BUDGET CONSUMED
  Total calls: {budget.get('total_calls',0)}/{budget.get('max_calls',30)} ({budget.get('budget_used_percent',0)}%)
  Breakdown:   {budget.get('calls_made',{})}

FINAL VERDICT: {unified.final_verdict} | Confidence: {unified.confidence}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    def _init_transparency(self) -> dict:
        return {
            "session_id": self.session_id,
            "afo": {"verdict_synthesized": False},
            "rol_agents": [],
            "forense_agents": [],
            "ssm": {"activated": False, "reason": None,
                    "scale": None, "social_verdict": None},
            "budget": {},
        }

    def _log(self, msg: str):
        ts = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[TT {self.session_id}] {ts} — {msg}")
