# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [2.8.0] — 2026-05-13

### Major Release — Agente Forense Orquestador + Tribunal Adversarial

This release introduces the **Agente Forense Orquestador (AFO)** and the full **Tribunal Adversarial** architecture — transforming Dark Strategist from a single-agent auditor into a hierarchical multi-agent forensic system.

#### Architecture — 3-Level Hierarchy

```
N0 — Agente Forense Orquestador (AFO)
      Directs, consolidates, emits unified verdict

N1 — Agentes Forenses (parallel, blind to each other)
      1 / 3 / 5 / 7 depending on Swarm Activation Score

N2 — Sub-agentes Forenses
      Permanent: UNIT-QUANT, UNIT-INQUISITOR, UNIT-TECH,
                 UNIT-PSYCH, UNIT-GEO, UNIT-MARKET,
                 UNIT-COMPLIANCE, UNIT-BIO
      Temporary: created dynamically for unknown domains
                 → triggers SUB_AGENT_EXPANSION_RECOMMENDED
```

#### Swarm Activation Score (auto-sizing)

| Initial Verdict | Tribunal Mode | Agents |
|----------------|--------------|--------|
| SOLID / VIABLE WITH ADJUSTMENTS | SINGLE | 1 |
| VIABLE WITH CRITICAL CORRECTIONS | TRIBUNAL_LIGHT | 3 |
| INVIABLE | TRIBUNAL_FULL | 5 |
| INVIABLE + War Room | TRIBUNAL_MAX | 7 |

#### New Files

1. **`orchestrator/tribunal.py`** — AgenteForenseOrquestador class. Full pipeline: routing → swarm score → parallel N1 execution → N2 spawning → synthesis → notifications → logging.

2. **`orchestrator/budget_controller.py`** — BudgetController class. Controls max_agents (7), max_calls_total (30), max_n2_per_n1 (3). Alerts at 80% budget. Blocks excess calls gracefully.

3. **`orchestrator/sub_agent_spawner.py`** — SubAgentSpawner class. Auto-detects N2 needs via signal words. Spawns permanent UNITs or temporary sub-agents. Temporary sub-agents trigger SUB_AGENT_EXPANSION_RECOMMENDED via Slack + GitHub + Sheets.

4. **`orchestrator/verdict_synthesizer.py`** — VerdictSynthesizer class. Consolidates all N1 reports (+ N2 findings) into VEREDICTO FORENSE UNIFICADO. Resolves conflicts toward highest severity. Applies Verdict Decision Table mechanically.

#### Updated Files

- **`orchestrator/main.py`** — New flags: `--tribunal` (activate tribunal mode), `--agents 1|3|5|7` (force size). Tribunal mode auto-sizes via Swarm Activation Score if `--agents` not specified.
- **`orchestrator/config.example.json`** — New `tribunal` section: max_agents, max_calls_total, max_n2_per_n1, alert_at_percent.

#### Usage

```bash
# Single mode (default)
python main.py --document doc.txt

# Tribunal auto-size (Swarm Activation Score decides)
python main.py --document doc.txt --tribunal

# Tribunal forced size
python main.py --document doc.txt --tribunal --agents 5

# Budget + routing summary
python main.py --document doc.txt --tribunal --verbose
```

#### Pending — v2.8 Roadmap

- [ ] example_04 — COMPARATIVE MODE worked example
- [ ] example_05 — OPTIMIZATION MODE worked example
- [ ] UNIT-PSYCH extended bias catalog
- [ ] Looker Studio dashboard template
- [ ] Phase 3 — Simulación Social Masiva (SSM) — roadmap planned

---

## [2.7.0] — 2026-05-12

### Major Release — Autonomous Router + 11 Domain Prompts + Python Infrastructure

12 new prompts (router + 11 domains). orchestrator/ and infrastructure/ folders.
UNKNOWN_DOMAIN protocol with Slack + GitHub + Sheets auto-notification.

---

## [2.6.1] — 2026-05-06

### Patch — Trading & Legal Domain Variants

system_prompt_trading.md + system_prompt_legal.md.

---

## [2.6.0] — 2026-05-05

### Major — SAT Intelligence Doctrine + 4 Audit Skills

sat_intelligence_doctrine.md + KAC + ACH + Deception Detection + Verdict Verification.

---

## [2.5.1] — 2026-04-25

§4.22 Industry & Business Taxonomy.

---

## [2.5.0] — 2026-04-25

MVP_THRESHOLD | Operational Modes | COMPARATIVE | OPTIMIZATION | FAST_TRACK | UNIT-PSYCH.

---

## [2.4.0] — 2026-04-24

MIT License. §4.14 Governance. §4.15 Deprecation.

---

## [2.3.0] — 2026-04-21

ES/EN Map. War Room threshold. Geofence. VERSION_TRACK. UNIT-BIO. REPORT_ID.

---

## [2.2.0] — 2026-04-20

Deterministic verdict. NEGLECT_DETECTED. §4.13 Activation Matrix.

---

## [2.1.0] — 2026-04-20

War Room. Sectoral Agnosticism. Micro-Agent Catalog. Geofence. Rules 09/10.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, Blocks 0–6.
