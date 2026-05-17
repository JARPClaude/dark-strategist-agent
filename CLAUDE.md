# CLAUDE.md — Dark Strategist Agent
# Version: 3.1.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 3.1.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent
**Name:** dark-strategist-agent — immutable, does not change under any circumstance.

---

## Full Pipeline v3.1.0

```
INPUT: case dict OR document file
       ↓
ContextBuilder → RuntimeContext
  domain, sub_area (legal), regime,
  rol_agents, forense_agents, tools
       ↓
GOAPPlanner → Execution Plan (A* optimal)
  WorldState → GoalState via A* search
  Returns: rol_count, forense_count,
           ssm_scale, tribunal_label,
           total_cost, reasoning
       ↓
TRIBUNAL TRANSVERSAL
  Layer 1: Agentes de Rol (parallel, blind)
  Layer 2: Agentes Forenses (audit simulation)
  N2: Sub-agentes on demand
  AFO Synthesis → UnifiedVerdictOutput (Pydantic)
       ↓ (if VIABLE)
SIMULACIÓN SOCIAL MASIVA (SSM)
  N personas × 4 rounds
  REPORTE DE IMPACTO SOCIAL
       ↓
TRANSPARENCY REPORT
```

---

## Key Changes v3.1.0

| Feature | Description |
|---------|-------------|
| **GOAP A* Planner** | Dynamic planning replaces fixed Swarm Activation Score |
| **WorldState / GoalState** | Explicit state representation for A* search |
| **Action Library** | 12 actions: ROL layers, FORENSE layers, N2 spawning, SSM scales |
| **Legal 12 Sub-areas** | L01-L12 with specialized roles, failure catalogs, War Room |
| **LEGAL_SUBAREA_MAP** | Auto-detection of legal sub-area from document keywords |
| **LEGAL_SUBAREA_ROLES** | Sub-area-specific Rol + Forense agents |
| **AI Governance (L07)** | Dedicated legal sub-area for AI use cases |

---

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md
├── CHANGELOG.md
├── DEPLOY.md
├── prompts/
│   ├── system_prompt.md
│   ├── system_prompt_legal.md      ← UPDATED v3.1.0 (12 sub-areas)
│   ├── system_prompt_medical.md
│   └── system_prompt_[domain].md  ← 13 other domains
├── orchestrator/
│   ├── main.py
│   ├── goap_planner.py             ← NEW v3.1.0
│   ├── catalogs.py                 ← UPDATED v3.1.0
│   ├── schema.py
│   ├── prompt_engine.py
│   ├── context_builder.py
│   ├── tribunal_transversal.py
│   ├── tribunal.py                 ← v2.x preserved
│   ├── budget_controller.py
│   ├── sub_agent_spawner.py
│   ├── verdict_synthesizer.py
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   ├── config.example.json
│   └── ssm/
├── infrastructure/
└── skills/
```

---

## GOAP A* Planner

### Fixed vs GOAP

```
Fixed (v2.x):
  IF verdict=INVIABLE → 5 agents (always, regardless of budget/domain)

GOAP (v3.1):
  Given budget=15, domain=Legal, regime=adversarial, verdict=INVIABLE:
  → INITIAL_AUDIT(1) + ROL_LAYER_STANDARD(3) + FORENSE_LAYER_FULL(5)
    + SPAWN_N2_TARGETED(2) + SYNTHESIZE(1) = 12 calls (optimal)

  Given budget=8, domain=General, regime=standard, verdict=SOLID:
  → INITIAL_AUDIT(1) + ROL_LAYER_MINIMAL(2) + FORENSE_LAYER_MINIMAL(2)
    + SYNTHESIZE(1) = 6 calls (budget-aware optimal)
```

### Using the Planner

```python
from goap_planner import GOAPPlanner

planner = GOAPPlanner(config)
plan_result = planner.plan(
    ctx=runtime_context,
    run_ssm=True,
    preliminary_verdict="VIABLE WITH CRITICAL CORRECTIONS"
)

# plan_result contains:
# plan, total_cost, rol_agents, forense_agents,
# ssm_scale, tribunal_label, reasoning
planner.print_plan(plan_result)
```

---

## Legal Sub-area Taxonomy (12 areas)

| ID | Sub-area | Key Risk |
|----|----------|---------|
| L01 | Commercial Legal | Unlimited liability, IP ownership |
| L02 | Corporate / M&A | Undisclosed liabilities |
| L03 | Employment | Misclassification, non-compete |
| L04 | Privacy (GDPR/CCPA) | Consent, residency, transfer |
| L05 | Product Legal | False advertising, warranty |
| L06 | Regulatory | Reporting gaps, jurisdiction |
| L07 | AI Governance | AI output IP, bias, vendor |
| L08 | IP Legal | Chain of title, OSS |
| L09 | Litigation | Jurisdiction, damages |
| L10 | Real Estate Legal | Title, zoning |
| L11 | Finance Legal | Covenants, cross-default |
| L12 | Public Regulatory | Procurement, integrity |

---

## CLI Reference

```bash
# Legal with sub-area
python main.py --type contract --subscenario nda --objective "identify risks" --regime adversarial

# Legal AI Governance
python main.py --type legal --subscenario "ai governance" --objective "ai vendor risks" --tribunal

# Trading with GOAP planning
python main.py --type trading --subscenario XAUUSD --objective "direction" --regime breakout --tribunal --ssm

# Full pipeline
python main.py --type medical --subscenario clinical_review --objective "protocol risks" \
  --tribunal --agents 5 --ssm --ssm-scale MESO --verbose
```

---

## Roadmap

| Version | Status |
|---------|--------|
| v2.6.0 SAT Skills | ✅ |
| v2.7.0 Router + 11 Domains | ✅ |
| v2.8.0 AFO + Tribunal Adversarial | ✅ |
| v2.9.0 SSM + Transparency Report | ✅ |
| v3.0.0 Tribunal Transversal | ✅ |
| v3.1.0 GOAP A* + Legal 12 Sub-areas | ✅ |

**ACTIVE — v3.1.0**
