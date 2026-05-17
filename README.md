# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-3.1.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-16-blue)
![Tribunal](https://img.shields.io/badge/tribunal-transversal-black)
![SSM](https://img.shields.io/badge/SSM-active-purple)
![GOAP](https://img.shields.io/badge/GOAP-A*_planner-orange)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

**v3.1.0 introduces:**
- **GOAP A\* Planner** — dynamic planning replaces fixed rules. Given domain, regime, and budget, A\* finds the optimal sequence of agents to deploy.
- **Legal Taxonomy (12 sub-areas)** — Commercial, Corporate/M&A, Employment, Privacy, Product, Regulatory, AI Governance, IP, Litigation, Real Estate, Finance, Public Regulatory.

---

### Version 3.1.0 — Major Release

| Feature | Status |
|---|---|
| Tribunal Transversal (2-layer) | ✅ v3.0 |
| Dynamic Prompt Engine | ✅ v3.0 |
| Pydantic VerdictOutput | ✅ v3.0 |
| Medical domain | ✅ v3.0 |
| **GOAP A\* Planner** | ✅ **v3.1** |
| **Legal 12 Sub-area Taxonomy** | ✅ **v3.1** |
| **AI Governance Legal (L07)** | ✅ **v3.1** |
| **LEGAL_SUBAREA_MAP auto-detection** | ✅ **v3.1** |

---

## GOAP A\* Planner

The AFO no longer uses fixed rules to decide how many agents to deploy. It plans dynamically.

```
FIXED (v2.x):
  IF verdict=INVIABLE → always 5 agents
  (ignores budget, domain, regime)

GOAP A* (v3.1):
  Given budget=15, domain=Legal, regime=adversarial:
  → optimal plan: ROL:3 + FORENSE:3 + N2:2 + SYNTHESIZE = 12 calls

  Given budget=8, domain=General, regime=standard:
  → optimal plan: ROL:2 + FORENSE:2 + SYNTHESIZE = 6 calls
```

### How A\* works in the AFO

```
WorldState (current):           GoalState:
  domain = Legal                  synthesis_done = True
  regime = adversarial            ssm_required = True
  budget_remaining = 20
  initial_audit_done = False
         ↓
  A* searches action space
  (12 possible actions × budget constraints)
         ↓
  Optimal plan found:
  1. INITIAL_AUDIT (cost=1)
  2. ROL_LAYER_STANDARD (cost=3)
  3. FORENSE_LAYER_FULL (cost=5)
  4. SPAWN_N2_TARGETED (cost=2)
  5. SYNTHESIZE (cost=1)
  6. SSM_MESO (cost=10)
  Total: 22 calls — within budget ✅
```

---

## Legal Domain — 12 Practice Sub-areas

| ID | Sub-area | Key Risk |
|----|----------|---------|
| L01 | Commercial Legal | Unlimited liability, IP gaps |
| L02 | Corporate / M&A | Undisclosed liabilities, synergy claims |
| L03 | Employment | Misclassification, non-compete |
| L04 | Privacy (GDPR/CCPA) | Consent, residency, transfer |
| L05 | Product Legal | False advertising, warranty |
| L06 | Regulatory | Reporting gaps, jurisdictional conflict |
| **L07** | **AI Governance** | AI output IP, bias monitoring, vendor liability |
| L08 | IP Legal | Chain of title, OSS contamination |
| L09 | Litigation | Jurisdictional defects, damages |
| L10 | Real Estate Legal | Title gaps, zoning violations |
| L11 | Finance Legal | Covenant breach, cross-default |
| L12 | Public Regulatory | Procurement irregularities, integrity |

Sub-areas are **auto-detected** from document keywords (nda, gdpr, trademark, employment, ai governance, etc.) or declared explicitly.

---

## Full Pipeline

```
INPUT: --type contract --subscenario nda --regime adversarial
       ↓
ContextBuilder → RuntimeContext (domain=Legal, sub_area=L01)
       ↓
GOAPPlanner A* → Execution Plan (optimal for budget + domain)
       ↓
TRIBUNAL TRANSVERSAL
  Layer 1: Agentes de Rol (simulate domain)
  Layer 2: Agentes Forenses (audit simulation)
  N2 Sub-agentes on demand
  AFO → UnifiedVerdictOutput (Pydantic)
       ↓ (if VIABLE)
SSM → N personas × 4 rounds → Social Report
       ↓
TRANSPARENCY REPORT (full operational metadata)
```

---

## Domain Catalog (16 domains)

| Domain | --type values |
|--------|--------------|
| Trading | `chart` `trading` `xauusd` `backtest` |
| Legal | `contract` `nda` `gdpr` `employment` `trademark` `litigation` |
| Financial | `finance` `investment` `valuation` `ma` |
| Cloud | `cloud` `saas` `paas` `iaas` |
| Code | `code` `architecture` `abap` |
| Cybersecurity | `cyber` `security` `pentest` |
| Agriculture | `agro` `livestock` `harvest` |
| Real Estate | `real_estate` `property` |
| Science | `science` `research` |
| Medical | `medical` `clinical` `health` |
| Media | `media` `content` |
| E-Commerce | `ecommerce` `marketplace` |
| Telecom | `telecom` `spectrum` |
| Public Sector | `public` `government` `procurement` |

---

## Quick Start

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json

# Legal contract — auto-detects sub-area
python main.py --type contract --subscenario nda --objective "identify risks" --regime adversarial

# Legal AI Governance
python main.py --type legal --subscenario "ai governance" --objective "ai vendor risks" --tribunal

# Trading with full pipeline
python main.py --type trading --subscenario XAUUSD --objective "direction" \
  --regime breakout --tribunal --ssm --ssm-scale MESO --verbose

# Medical
python main.py --type medical --subscenario clinical_review \
  --objective "protocol risks" --tribunal --agents 5
```

---

## SSM Activation Logic

| Verdict | SSM |
|---------|-----|
| 🔴 INVIABLE | ❌ Blocked |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional `--ssm` |

---

## Verdict Decision Table

| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL | 🔴 INVIABLE |
| 0F + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0F + 0S + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs | 🟢 SOLID UNDER PRESSURE |

---

## Roadmap

| Version | Feature | Status |
|---------|---------|--------|
| v2.6-v2.9 | SAT Skills, Domains, AFO, SSM | ✅ |
| v3.0.0 | Tribunal Transversal + Dynamic Prompts | ✅ |
| v3.1.0 | GOAP A\* Planner + Legal 12 Sub-areas | ✅ |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v3.1.0]
[PLANNER: GOAP A* — dynamic optimal planning]
[TRIBUNAL: TRANSVERSAL — Rol + Forense layers]
[LEGAL: 12 sub-areas — L01 to L12]
[DOMAINS: 16 total]
[SSM: ACTIVE — MICRO/MESO/MACRO]
[TRANSPARENCY_REPORT: ACTIVE]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
```

---

## License

MIT License — Open Source.
