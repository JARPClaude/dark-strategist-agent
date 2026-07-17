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

from schema import RuntimeContext, AgentVerdictOutput, UnifiedVerdictOutput, Finding, compute_confidence, should_escalate
from archetype_lenses import select_lenses, build_lens_directive
from context_builder import describe_domain_resolution
from prompt_engine import PromptEngine
from budget_controller import BudgetController
from sub_agent_spawner import SubAgentSpawner
from notifier import SlackNotifier, GitHubNotifier
from sheets_logger import SheetsLogger
from ssm import SimulacionSocialMasiva
from retriever import build_agent_context, load_corpus, load_corpus_files, overlap_score


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
        self.engine = PromptEngine(prompts_dir=config.get("prompts_dir", "./prompts"))
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
        #--- v3.10.0: BYO per-case corpus overrides; v3.8.0 map gancho is fallback (empty -> no-op).
        _byo = getattr(ctx, "corpus_paths", None)
        self._active_corpus = (load_corpus_files(_byo) if _byo
                               else load_corpus(getattr(ctx, "corpus", None)))
        #--- P4 (v3.14.0): external signals = distinct time-sensitive EVIDENCE channel (BYO only).
        #--- v3.15.0: keep a path-tagged view for provenance; the agent feed (_active_signals)
        #--- is the SAME passage list, just projected -> byte-identical to the P4 feed.
        _sig_paths = getattr(ctx, "signals_paths", None) or []
        if isinstance(_sig_paths, str):
            _sig_paths = [_sig_paths]
        _tagged = []
        for _p in _sig_paths:
            #--- LW-3: signals load per-line (txt_atomic_lines) so consecutive observations
            #--- are individually addressable for provenance; corpus load stays paragraph-split.
            for _passage in load_corpus_files(_p, txt_atomic_lines=True):
                _tagged.append((_p, _passage))
        self._active_signals_tagged = _tagged
        self._active_signals = [_passage for _, _passage in _tagged]
        self._transparency["signals"] = {"active": bool(self._active_signals),
                                         "count": len(self._active_signals),
                                         "provenance": []}
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
        self.budget.check_context_budget(
            len(rol_simulation_summary), label="Rol->Forense handoff"
        )

        # ── Layer 2: Agentes Forenses ──────────────────────────────────────
        self._log(f"Layer 2: Launching {len(ctx.forense_agents)} Agentes Forenses...")
        forense_outputs = self._run_forense_layer(document, ctx, rol_simulation_summary)
        self._transparency["forense_agents"] = [
            {"id": f["agent_id"], "role": f["role"],
             "verdict": f.get("preliminary_verdict", "UNKNOWN")}
            for f in forense_outputs
        ]
        for f in forense_outputs:
            for sa in f.get("sub_agents_used", []):
                if not isinstance(sa, dict):
                    continue
                bucket = "permanent" if sa.get("type") == "PERMANENT" else "temporary"
                self._transparency["sub_agents"][bucket].append(sa.get("unit", "UNKNOWN"))

        # ── Synthesis ──────────────────────────────────────────────────────
        self._log("Synthesizing all outputs...")
        all_outputs = rol_outputs + forense_outputs
        unified = self._synthesize(document, ctx, all_outputs)
        unified, all_outputs = self._maybe_escalate(document, ctx, all_outputs, unified)
        #--- LW-7 (v3.23.0): fail-closed collapse guard. BINDING verdict-path step (distinct
        #--- from the NON-BINDING confidence layer). Overrides the all-clear verdict when zero
        #--- agents contributed. After escalation so it reflects final coverage; cannot mask a
        #--- real INVIABLE (>=1 FATAL needs >=1 agent).
        unified = self._apply_collapse_guard(unified)
        self._transparency["afo"]["verdict_synthesized"] = True
        #--- Provenance (v3.15.0): post-verdict, NON-BINDING attribution of each finding to the
        #--- external signal passage it most overlaps. Reads the FINAL verdict, writes only the
        #--- report -> structurally cannot alter final_verdict (same independence as P4).
        self._transparency["signals"]["provenance"] = self._attribute_signal_provenance(unified)

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
                    agent_id, role, ctx, rol_simulation,
                    handoff_window=self.config.get("tribunal", {}).get("handoff_window", 8000)
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
                        {"domain": ctx.domain, "session_id": self.session_id}, corpus=self._active_corpus
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
            ctx, all_outputs, ctx.tribunal_label, self.session_id,
            synthesis_window=self.config.get("tribunal", {}).get("synthesis_window", 1500)
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
            uvo = UnifiedVerdictOutput(**data)
            return self._apply_confidence(uvo, all_outputs)
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

        uvo = UnifiedVerdictOutput(
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
        return self._apply_confidence(uvo, all_outputs)

    # ─── Helpers ──────────────────────────────────────────────────────────────

    @staticmethod
    def _norm_title(s) -> str:
        return " ".join(str(s).lower().split())

    COLLAPSE_VERDICT = "INDETERMINATE — TRIBUNAL COLLAPSE"

    def _apply_collapse_guard(self, unified: UnifiedVerdictOutput) -> UnifiedVerdictOutput:
        """LW-7: fail-closed gate for a full tribunal collapse.

        When zero agents contributed (agents_consulted==0, grounded to non-errored
        outputs by _apply_confidence/LW-5), NO analysis occurred, so the severity
        table empty-findings branch (SOLID UNDER PRESSURE, the all-clear) is
        misleading. This BINDING verdict-path step withholds the verdict instead of
        failing open. Distinct from the confidence/escalation layers (NON-BINDING),
        which report LOW / collapse but never change final_verdict. Cannot mask a real
        adverse verdict: >=1 FATAL (INVIABLE) requires >=1 contributing agent, so the
        guard only ever fires over a genuinely empty analysis. Idempotent.
        """
        if unified.agents_consulted == 0:
            unified.final_verdict = self.COLLAPSE_VERDICT
            unified.verdict_reasoning = (
                "Zero agent coverage; no analysis was performed (full tribunal "
                "collapse). Verdict withheld (fail-closed); rerun once agent "
                "connectivity is restored."
            )
        return unified

    def _maybe_escalate(self, document, ctx, all_outputs, unified):
        """
        P1 (v3.12.0) -- confidence-gated escalation. If confidence is LOW and agent budget
        remains, run a bounded extra forensic pass on the verdict-driving findings,
        re-synthesize, and recompute confidence. NON-BINDING: never alters final_verdict
        (severity-driven). Confidence may stay LOW (honest) if still uncorroborated.
        Capped at tribunal.max_escalation_rounds.
        """
        tcfg = self.config.get("tribunal", {})
        enabled = tcfg.get("escalation_enabled", True)
        max_rounds = tcfg.get("max_escalation_rounds", 1)
        max_esc_agents = tcfg.get("max_escalation_agents", 2)
        esc = {"triggered": False, "rounds": 0,
               "confidence_before": unified.confidence,
               "confidence_after": unified.confidence, "reason": None}
        rounds = 0
        while should_escalate(unified.confidence, rounds, max_rounds,
                              self.budget.remaining_agents(), enabled,
                              agent_coverage=unified.agents_consulted):
            self._log("Confidence LOW -- escalation round %d (agents left: %d)"
                      % (rounds + 1, self.budget.remaining_agents()))
            extra = self._run_escalation_round(document, ctx, unified, rounds + 1, max_esc_agents)
            if not extra:
                esc["reason"] = "no agent budget for escalation"
                break
            all_outputs = all_outputs + extra
            unified = self._synthesize(document, ctx, all_outputs)
            rounds += 1
        if rounds == 0 and esc["reason"] is None:
            #--- LW-6: distinguish zero-coverage collapse from disabled/no-budget (honest reason).
            if unified.confidence != "LOW":
                esc["reason"] = "confidence not LOW -- no escalation needed"
            elif unified.agents_consulted == 0:
                esc["reason"] = "zero agent coverage -- escalation cannot help (tribunal collapse)"
            else:
                esc["reason"] = "escalation disabled or no budget"
        esc.update({"triggered": rounds > 0, "rounds": rounds,
                    "confidence_after": unified.confidence,
                    "lenses": sorted({o.get("lens") for o in all_outputs
                                      if isinstance(o, dict) and o.get("escalation") and o.get("lens")})})
        self._transparency["escalation"] = esc
        return unified, all_outputs

    def _run_escalation_round(self, document, ctx, unified, round_no, max_esc_agents):
        """Bounded extra forensic pass over the verdict-driving findings. Each FOR-ESC-*
        agent is driven by a distinct archetype lens (P2 -- abstract adversarial
        perspectives, never real persons). Distinct agent ids (FOR-ESC-*) so cross-agent
        corroboration counts them as independent. Degrades gracefully (errors captured,
        lens optional) so offline/no-API runs never crash."""
        n_esc = min(self.budget.remaining_agents(), max(0, int(max_esc_agents)))
        roles = (ctx.forense_agents or [])[:n_esc]
        if not roles:
            return []
        if unified.fatal_findings:
            driving = unified.fatal_findings
        elif unified.serious_findings:
            driving = unified.serious_findings
        elif unified.moderate_findings:
            driving = unified.moderate_findings
        else:
            driving = unified.latent_findings
        focus = " | ".join(getattr(f, "title", "") for f in driving[:5]) or "low-corroboration verdict"
        lenses = select_lenses(len(roles))  #--- P2: one archetype lens per escalation agent (deterministic)
        results = []
        with ThreadPoolExecutor(max_workers=max(1, len(roles))) as executor:
            futures = {}
            for i, role in enumerate(roles):
                agent_id = "FOR-ESC-%s" % str(i + 1).zfill(2)
                lens = lenses[i] if i < len(lenses) else None
                directive = build_lens_directive(lens, round_no, focus)
                prompt = self.engine.build_forense_prompt(
                    agent_id, role, ctx, directive,
                    handoff_window=self.config.get("tribunal", {}).get("handoff_window", 8000)
                )
                futures[executor.submit(self._call_agent, agent_id, "FORENSE", role, prompt, document)] = (agent_id, role, lens)
            for future in as_completed(futures):
                agent_id, role, lens = futures[future]
                lens_id = (lens or {}).get("id")
                try:
                    result = future.result(timeout=120)
                    result["role"] = role
                    result["escalation"] = True
                    result["lens"] = lens_id
                    results.append(result)
                    self._log("%s (escalation, lens=%s) -- verdict: %s" % (agent_id, lens_id, result.get("preliminary_verdict", "N/A")))
                except Exception as e:
                    self._log("%s (escalation, lens=%s) failed: %s" % (agent_id, lens_id, e))
                    results.append({"agent_id": agent_id, "role": role,
                                    "agent_type": "FORENSE", "error": str(e), "escalation": True, "lens": lens_id})
        return results

    def _apply_confidence(self, unified, all_outputs):
        """
        v3.11.0 -- recompute confidence deterministically (NON-BINDING; never
        touches final_verdict). Grounds agents_consulted and multi_agent_confirmed
        from cross-agent corroboration, then derives confidence via compute_confidence.

        LW-2: corroboration is similarity-based, not exact-title. Two independent agents
        rarely word a finding's title identically, AND the synthesizer rewrites the unified
        titles -- so exact (severity, title) matching recorded "Confirmed by 2+: 0" even
        under unanimous consensus, biasing confidence LOW. We now match on title+evidence
        token overlap (rag.corroboration_min_overlap, default 4) with same severity
        required, keeping the legacy exact-title match as a floor (strict superset -> no
        regression). driver_corroborated compares the SYNTHESIZER finding against the
        corroborated RAW findings by the same similarity, crossing the synthesizer<->raw
        title gap. Still NON-BINDING / deterministic / post-verdict: writes only
        confidence + multi_agent_confirmed, never final_verdict or any Finding.
        """
        #--- LW-5: count only agents that actually contributed usable output. A fully-
        #--- collapsed tribunal (every output carries "error", no findings) must NOT report
        #--- HIGH confidence over zero analysis. compute_confidence's clean-verdict HIGH
        #--- branch (driver_finding_count==0) is legitimate ONLY when healthy agents
        #--- genuinely found nothing; errored agents were not "consulted". NON-BINDING:
        #--- agents_consulted feeds confidence only, never final_verdict.
        contributing = [o for o in all_outputs if isinstance(o, dict) and "error" not in o]
        unified.agents_consulted = len(contributing)
        min_ov = self.config.get("rag", {}).get("corroboration_min_overlap", 4)

        #--- LW-2: per-finding signal = title + evidence. Evidence anchors to the document
        #--- (objective), discriminating "same defect" from shared title scaffolding
        #--- ("missing X clause" vs "missing Y clause") far better than the title alone.
        def _blob(title, evidence):
            return ((title or "") + " " + (evidence or "")).strip()

        def _similar(sev_a, t_a, b_a, sev_b, t_b, b_b):
            #--- same severity required; legacy exact-title floor OR token-overlap >= min_ov.
            if sev_a != sev_b:
                return False
            if t_a and t_a == t_b:
                return True
            return overlap_score(b_a, b_b) >= min_ov

        #--- Raw findings with agent provenance (raw title space, from all_outputs).
        raw = []  #--- (agent, sev, norm_title, blob)
        for i, out in enumerate(all_outputs):
            agent = out.get("agent_id", "_idx%d" % i) if isinstance(out, dict) else "_idx%d" % i
            findings = out.get("findings", []) if isinstance(out, dict) else []
            local = {}  #--- dedupe within one agent by (sev, norm_title); keep first blob
            for f in findings:
                if not isinstance(f, dict):
                    continue
                sev = (f.get("severity") or "").upper()
                title = self._norm_title(f.get("title", ""))
                if not title:
                    continue
                key = (sev, title)
                if key not in local:
                    local[key] = _blob(f.get("title", ""), f.get("evidence", ""))
            for (sev, title), blob in local.items():
                raw.append((agent, sev, title, blob))

        #--- Cross-agent corroboration: a raw finding is corroborated iff another agent has
        #--- a similar one (same severity, exact-title OR overlap>=min_ov).
        corroborated_idx = set()
        for a in range(len(raw)):
            ag_a, sev_a, t_a, b_a = raw[a]
            for b in range(len(raw)):
                if a == b:
                    continue
                ag_b, sev_b, t_b, b_b = raw[b]
                if ag_a != ag_b and _similar(sev_a, t_a, b_a, sev_b, t_b, b_b):
                    corroborated_idx.add(a)
                    break

        #--- multi_agent_confirmed (report-only; len() is what compute_confidence cares about).
        #--- Greedy single-link clustering over corroborated raws -> one entry per distinct
        #--- confirmed defect (deterministic: stable raw order, first member is representative;
        #--- a new member joins a cluster if it is similar to ANY existing member).
        clusters = []  #--- each: dict(sev, members:[(t,b)], agents:set, repr_title)
        for a in sorted(corroborated_idx):
            ag, sev, t, b = raw[a]
            placed = False
            for cl in clusters:
                if cl["sev"] == sev and any(
                    _similar(sev, t, b, sev, mt, mb) for (mt, mb) in cl["members"]
                ):
                    cl["members"].append((t, b))
                    cl["agents"].add(ag)
                    placed = True
                    break
            if not placed:
                clusters.append({"sev": sev, "members": [(t, b)],
                                 "agents": {ag}, "repr_title": t})
        unified.multi_agent_confirmed = sorted(
            "%s: %s" % (cl["sev"], cl["repr_title"])
            for cl in clusters if len(cl["agents"]) >= 2
        )

        #--- Verdict-driving tier (synthesizer findings).
        if unified.fatal_findings:
            driving, tier_sev = unified.fatal_findings, "FATAL"
        elif unified.serious_findings:
            driving, tier_sev = unified.serious_findings, "SERIOUS"
        elif unified.moderate_findings:
            driving, tier_sev = unified.moderate_findings, "MODERATE"
        elif unified.latent_findings:
            driving, tier_sev = unified.latent_findings, "LATENT"
        else:
            driving, tier_sev = [], None

        #--- LW-2: cross the synthesizer<->raw gap. A driving (synthesizer) finding is
        #--- corroborated if it is similar to ANY corroborated RAW finding of the same
        #--- severity -> exact-title floor OR title+evidence overlap. The synthesizer
        #--- rewrites titles but preserves evidence substance, so the blob bridges the gap.
        corr_raw = [raw[a] for a in corroborated_idx]
        driver_corroborated = False
        if tier_sev:
            for f in driving:
                ft = self._norm_title(getattr(f, "title", ""))
                fb = _blob(getattr(f, "title", ""), getattr(f, "evidence", ""))
                if any(_similar(tier_sev, ft, fb, sev_r, t_r, b_r)
                       for (_ag, sev_r, t_r, b_r) in corr_raw):
                    driver_corroborated = True
                    break

        unresolved = sum(1 for c in unified.conflicts_detected if "UNRESOLVED" in str(c).upper())

        unified.confidence = compute_confidence(
            agents_consulted=unified.agents_consulted,
            driver_corroborated=driver_corroborated,
            driver_finding_count=len(driving),
            unresolved_conflicts=unresolved,
        )
        return unified

    def _agent_doc_context(self, document, query_text):
        #--- v3.8.0: RAG-assisted feed; non-breaking fallback to [:N] inside.
        rag = self.config.get("rag", {})
        return build_agent_context(
            document, query_text,
            window=self.config.get("tribunal", {}).get("doc_window", 4000),
            chunk_size=rag.get("chunk_size", 1000),
            chunk_overlap=rag.get("chunk_overlap", 150),
            doc_top_k=rag.get("doc_top_k", 6),
            corpus=self._active_corpus,
            corpus_top_k=rag.get("corpus_top_k", 3),
            signals=getattr(self, "_active_signals", None),
            signals_top_k=rag.get("signals_top_k", 3),
        )

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
                        "content": f"Analyze this document:\n\n{self._agent_doc_context(document, role)}"}]
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
        """
        Builds the Rol->Forense handoff. Full-fidelity: preserves every
        audit-relevant field with agent provenance. No truncation of structured
        fields (telephone-game fix, v3.4 R1 FUGA#1). The Forense layer cannot
        audit assumptions or demanded information it never receives.
        """
        blocks = []
        for r in rol_outputs:
            aid = r.get("agent_id", "ROL-?")
            role = r.get("role", "Unknown Role")
            stance = r.get("stance", "NEUTRAL")
            stance_reasoning = r.get("stance_reasoning", "")
            perspective = r.get("role_perspective", "")
            concerns = r.get("primary_concerns", [])
            action = r.get("intended_action", "Not specified")
            assumptions = r.get("assumptions_made", [])
            demanded = r.get("information_demanded", [])

            block = [f"[{aid}] {role} — stance={stance}"]
            if stance_reasoning:
                block.append(f"  stance_reasoning: {stance_reasoning}")
            if perspective:
                block.append(f"  perspective: {perspective}")
            if concerns:
                block.append("  concerns: " + " | ".join(concerns))
            block.append(f"  intended_action: {action}")
            if assumptions:
                block.append("  assumptions_made: " + " | ".join(assumptions))
            if demanded:
                block.append("  information_demanded: " + " | ".join(demanded))
            blocks.append("\n".join(block))
        return "\n\n".join(blocks)

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
            f"Confidence: {unified.confidence}  (auditability signal: corroboration/conflict, NOT a success probability or efficiency guarantee)",
            f"Reasoning:  {unified.verdict_reasoning}",
            f"{'='*60}",
        ]
        return "\n".join(lines)

    def _attribute_signal_provenance(self, unified: UnifiedVerdictOutput) -> list:
        """Deterministic, post-verdict provenance: attribute each finding to the external
        signal passage it shares the most tokens with (v3.15.0).

        NON-BINDING auditability hint, NOT causal proof and NEVER a verdict input. It reads
        the already-final `unified` and returns plain records for the transparency report;
        it mutates neither the verdict nor any Finding. Empty when there are no signals or
        when the best overlap is below `rag.provenance_min_overlap` (default 3) — we prefer
        NOT attributing over attributing on stopword noise.
        """
        tagged = getattr(self, "_active_signals_tagged", None) or []
        if not tagged:
            return []
        min_ov = self.config.get("rag", {}).get("provenance_min_overlap", 3)
        tiers = [("FATAL", unified.fatal_findings),
                 ("SERIOUS", unified.serious_findings),
                 ("MODERATE", unified.moderate_findings),
                 ("LATENT", unified.latent_findings)]
        out = []
        for sev, findings in tiers:
            for f in findings:
                ftext = (f.evidence or "") + " " + (f.description or "")
                best_i, best_sc = -1, 0
                for i, (_path, passage) in enumerate(tagged):
                    sc = overlap_score(ftext, passage)
                    if sc > best_sc:
                        best_sc, best_i = sc, i
                if best_i >= 0 and best_sc >= min_ov:
                    path, passage = tagged[best_i]
                    snippet = " ".join((passage or "").split())[:80]
                    out.append({"severity": sev, "title": f.title,
                                "signal_index": best_i, "source": path,
                                "overlap": best_sc, "snippet": snippet})
        return out

    def _build_transparency_report(self, ctx: RuntimeContext, duration: float,
                                   ssm_reason: str,
                                   unified: UnifiedVerdictOutput) -> str:
        t = self._transparency
        from slop_filter import score_prose
        _slop_src = (unified.verdict_reasoning or "") + " " + " ".join(
            (f.title or "") + " " + (f.description or "")
            for f in (unified.fatal_findings + unified.serious_findings
                      + unified.moderate_findings + unified.latent_findings))
        slop = score_prose(_slop_src)
        #--- LW-8 (v3.24.0): declare HOW the domain was decided. A filename-driven
        #--- resolution must never be readable as a document-driven one, and the
        #--- General sink (no catalog -> no LG08/LG09) must never be silent.
        domain_res = describe_domain_resolution(ctx)
        rol_lines = "\n".join([
            f"    {a['id']}  {a['role'][:45]}  stance={a['stance']}"
            for a in t.get("rol_agents", [])
        ])
        for_lines = "\n".join([
            f"    {a['id']}  {a['role'][:45]}  verdict={a['verdict']}"
            for a in t.get("forense_agents", [])
        ])
        sub_perm = sorted(set(t.get("sub_agents", {}).get("permanent", [])))
        sub_temp = sorted(set(t.get("sub_agents", {}).get("temporary", [])))
        perm_lines = "\n".join([f"    {u}" for u in sub_perm]) if sub_perm else "    None"
        temp_lines = "\n".join([
            f"    {u}  ← SUB_AGENT_EXPANSION_RECOMMENDED dispatched"
            for u in sub_temp]) if sub_temp else "    None"
        budget = t.get("budget", {})
        escalation = t.get("escalation", {})
        _prov = t.get("signals", {}).get("provenance", []) or []
        prov_lines = "\n".join([
            f"    [{p['severity']}] {p['title'][:50]}  <- signal #{p['signal_index']} "
            f"({p['source']}, overlap={p['overlap']})  \"{p['snippet']}\""
            for p in _prov
        ]) if _prov else "    none"
        ssm_block = (
            f"\n  STATUS:  ACTIVATED | Scale: {t['ssm']['scale']} | "
            f"Social: {t['ssm'].get('social_verdict', 'See SSM report')}"
            if t["ssm"]["activated"]
            else f"\n  STATUS:  NOT ACTIVATED — {ssm_reason}"
        )

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DARK STRATEGIST v3.23.0 — TRANSPARENCY REPORT
Session: DS-{self.session_id} | Duration: {round(duration,1)}s
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AGENTE FORENSE ORQUESTADOR (AFO)
  Domain:      {ctx.domain} / {ctx.subscenario}
  Resolved by: {domain_res}
  Regime:      {ctx.regime} — {ctx.regime_description}
  Tribunal:    {ctx.tribunal_label}
  Synthesized: YES — VEREDICTO FORENSE UNIFICADO
  Ext.signals: {('ACTIVE — %d evidence passage(s) (non-binding)' % t['signals']['count']) if t.get('signals', {}).get('active') else 'none'}

TRIBUNAL TRANSVERSAL — LAYER 1: AGENTES DE ROL
  (Simulated the domain environment)
{rol_lines or '    None'}

TRIBUNAL TRANSVERSAL — LAYER 2: AGENTES FORENSES
  (Audited the simulation + document)
{for_lines or '    None'}

SUB-AGENTES FORENSES (N2 — spawned by Forense layer)
  Permanent:
{perm_lines}
  Temporary:
{temp_lines}

VERDICT SUMMARY
  🔴 FATAL:    {len(unified.fatal_findings)}
  🟠 SERIOUS:  {len(unified.serious_findings)}
  🟡 MODERATE: {len(unified.moderate_findings)}
  🔵 LATENT:   {len(unified.latent_findings)}
  Confirmed by 2+ agents: {len(unified.multi_agent_confirmed)}
  Conflicts resolved:     {len(unified.conflicts_detected)}

SIGNAL PROVENANCE (v3.15.0 — heuristic, NON-BINDING; likely originating signal, not causal proof)
{prov_lines}

CONFIDENCE (deterministic, NON-BINDING -- auditability signal, not success/efficiency)
  Level:       {unified.confidence}
  Escalation:  {'YES' if escalation.get('triggered') else 'NO'} | rounds: {escalation.get('rounds', 0)} | {escalation.get('confidence_before', 'N/A')} -> {escalation.get('confidence_after', 'N/A')}{(' | ' + str(escalation.get('reason'))) if escalation.get('reason') else ''}{(' | lenses: ' + ', '.join(escalation.get('lenses') or [])) if escalation.get('lenses') else ''}

SIMULACIÓN SOCIAL MASIVA (SSM){ssm_block}

BUDGET CONSUMED
  Total calls: {budget.get('total_calls',0)}/{budget.get('max_calls',30)} ({budget.get('budget_used_percent',0)}%)
  Breakdown:   {budget.get('calls_made',{})}

PROSE QUALITY (stop-slop — advisory, score-only)
  Score: {slop['score']}/{slop['max']} (threshold {slop['threshold']}) → {slop['flag']}
  Dimensions: {slop['dimensions']}

FINAL VERDICT: {unified.final_verdict} | Confidence: {unified.confidence} (non-binding; not a success/efficiency guarantee)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    def _init_transparency(self) -> dict:
        return {
            "session_id": self.session_id,
            "afo": {"verdict_synthesized": False},
            "rol_agents": [],
            "forense_agents": [],
            "sub_agents": {"permanent": [], "temporary": []},
            "ssm": {"activated": False, "reason": None,
                    "scale": None, "social_verdict": None},
            "budget": {},
            "escalation": {},
            "signals": {"active": False, "count": 0},
        }

    def _log(self, msg: str):
        ts = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[TT {self.session_id}] {ts} — {msg}")
