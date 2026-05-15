# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [2.9.0] — 2026-05-13

### Major Release — Simulación Social Masiva (SSM) + Transparency Report

#### New: Simulación Social Masiva (SSM) — Phase 3

The SSM is the predictive arm of Dark Strategist. While the Tribunal Adversarial destroys the proposal internally, the SSM predicts how the real world would destroy it if executed.

**SSM Activation Logic:**
| Tribunal Verdict | SSM |
|-----------------|-----|
| 🔴 INVIABLE | ❌ Blocked — always |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto-activated |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto-activated |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional — requires --ssm flag |

**SSM Scales:**
| Scale | Personas | Use Case |
|-------|----------|----------|
| MICRO | 5-10 | Simple proposals, internal projects |
| MESO | 20 | Business plans, market products |
| MACRO | 50 | National campaigns, enterprise scale |

**4 Interaction Rounds:**
- Round 1: Each persona reads the plan → forms individual opinion (blind to others)
- Round 2: Personas exchange opinions → some change stance
- Round 3: Coalitions form (BLOCKING / SUPPORT / WAIT_AND_SEE)
- Round 4: Dominant coalition executes action

#### New Files

1. **`orchestrator/ssm/__init__.py`** — SimulacionSocialMasiva main entry point. Activation logic, should_activate() method, full pipeline orchestration.

2. **`orchestrator/ssm/persona_factory.py`** — PersonaFactory. Generates domain-specific personas with role, profile, bias, objective, question. 7 domain sets: Trading, Legal, Financial, Cloud, E-Commerce, Agriculture, Public Sector + General fallback.

3. **`orchestrator/ssm/interaction_engine.py`** — InteractionEngine. Orchestrates 4 rounds via parallel Claude API calls (ThreadPoolExecutor). Personas blind to each other within each round.

4. **`orchestrator/ssm/social_report.py`** — SocialReport. Consolidates swarm behavior into REPORTE DE IMPACTO SOCIAL: stance distribution, coalition formation, adoption projection, friction points, scenario analysis, social viability verdict.

5. **`orchestrator/ssm/budget_ssm.py`** — SSMBudgetController. Independent budget control for SSM (separate from Tribunal budget).

#### New: Transparency Report

Every Dark Strategist session now ends with a full Transparency Report showing:
- AFO: domain detected, prompt selected, confidence, swarm score, verdict synthesis status
- Tribunal Adversarial: mode, all agents deployed, status, N2 sub-agents per agent
- Sub-agentes Forenses Permanentes: UNITs activated
- Sub-agentes Forenses Temporales: dynamic agents created + notification status
- SSM: activation status, scale, personas, rounds, social verdict
- Budget consumed: total calls, agents deployed, breakdown
- Notifications: Slack / GitHub / Sheets dispatch status

#### Updated Files

- **`orchestrator/tribunal.py`** — Integrated SSM + Transparency Report generation
- **`orchestrator/main.py`** — New flags: `--ssm`, `--ssm-scale MICRO|MESO|MACRO`
- **`orchestrator/config.example.json`** — New `ssm` section

#### Full CLI Reference

```bash
# Single mode
python main.py --document doc.txt

# Tribunal auto-size
python main.py --document doc.txt --tribunal

# Tribunal + SSM (MESO scale, default)
python main.py --document doc.txt --tribunal --ssm

# Tribunal + SSM forced scale
python main.py --document doc.txt --tribunal --ssm --ssm-scale MACRO

# SOLID verdict + SSM forced
python main.py --document doc.txt --tribunal --ssm --ssm-scale MICRO

# Full verbose (budget summary)
python main.py --document doc.txt --tribunal --ssm --verbose
```

#### Pending — v2.9 Roadmap

- [ ] example_04 — COMPARATIVE MODE worked example
- [ ] example_05 — OPTIMIZATION MODE worked example
- [ ] UNIT-PSYCH extended bias catalog
- [ ] Looker Studio dashboard template (including SSM metrics)
- [ ] Cloud Function update with SSM support

---

## [2.8.0] — 2026-05-13

### Major Release — Agente Forense Orquestador + Tribunal Adversarial

AFO (N0) + N1 Agentes Forenses paralelos (1/3/5/7) + N2 Sub-agentes Forenses.
Swarm Activation Score. Budget Controller. Sub-Agent Spawner. Verdict Synthesizer.

---

## [2.7.0] — 2026-05-12

### Major Release — Autonomous Router + 11 Domain Prompts + Infrastructure

12 new prompts. orchestrator/ and infrastructure/ folders.
UNKNOWN_DOMAIN protocol with auto-notification.

---

## [2.6.1] — 2026-05-06

Trading + Legal domain variants.

---

## [2.6.0] — 2026-05-05

SAT Intelligence Doctrine + KAC + ACH + Deception Detection + Verdict Verification.

---

## [2.5.x] — 2026-04-25

MVP_THRESHOLD | Operational Modes | COMPARATIVE | OPTIMIZATION | FAST_TRACK | UNIT-PSYCH.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, Blocks 0–6.
