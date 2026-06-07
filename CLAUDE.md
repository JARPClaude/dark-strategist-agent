# CLAUDE.md — Dark Strategist Agent
# Version: 3.17.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 3.17.0 — Minor Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent
**Name:** dark-strategist-agent — immutable, does not change under any circumstance.

---

## Full Pipeline

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

## Key Changes (v3.2 baseline; later versions in Version History)

| Feature | Description |
|---------|-------------|
| **Adaptive Autonomous Drive** | Skill that grants AFO autonomous expansion beyond initial prompt |
| **Marketing domain (P16)** | UNIT-MARKET primary. Rules MK1-MK4. CAC/ROAS/funnel audit. |
| **Operations domain (P17)** | UNIT-TECH primary. Rules OP1-OP4. Supply chain + SoD. |
| **Human Resources domain (P18)** | UNIT-COMPLIANCE primary. Rules HR1-HR4. Pay equity + labor law. |
| **Strategy domain (P19)** | UNIT-MARKET primary. Rules ST1-ST4. Competitive + assumption audit. |
| **Startup domain (P20)** | UNIT-QUANT primary. Rules SU1-SU5. PMF + unit economics. |
| **SKILLS_CATALOG** | New section in catalogs.py registering all 6 active skills. |

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
│   ├── wizard.py                   ← NEW v3.9.0 (interactive CLI)
│   ├── test_wizard.py              ← NEW v3.9.0 (wizard unit)
│   ├── goap_planner.py             ← v3.1.0
│   ├── catalogs.py                 ← UPDATED v3.2.0 (21 domains)
│   ├── schema.py
│   ├── prompt_engine.py
│   ├── context_builder.py
│   ├── tribunal_transversal.py
│   ├── archetype_lenses.py          ← NEW v3.13.0 (escalation lenses)
│   ├── budget_controller.py
│   ├── sub_agent_spawner.py
│   ├── retriever.py                ← NEW v3.8.0 (BM25 RAG feed)
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   ├── config.example.json
│   └── ssm/
├── corpus/                         ← NEW v3.8.0 (jurisdictional RAG corpora; empty)
├── infrastructure/
└── skills/
    ├── kac-assumption-audit/SKILL.md
    ├── ach-competing-explanations/SKILL.md
    ├── deception-detection/SKILL.md
    ├── verdict-verification/SKILL.md
    ├── adaptive-autonomous-drive/SKILL.md  ← NEW v3.2.0
    └── context-degradation/SKILL.md  ← NEW v3.7.0
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
| `context-degradation` | Context-degradation lens for LLM/RAG/agentic audits (P04/P07) | v1.0.0 |

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
| v3.3.0 Prompt-sweep closed — §4.14.1 validated | ✅ |
| v3.4.0 Synthesis shape contract + provenance restored + dead-code removal | ✅ |
| v3.5.0 UNIT-INGEST + UNIT-FACTCHECK + UNIT-PSYCH 80+ + stop-slop + lethal-trifecta P07 | ✅ |
| v3.6.0 Legal+Finance forensic matrix (25 incorporations, Sev×Lik non-binding, 4 variance decomp, SOX tier map) | ✅ |
| v3.7.0 Context-degradation lens (skill #6) into P04/P07 — 5 patterns, RULE C05/CY06, +10 rows | ✅ |
| v3.8.0 RAG retrieval at doc-feed layer — BM25 R1 intra-document + R2 jurisdictional corpus, non-breaking [:N] fallback | ✅ |
| v3.9.0 Interactive Wizard CLI (guided flag builder, synthesizes argv into the same parser) + doc_top_k align (D-v38-01) | ✅ |
| v3.10.0 BYO per-case reference corpus (--corpus + wizard step + markitdown; any jurisdiction, repo holds no laws) + R2 token-overlap floor + pydantic declared | ✅ |
| v3.11.0 Deterministic auditable confidence (both synthesis paths; cross-agent corroboration + unresolved clashes; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |
| v3.12.0 Confidence-gated escalation (LOW confidence + budget → bounded extra forensic round → re-synth → recompute; capped; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |
| v3.13.0 Archetype lenses for the escalation round (one abstract adversarial lens per FOR-ESC agent; refute-first + extend-first; NO real-person impersonation; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |
| v3.14.0 External-signals evidence channel (--signals; distinct [EXTERNAL SIGNALS] feed after corpus, in-band directive, BM25 reuse, drop-zero-overlap; signals = time-sensitive EVIDENCE that may substantiate a Finding; NON-BINDING — never alters the FATAL→INVIABLE verdict) | ✅ |
| v3.15.0 Signal-provenance attribution in the transparency report (deterministic post-verdict token-overlap; attributes each finding to the external signal it most overlaps; configurable floor `rag.provenance_min_overlap`; heuristic, NON-BINDING — reads the final verdict, writes only the report, never alters the FATAL→INVIABLE verdict) | ✅ |
| v3.16.0 Reputational-risk forensic lens (skill #7) into P11/P16/P19 - 5 patterns (over-claim, broken-promise, stakeholder-betrayal, association-contamination, silence-in-crisis), 7 RULES + 7 Failure-Catalog rows; detection lens, severity bound by the Failure Catalog, NON-BINDING - never alters the FATAL->INVIABLE verdict | ✅ |

---

## Rules for extending

1. Increment version in CHANGELOG.md
2. Self-audit every candidate version
3. Do not soften the critical tone
4. New domain → entry in `catalogs.py` (ROLE_CATALOG + SSM_CATALOG + DOMAIN_MAP + DOMAIN_TOOLS)
5. New static prompt → `prompts/system_prompt_[domain].md`
6. New skill → `skills/[skill-name]/SKILL.md` + entry in SKILLS_CATALOG
7. The name `dark-strategist-agent` does not change under any circumstance

**ACTIVE — v3.16.0**
