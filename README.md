# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-3.0.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-16-blue)
![Tribunal](https://img.shields.io/badge/tribunal-transversal-black)
![SSM](https://img.shields.io/badge/SSM-active-purple)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

**v3.0.0 — The Tribunal Transversal:**
- **Agentes de Rol** simulate the domain environment (stakeholders, market, regulatory context)
- **Agentes Forenses** audit what the simulation produces — detecting inconsistencies, contrasting hypotheses, exposing deception
- **Dynamic prompts** generated at runtime from catalogs — no static files required
- **Pydantic structured output** — verdicts are comparable programmatically
- **Regime calibration** — analysis intensity set before any agent runs

---

### Version 3.0.0 — Major Release

| Feature | Status |
|---|---|
| SAT Intelligence Doctrine + 4 Audit Skills | ✅ v2.6 |
| 15 Domain Variants + Router | ✅ v2.7 |
| AFO + Tribunal Adversarial | ✅ v2.8 |
| SSM + Transparency Report | ✅ v2.9 |
| **Tribunal Transversal (2-layer architecture)** | ✅ **v3.0** |
| **Dynamic Prompt Engine (master template)** | ✅ **v3.0** |
| **ROLE_CATALOG (Rol + Forense per domain)** | ✅ **v3.0** |
| **Pydantic VerdictOutput (structured JSON)** | ✅ **v3.0** |
| **RuntimeContext + ContextBuilder** | ✅ **v3.0** |
| **Regime field (6 regimes)** | ✅ **v3.0** |
| **Medical / Clinical domain** | ✅ **v3.0** |

---

## The Two-Layer Tribunal

```
LAYER 1 — Agentes de Rol (parallel, blind)
  Each simulates a domain stakeholder:
  Trading:     Institutional investor, market maker, retail trader...
  Legal:       Contracting party, regulator, affected third party...
  Medical:     Clinician, regulator, patient advocate...
  [14 domain sets × 4-5 roles each]
       ↓ simulation output

LAYER 2 — Agentes Forenses (parallel, blind)
  Each audits the simulation:
  Trading:     Quantitative forense, execution forense, regime forense
  Legal:       Clause forense, jurisdiction forense, liability forense
  Medical:     Clinical forense, regulatory forense, liability forense
  [14 domain sets × 3 forensic roles each]
       ↓ structured VerdictOutput (Pydantic)

AFO SYNTHESIS
  → Consolidates all outputs
  → Resolves conflicts (highest severity wins)
  → Applies Verdict Decision Table
  → VEREDICTO FORENSE UNIFICADO
```

---

## Quick Start

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json

# Case-based (v3.0 — recommended)
python main.py --type contract --subscenario alquiler --objective "identify risks"
python main.py --type trading --subscenario XAUUSD --objective "direction" --regime breakout
python main.py --type medical --subscenario clinical_review --objective "protocol risks"

# With Tribunal Transversal + SSM
python main.py --type finance --subscenario investment_review \
  --objective "evaluate viability" --tribunal --ssm

# Full pipeline
python main.py --type trading --subscenario XAUUSD --objective "buy sell wait" \
  --regime breakout --tribunal --agents 5 --ssm --ssm-scale MACRO --verbose
```

---

## Regime Options

| Regime | Description |
|--------|-------------|
| `standard` | Balanced — default |
| `adversarial` | Maximum pressure — worst case |
| `breakout` | High volatility / trend conditions |
| `crisis` | Capital preservation priority |
| `regulatory` | Compliance-first lens |
| `fast_track` | Rapid — 4 levels only |
| `comparative` | N≥2 solutions |

---

## Domain Catalog (16 domains)

| Domain | --type values |
|--------|--------------|
| Trading | `chart` `trading` `xauusd` `backtest` |
| Legal | `contract` `alquiler` `legal` |
| Financial | `finance` `investment` `valuation` |
| Cloud | `cloud` `saas` `paas` `iaas` |
| Code | `code` `architecture` `abap` |
| Cybersecurity | `cyber` `security` `pentest` |
| Agriculture | `agro` `livestock` `harvest` |
| Real Estate | `real_estate` `property` |
| Science | `science` `research` |
| **Medical** | `medical` `clinical` `health` |
| Media | `media` `content` |
| E-Commerce | `ecommerce` `marketplace` |
| Telecom | `telecom` `spectrum` |
| Public Sector | `public` `government` `procurement` |

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
| v2.6.0 | SAT Skills | ✅ |
| v2.7.0 | Router + 11 Domains | ✅ |
| v2.8.0 | AFO + Tribunal Adversarial | ✅ |
| v2.9.0 | SSM + Transparency Report | ✅ |
| v3.0.0 | Tribunal Transversal + Dynamic Prompts | ✅ |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v3.0.0]
[TRIBUNAL: TRANSVERSAL — Rol + Forense layers]
[DOMAINS: 16 (including Medical)]
[PROMPTS: DYNAMIC — master template + catalogs]
[OUTPUT: STRUCTURED — Pydantic VerdictOutput]
[SSM: ACTIVE — MICRO/MESO/MACRO]
[TRANSPARENCY_REPORT: ACTIVE — every session]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
```

---

## License

MIT License — Open Source.
