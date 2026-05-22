# CLAUDE.md — Dark Strategist Agent
# Version: 3.2.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 3.2.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent
**Name:** dark-strategist-agent — immutable, does not change under any circumstance.

---

## Full Pipeline v3.2.0

```
INPUT: case dict OR document file
       ↓
ContextBuilder → RuntimeContext
  domain, sub_area (legal), regime,
  rol_agents, forense_agents, tools
       ↓
GOAPPlanner → Execution Plan (A* optimal)
  WorldState → GoalState via A* search
       ↓
TRIBUNAL TRANSVERSAL
  Layer 1: Agentes de Rol (parallel, blind)
  Layer 2: Agentes Forenses (audit simulation)
  [SKILL: ADAPTIVE AUTONOMOUS DRIVE]
    → autonomous rounds if gaps detected
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

## Key Changes v3.2.0

| Feature | Description |
|---------|-------------|
| **Adaptive Autonomous Drive** | Skill that grants AFO autonomous expansion beyond initial prompt |
| **Marketing domain (P16)** | UNIT-MARKET primary. Rules MK1-MK4. CAC/ROAS/funnel audit. |
| **Operations domain (P17)** | UNIT-TECH primary. Rules OP1-OP4. Supply chain + SoD. |
| **Human Resources domain (P18)** | UNIT-COMPLIANCE primary. Rules HR1-HR4. Pay equity + labor law. |
| **Strategy domain (P19)** | UNIT-MARKET primary. Rules ST1-ST4. Competitive + assumption audit. |
| **Startup domain (P20)** | UNIT-QUANT primary. Rules SU1-SU5. PMF + unit economics. |
| **SKILLS_CATALOG** | New section in catalogs.py registering all 5 active skills. |

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
│   ├── system_prompt_legal.md      ← v3.1.0 (12 sub-areas)
│   ├── system_prompt_medical.md    ← v3.0.0
│   ├── system_prompt_marketing.md  ← NEW v3.2.0
│   ├── system_prompt_operations.md ← NEW v3.2.0
│   ├── system_prompt_hr.md         ← NEW v3.2.0
│   ├── system_prompt_strategy.md   ← NEW v3.2.0
│   ├── system_prompt_startup.md    ← NEW v3.2.0
│   └── system_prompt_[domain].md   ← 13 other domains
├── orchestrator/
│   ├── main.py
│   ├── goap_planner.py             ← v3.1.0
│   ├── catalogs.py                 ← UPDATED v3.2.0 (21 domains)
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
    ├── kac-assumption-audit/SKILL.md
    ├── ach-competing-explanations/SKILL.md
    ├── deception-detection/SKILL.md
    ├── verdict-verification/SKILL.md
    └── adaptive-autonomous-drive/SKILL.md  ← NEW v3.2.0
```

---

## Skills Catalog

| Skill | Function | Version |
|-------|----------|---------|
| `kac-assumption-audit` | Key Assumptions Check — before any FATAL/SERIOUS | v2.6.0 |
| `ach-competing-explanations` | When 2+ contradictory conclusions exist | v2.6.0 |
| `deception-detection` | When author has high personal/financial stakes | v2.6.0 |
| `verdict-verification` | Mandatory gate before any VERDICT block | v2.6.0 |
| `adaptive-autonomous-drive` | Autonomous goal generation and expansion | v3.2.0 |

---

## Domain Catalog (20 prompts + 1 base)

| ID | Domain | --type values | Primary Unit |
|----|--------|--------------|--------------|
| P01 | General | (fallback) | Contextual |
| P02 | Trading | chart, trading, xauusd, backtest | UNIT-QUANT |
| P03 | Legal | contract, nda, gdpr, employment | UNIT-INQUISITOR |
| P04 | Code | code, architecture, abap | UNIT-TECH |
| P05 | Financial | finance, investment, valuation, ma | UNIT-QUANT |
| P06 | Cloud | cloud, saas, paas, iaas | UNIT-TECH |
| P07 | Cybersecurity | cyber, security, pentest | UNIT-TECH |
| P08 | Agriculture | agro, livestock, harvest | UNIT-BIO |
| P09 | Real Estate | real_estate, property | UNIT-MARKET |
| P10 | Science | science, research | UNIT-QUANT |
| P11 | Media | media, content | UNIT-MARKET |
| P12 | E-Commerce | ecommerce, marketplace | UNIT-MARKET |
| P13 | Telecom | telecom, spectrum | UNIT-GEO |
| P14 | Public Sector | public, government, procurement | UNIT-COMPLIANCE |
| P15 | Medical | medical, clinical, health | UNIT-INQUISITOR |
| P16 | Marketing | marketing, growth, brand, funnel | UNIT-MARKET |
| P17 | Operations | operations, ops, supply_chain, sop | UNIT-TECH |
| P18 | Human Resources | hr, talent, compensation, culture | UNIT-COMPLIANCE |
| P19 | Strategy | strategy, strategic, competitive | UNIT-MARKET |
| P20 | Startup | startup, pitch, deck, pmf, runway | UNIT-QUANT |

---

## CLI Reference

```bash
# New domains v3.2.0
python main.py --type marketing --subscenario growth_plan --objective "audit CAC assumptions"
python main.py --type operations --subscenario supply_chain --objective "identify SPOF" --regime adversarial
python main.py --type hr --subscenario compensation --objective "pay equity audit" --regime regulatory
python main.py --type strategy --subscenario market_entry --objective "competitive risks" --tribunal
python main.py --type startup --subscenario pitch --objective "validate unit economics" --tribunal --ssm

# Full pipeline
python main.py --type startup --subscenario series_a --objective "investor readiness" \
  --regime adversarial --tribunal --agents 5 --ssm --ssm-scale MESO --verbose
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
| v3.2.0 Adaptive Autonomous Drive + 5 Domains | ✅ |

---

## Rules for extending

1. Increment version in CHANGELOG.md
2. Self-audit every candidate version
3. Do not soften the critical tone
4. New domain → entry in `catalogs.py` (ROLE_CATALOG + SSM_CATALOG + DOMAIN_MAP + DOMAIN_TOOLS)
5. New static prompt → `prompts/system_prompt_[domain].md`
6. New skill → `skills/[skill-name]/SKILL.md` + entry in SKILLS_CATALOG
7. The name `dark-strategist-agent` does not change under any circumstance

**ACTIVE — v3.2.0**
