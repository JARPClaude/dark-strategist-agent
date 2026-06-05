# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-3.11.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-20-blue)
![Skills](https://img.shields.io/badge/skills-6-orange)
![Tribunal](https://img.shields.io/badge/tribunal-transversal-black)
![SSM](https://img.shields.io/badge/SSM-active-purple)
![GOAP](https://img.shields.io/badge/GOAP-A*_planner-orange)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

**Core capabilities:**
- **Adaptive Autonomous Drive** — the AFO now expands analysis autonomously when it detects gaps, without user instruction.
- **5 New Domains** — Marketing, Operations, Human Resources, Strategy, Startup (P16–P20).
- **20 total domain variants** covering any industry, any document type, any country.

---

### Full Feature Set

| Feature | Status |
|---|---|
| Tribunal Transversal (2-layer) | ✅ v3.0 |
| Dynamic Prompt Engine | ✅ v3.0 |
| Pydantic VerdictOutput | ✅ v3.0 |
| Medical domain | ✅ v3.0 |
| GOAP A\* Planner | ✅ v3.1 |
| Legal 12 Sub-area Taxonomy | ✅ v3.1 |
| **Adaptive Autonomous Drive (skill)** | ✅ **v3.2** |
| **Marketing domain (P16)** | ✅ **v3.2** |
| **Operations domain (P17)** | ✅ **v3.2** |
| **Human Resources domain (P18)** | ✅ **v3.2** |
| **Strategy domain (P19)** | ✅ **v3.2** |
| **Startup domain (P20)** | ✅ **v3.2** |
| Forensic units (INGEST / FACTCHECK / PSYCH) + stop-slop scorer | ✅ v3.5 |
| Legal + Finance forensic matrix (Sev×Lik non-binding, SOX tier map, 4 variance lenses) | ✅ v3.6 |
| Context-degradation forensic lens (skill #6) | ✅ v3.7 |
| RAG document-feed — BM25 (R1 intra-document + R2 corpus), non-breaking [:N] fallback | ✅ v3.8 |
| Interactive Wizard CLI (guided flag builder) | ✅ v3.9 |
| BYO per-case reference corpus (`--corpus`, any jurisdiction) + R2 token-overlap floor | ✅ v3.10 |

---

## Adaptive Autonomous Drive

The AFO no longer stops at the first analysis pass. When the **Adaptive Autonomous Drive** skill is active, it:

```
Standard analysis complete
        ↓
[SKILL: ADAPTIVE AUTONOMOUS DRIVE]
  GoalEngine detects gaps → generates new internal goals
  MotivationModel identifies highest adversarial value
  AutonomousLoop activates sub-agents without user instruction
  StateMemory tracks what has been covered
  SelfEvaluation decides if analysis is complete
  SafetyGuard enforces hard limits (no infinite loops)
        ↓
Additional adversarial rounds executed
        ↓
Final report — deeper, higher coverage, no gaps left unaddressed
```

---

## Skills Catalog

| Skill | Function |
|-------|----------|
| `kac-assumption-audit` | Mandatory before any FATAL/SERIOUS finding |
| `ach-competing-explanations` | When 2+ contradictory conclusions are possible |
| `deception-detection` | When author has high personal/financial stakes |
| `verdict-verification` | Mandatory gate before any VERDICT block |
| `adaptive-autonomous-drive` | Autonomous goal generation and gap expansion |
| `context-degradation` | LLM/RAG/agentic context-degradation audit lens (P04/P07) |

---

## Domain Catalog (20 domains)

| ID | Domain | --type values | Primary Unit |
|----|--------|--------------|--------------|
| P02 | Trading | `chart` `trading` `xauusd` `backtest` | UNIT-QUANT |
| P03 | Legal | `contract` `nda` `gdpr` `employment` `litigation` | UNIT-INQUISITOR |
| P04 | Code | `code` `architecture` `abap` | UNIT-TECH |
| P05 | Financial | `finance` `investment` `valuation` `ma` | UNIT-QUANT |
| P06 | Cloud | `cloud` `saas` `paas` `iaas` | UNIT-TECH |
| P07 | Cybersecurity | `cyber` `security` `pentest` | UNIT-TECH |
| P08 | Agriculture | `agro` `livestock` `harvest` | UNIT-BIO |
| P09 | Real Estate | `real_estate` `property` | UNIT-MARKET |
| P10 | Science | `science` `research` | UNIT-QUANT |
| P11 | Media | `media` `content` | UNIT-MARKET |
| P12 | E-Commerce | `ecommerce` `marketplace` | UNIT-MARKET |
| P13 | Telecom | `telecom` `spectrum` | UNIT-GEO |
| P14 | Public Sector | `public` `government` `procurement` | UNIT-COMPLIANCE |
| P15 | Medical | `medical` `clinical` `health` | UNIT-INQUISITOR |
| **P16** | **Marketing** | `marketing` `growth` `brand` `funnel` | UNIT-MARKET |
| **P17** | **Operations** | `operations` `ops` `supply_chain` `sop` | UNIT-TECH |
| **P18** | **Human Resources** | `hr` `talent` `compensation` `culture` | UNIT-COMPLIANCE |
| **P19** | **Strategy** | `strategy` `strategic` `competitive` | UNIT-MARKET |
| **P20** | **Startup** | `startup` `pitch` `deck` `pmf` `runway` | UNIT-QUANT |

---

## Full Pipeline

```
INPUT: --type startup --subscenario pitch --regime adversarial
       ↓
ContextBuilder → RuntimeContext (domain=Startup, regime=adversarial)
       ↓
GOAPPlanner A* → Execution Plan (optimal for budget + domain)
       ↓
TRIBUNAL TRANSVERSAL
  Layer 1: Agentes de Rol (simulate domain stakeholders)
  Layer 2: Agentes Forenses (audit the simulation)
  [ADAPTIVE AUTONOMOUS DRIVE] → expand if gaps detected
  N2 Sub-agentes on demand
  AFO → UnifiedVerdictOutput (Pydantic)
       ↓ (if VIABLE)
SSM → N personas × 4 rounds → Social Report
       ↓
TRANSPARENCY REPORT (full operational metadata)
```

---

## Quick Start

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json

# Marketing audit
python main.py --type marketing --subscenario growth_plan --objective "audit CAC assumptions"

# Operations with adversarial regime
python main.py --type operations --subscenario supply_chain \
  --objective "identify single points of failure" --regime adversarial --tribunal

# HR pay equity
python main.py --type hr --subscenario compensation \
  --objective "pay equity audit" --regime regulatory --tribunal

# Strategy competitive analysis
python main.py --type strategy --subscenario market_entry \
  --objective "competitive risks" --tribunal --agents 5

# Startup pitch full pipeline
python main.py --type startup --subscenario pitch \
  --objective "validate unit economics" --tribunal --ssm --ssm-scale MESO --verbose
```

---

## Verdict Decision Table

| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL | 🔴 INVIABLE |
| 0F + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0F + 0S + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs | 🟢 SOLID UNDER PRESSURE |

---

## SSM Activation Logic

| Verdict | SSM |
|---------|-----|
| 🔴 INVIABLE | ❌ Blocked |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional `--ssm` |

---

## Roadmap

| Version | Feature | Status |
|---------|---------|--------|
| v2.6–v2.9 | SAT Skills, Domains, AFO, SSM | ✅ |
| v3.0.0 | Tribunal Transversal + Dynamic Prompts | ✅ |
| v3.1.0 | GOAP A\* + Legal 12 Sub-areas | ✅ |
| v3.2.0 | Adaptive Autonomous Drive + 5 Domains | ✅ |
| v3.3.0 | Prompt-sweep cycle closed — §4.14.1 validated end-to-end | ✅ |
| v3.4.0 | Synthesis shape contract + transparency provenance restored + dead-code removal | ✅ |
| v3.5.0 | UNIT-INGEST + UNIT-FACTCHECK + UNIT-PSYCH 80+ + stop-slop scorer + lethal-trifecta P07 | ✅ |
| v3.6.0 | Legal+Finance forensic matrix — 25 incorporations, Sev×Lik non-binding, 4 variance decompositions, SOX deficiency tier map | ✅ |
| v3.7.0 | Context-degradation forensic lens (skill #6) into P04/P07 — 5 patterns, RULE C05/CY06, +10 catalog rows | ✅ |
| v3.8.0 | RAG retrieval at document-feed layer — BM25 (R1 intra-document relevance replaces blind doc_window truncation; R2 optional jurisdictional corpus), non-breaking [:N] fallback | ✅ |
| v3.9.0 | Interactive Wizard CLI — guided flag builder (synthesizes argv into the same parser); doc_top_k align (D-v38-01) | ✅ |
| v3.10.0 | BYO per-case reference corpus — `--corpus` + wizard step + markitdown (any jurisdiction; repo holds no laws) + R2 token-overlap floor + pydantic declared | ✅ |
| v3.11.0 | Deterministic auditable confidence — computed in both synthesis paths from cross-agent corroboration + unresolved clashes; NON-BINDING (never alters the FATAL→INVIABLE verdict) | ✅ |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v3.11.0]
[PLANNER: GOAP A* — dynamic optimal planning]
[TRIBUNAL: TRANSVERSAL — Rol + Forense layers]
[SKILL: ADAPTIVE AUTONOMOUS DRIVE — active]
[DOMAINS: 20 total — P01 to P20]
[SKILLS: 6 active]
[SSM: ACTIVE — MICRO/MESO/MACRO]
[TRANSPARENCY_REPORT: ACTIVE — every session]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
```

---

## License

MIT License — Open Source.
