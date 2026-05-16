# CLAUDE.md — Dark Strategist Agent
# Version: 3.0.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 3.0.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent
**Name:** dark-strategist-agent — immutable, does not change under any circumstance.

---

## Full Pipeline v3.0.0

```
INPUT: case dict OR document file
       ↓
ContextBuilder → RuntimeContext
  domain, regime, rol_agents, forense_agents,
  ssm_personas, tools, tribunal_size
       ↓
TRIBUNAL TRANSVERSAL
  Layer 1: Agentes de Rol (parallel, blind)
    → simulate the domain environment
    → each adopts a stakeholder perspective
       ↓
  Layer 2: Agentes Forenses (parallel, blind)
    → audit the Rol simulation + document
    → detect inconsistencies, contrast hypotheses
    → spawn N2 Sub-agentes if needed
       ↓
  AFO Synthesis → UnifiedVerdictOutput (Pydantic)
    → programmatic conflict resolution
    → deterministic verdict table
       ↓ (if VIABLE)
SIMULACIÓN SOCIAL MASIVA (SSM)
  → N personas × 4 rounds
  → REPORTE DE IMPACTO SOCIAL
       ↓
TRANSPARENCY REPORT
  → Full operational metadata
```

---

## Key Architectural Changes v3.0.0 vs v2.x

| Aspect | v2.x | v3.0.0 |
|--------|------|---------|
| Prompts | 15 static .md files | 1 master template + catalogs |
| Tribunal | Forenses read document | Rol simulate → Forenses audit simulation |
| Output | Free text | Pydantic structured JSON |
| Domain knowledge | Per-file | catalogs.py (single source) |
| CLI | --document | --type --subscenario --objective --regime |
| New field | N/A | --regime (6 regimes) |
| New domain | N/A | Medical/Clinical |

---

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md
├── CHANGELOG.md
├── DEPLOY.md
├── prompts/
│   ├── system_prompt.md              ← Base fallback
│   ├── system_prompt_router.md
│   ├── system_prompt_medical.md      ← NEW v3.0.0
│   └── system_prompt_[domain].md     ← 14 existing domains
├── orchestrator/
│   ├── main.py                       ← v3.0 entry point
│   ├── catalogs.py                   ← NEW v3.0.0
│   ├── schema.py                     ← NEW v3.0.0
│   ├── prompt_engine.py              ← NEW v3.0.0
│   ├── context_builder.py            ← NEW v3.0.0
│   ├── tribunal_transversal.py       ← NEW v3.0.0
│   ├── tribunal.py                   ← v2.x preserved
│   ├── budget_controller.py
│   ├── sub_agent_spawner.py
│   ├── verdict_synthesizer.py
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   ├── config.example.json
│   └── ssm/
│       ├── __init__.py
│       ├── persona_factory.py
│       ├── interaction_engine.py
│       ├── social_report.py
│       └── budget_ssm.py
├── infrastructure/
│   └── cloud_function/
├── docs/
└── skills/
```

---

## CLI Reference v3.0.0

```bash
# Case-based (recommended)
python main.py --type contract --subscenario alquiler --objective "identify risks"
python main.py --type trading --subscenario XAUUSD --objective "buy sell wait" --regime breakout
python main.py --type medical --subscenario clinical_review --objective "protocol risks"

# With Tribunal Transversal
python main.py --type finance --subscenario investment_review --objective "evaluate viability" --tribunal

# With SSM
python main.py --type contract --subscenario alquiler --objective "risks" --tribunal --ssm

# Full pipeline
python main.py --type trading --subscenario XAUUSD --objective "direction" \
  --regime breakout --tribunal --agents 5 --ssm --ssm-scale MACRO --verbose

# v2.x document compatibility
python main.py --document doc.txt --tribunal --ssm

# Domain expansion report
python main.py --report
```

---

## Regime Options

| Regime | Description |
|--------|-------------|
| standard | Balanced — default |
| adversarial | Maximum pressure — worst case |
| breakout | High volatility / trend |
| crisis | Capital preservation priority |
| regulatory | Compliance-first |
| fast_track | Rapid — 4 levels |
| comparative | N≥2 solutions |

---

## Domain Catalog (16 domains)

| Domain | Type values |
|--------|------------|
| Trading | chart, trading, xauusd, eurusd, backtest |
| Legal | contract, alquiler, legal, compliance |
| Financial | finance, investment, valuation, ma |
| Cloud | cloud, saas, paas, iaas |
| Code | code, architecture, abap |
| Cybersecurity | cyber, security, pentest |
| Agriculture | agro, livestock, harvest |
| Real Estate | real_estate, property |
| Science | science, research |
| Medical | medical, clinical, health |
| Media | media, content |
| E-Commerce | ecommerce, marketplace |
| Telecom | telecom, spectrum |
| Public Sector | public, government, procurement |
| General | (fallback) |

---

## SSM Activation Logic

| Tribunal Verdict | SSM |
|----------------|-----|
| 🔴 INVIABLE | ❌ Blocked |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional (--ssm) |

---

## Roadmap

| Version | Status |
|---------|--------|
| v2.6.0 SAT Skills | ✅ |
| v2.7.0 Router + 11 Domains | ✅ |
| v2.8.0 AFO + Tribunal Adversarial | ✅ |
| v2.9.0 SSM + Transparency Report | ✅ |
| v3.0.0 Tribunal Transversal + Dynamic Prompts | ✅ |

---

## Rules for extending

1. Increment version in CHANGELOG.md
2. Self-audit every candidate version
3. Do not soften the critical tone
4. New domain → entry in `catalogs.py` (ROLE_CATALOG + SSM_CATALOG + DOMAIN_MAP + DOMAIN_TOOLS)
5. New static prompt (optional) → `prompts/system_prompt_[domain].md`
6. New prompt registered in `system_prompt_router.md`
7. New skills → `skills/[skill-name]/SKILL.md`
8. The name `dark-strategist-agent` does not change under any circumstance

**ACTIVE — v3.0.0**
