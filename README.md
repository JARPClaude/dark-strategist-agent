# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-2.7.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-14-blue)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

This is not a validator. Not a consultant. Not a coach.
It is the mechanism that exposes what others do not want to see — and the Director who coordinates the team that confirms it.

**v2.7.0 introduces full autonomy:** the agent detects the document domain, selects the correct prompt automatically, and — when no prompt exists — builds a dynamic calibration and notifies the design team via Slack, GitHub, and Google Sheets without user intervention.

---

### Version 2.7.0 — Major Release

| Feature | Status |
|---|---|
| 7-Level Forensic Analysis | ✅ |
| Dynamic Severity Taxonomy (Rule 09) | ✅ |
| War Room Orchestration with 8 Micro-Agents | ✅ |
| Deterministic Verdict Decision Table | ✅ |
| SAT Intelligence Doctrine (CIA Tradecraft) | ✅ v2.6.0 |
| KAC / ACH / Deception Detection / Verdict Verification | ✅ v2.6.0 |
| Domain Variant — Trading (MQL5, Pine Script) | ✅ v2.6.1 |
| Domain Variant — Legal (Contracts, Compliance) | ✅ v2.6.1 |
| **Router Agent — Autonomous Domain Detection** | ✅ **v2.7.0** |
| **Domain Variant — Code (ABAP, Java, .NET, Python)** | ✅ **v2.7.0** |
| **Domain Variant — Financial (M&A, DCF, Valuation)** | ✅ **v2.7.0** |
| **Domain Variant — Cloud (SaaS / PaaS / IaaS)** | ✅ **v2.7.0** |
| **Domain Variant — Cybersecurity / Systems Audit** | ✅ **v2.7.0** |
| **Domain Variant — Agriculture / Livestock / Mining** | ✅ **v2.7.0** |
| **Domain Variant — Real Estate / Property** | ✅ **v2.7.0** |
| **Domain Variant — Science / R&D / Clinical** | ✅ **v2.7.0** |
| **Domain Variant — Media / Content Creators** | ✅ **v2.7.0** |
| **Domain Variant — E-Commerce / Marketplaces** | ✅ **v2.7.0** |
| **Domain Variant — Telecom / Infrastructure** | ✅ **v2.7.0** |
| **Domain Variant — Public Sector / Government** | ✅ **v2.7.0** |
| **UNKNOWN_DOMAIN Protocol + Dynamic Calibration** | ✅ **v2.7.0** |
| **Slack + GitHub Issues + Google Sheets — Auto-notify** | ✅ **v2.7.0** |
| **Google Cloud Function — HTTP endpoint** | ✅ **v2.7.0** |

---

## Quick Start

### Option A — Claude.ai Projects (manual)
1. Select prompt from `/prompts/`
2. Paste into **Project Instructions**
3. Present your document

### Option B — API Autonomous
```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json
python main.py --document path/to/document.txt
```

### Option C — Cloud Function (production)
```bash
curl -X POST https://YOUR_REGION-YOUR_PROJECT.cloudfunctions.net/dark-strategist \
    -H "Content-Type: application/json" \
    -d '{"document": "Your document text here"}'
```

See `DEPLOY.md` for full deployment guide.

---

## Domain Catalog

| Prompt | Domain | Primary Unit |
|--------|--------|--------------|
| `system_prompt.md` | General — universal fallback | Contextual |
| `system_prompt_router.md` | Auto-detect (API) | Contextual |
| `system_prompt_trading.md` | Capital Markets / Algorithmic Trading | UNIT-QUANT |
| `system_prompt_legal.md` | Legal / Regulatory / Compliance | UNIT-INQUISITOR |
| `system_prompt_code.md` | Software Dev / Code Review (ABAP, Java, .NET) | UNIT-TECH |
| `system_prompt_financial.md` | Financial Analysis / M&A / Valuation | UNIT-QUANT |
| `system_prompt_cloud.md` | Cloud / SaaS / PaaS / IaaS | UNIT-TECH |
| `system_prompt_cybersecurity.md` | Cybersecurity / Systems Audit | UNIT-TECH + COMPLIANCE |
| `system_prompt_agro.md` | Agriculture / Livestock / Mining | UNIT-BIO |
| `system_prompt_realestate.md` | Real Estate / Property | UNIT-MARKET |
| `system_prompt_science.md` | Science / R&D / Clinical | UNIT-QUANT |
| `system_prompt_media.md` | Media / Content Creators | UNIT-MARKET |
| `system_prompt_ecommerce.md` | E-Commerce / Marketplaces / D2C | UNIT-MARKET |
| `system_prompt_telecom.md` | Telecommunications / Infrastructure | UNIT-GEO |
| `system_prompt_publicsector.md` | Public Sector / Government / Education | UNIT-COMPLIANCE |

---

## UNKNOWN_DOMAIN Protocol

```
Document presented
       ↓
Router: UNKNOWN_DOMAIN detected
       ↓
Dynamic calibration on base protocol
       ↓
Full 7-level audit executed
       ↓
DOMAIN_EXPANSION_RECOMMENDED appended
       ↓ (automatic — zero user action)
Slack → #dark-strategist-alerts
GitHub Issue → JARPClaude/dark-strategist-agent
Google Sheets → DomainExpansionLog
```

---

## Core Capabilities

### 7-Level Forensic Analysis
| Level | Name |
|---|---|
| 1 | STRUCTURAL — Internal coherence |
| 2 | LOGICAL — Validity, fallacies, circular reasoning |
| 3 | ASSUMPTIONS — Tacit premises, fragility |
| 4 | RISKS — Direct failure, endogenous |
| 5 | OMISSIONS — Missing elements |
| 6 | IMPLEMENTATION — Theory vs. reality |
| 7 | UNINTENDED CONSEQUENCES — Exogenous damage |

### Verdict Decision Table
| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL | 🔴 INVIABLE |
| 0F + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0F + 0S + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs | 🟢 SOLID UNDER PRESSURE |

### Micro-Agent Catalog
| Unit | Primary Domain |
|---|---|
| UNIT-QUANT | Trading, Financial, Science |
| UNIT-INQUISITOR | Legal — PRIMARY |
| UNIT-TECH | Code, Cloud, Cybersecurity — PRIMARY |
| UNIT-BIO | Agro — PRIMARY |
| UNIT-MARKET | Real Estate, Media, E-Commerce — PRIMARY |
| UNIT-GEO | Telecom — PRIMARY |
| UNIT-COMPLIANCE | Public Sector, Cybersecurity — PRIMARY |
| UNIT-PSYCH | All domains — deception detection |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v2.7.0]
[DOMAIN_CATALOG: 14 prompts + 1 base + 1 router]
[UNKNOWN_DOMAIN_HANDLER: ACTIVE]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
```

---

## License

MIT License — Open Source.
