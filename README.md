# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-2.9.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-14-blue)
![Tribunal](https://img.shields.io/badge/tribunal-adversarial-black)
![SSM](https://img.shields.io/badge/SSM-active-purple)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

**v2.9.0 completes the full pipeline:**
1. **Tribunal Adversarial** — destroys the proposal internally (multiple agents, blind to each other)
2. **Simulación Social Masiva** — predicts how the real world destroys it if executed
3. **Transparency Report** — shows the user exactly what work was done and by whom

---

### Version 2.9.0 — Full Pipeline

| Feature | Status |
|---|---|
| 7-Level Forensic Analysis | ✅ |
| SAT Intelligence Doctrine + 4 Audit Skills | ✅ v2.6.0 |
| 14 Domain Variants + Router | ✅ v2.7.0 |
| Agente Forense Orquestador (AFO) | ✅ v2.8.0 |
| Tribunal Adversarial (1/3/5/7 parallel agents) | ✅ v2.8.0 |
| Sub-agentes Forenses (permanent + temporary) | ✅ v2.8.0 |
| Budget Controller | ✅ v2.8.0 |
| **Simulación Social Masiva (SSM)** | ✅ **v2.9.0** |
| **PersonaFactory — domain-specific personas** | ✅ **v2.9.0** |
| **4-round interaction engine** | ✅ **v2.9.0** |
| **Coalition formation + action simulation** | ✅ **v2.9.0** |
| **REPORTE DE IMPACTO SOCIAL** | ✅ **v2.9.0** |
| **Transparency Report** | ✅ **v2.9.0** |

---

## The Full Pipeline

```
Document presented
       ↓
FASE 1 — TRIBUNAL ADVERSARIAL
  AFO routes document → detects domain
  Swarm Activation Score → 1/3/5/7 agents
  Agentes Forenses audit in parallel (blind)
  Sub-agentes Forenses deployed on demand
  Verdict Synthesizer → VEREDICTO FORENSE UNIFICADO
       ↓ (if VIABLE)

FASE 2 — SIMULACIÓN SOCIAL MASIVA
  PersonaFactory generates N personas by domain
  Round 1: Individual opinions (blind)
  Round 2: Exchange → stance shifts
  Round 3: Coalition formation
  Round 4: Dominant coalition acts
  → REPORTE DE IMPACTO SOCIAL

FASE 3 — TRANSPARENCY REPORT
  Full operational metadata emitted
  AFO + Tribunal + Sub-agents + SSM + Budget + Notifications
```

---

## SSM Activation Logic

| Tribunal Verdict | SSM |
|----------------|-----|
| 🔴 INVIABLE | ❌ Blocked — always |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto-activated |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto-activated |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional — `--ssm` flag |

---

## Quick Start

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json

# Single audit
python main.py --document doc.txt

# Tribunal auto-size
python main.py --document doc.txt --tribunal

# Tribunal + SSM
python main.py --document doc.txt --tribunal --ssm

# Full pipeline, MACRO scale
python main.py --document doc.txt --tribunal --ssm --ssm-scale MACRO --verbose
```

---

## Domain Catalog (15 prompts)

| Prompt | Domain | Primary Unit |
|--------|--------|--------------|
| `system_prompt.md` | General | Contextual |
| `system_prompt_router.md` | Auto-detect | Contextual |
| `system_prompt_trading.md` | Trading / Algorithmic | UNIT-QUANT |
| `system_prompt_legal.md` | Legal / Compliance | UNIT-INQUISITOR |
| `system_prompt_code.md` | Code / ABAP / Architecture | UNIT-TECH |
| `system_prompt_financial.md` | Financial / M&A / Valuation | UNIT-QUANT |
| `system_prompt_cloud.md` | Cloud / SaaS / PaaS / IaaS | UNIT-TECH |
| `system_prompt_cybersecurity.md` | Cybersecurity / Audit | UNIT-TECH |
| `system_prompt_agro.md` | Agriculture / Livestock | UNIT-BIO |
| `system_prompt_realestate.md` | Real Estate | UNIT-MARKET |
| `system_prompt_science.md` | Science / R&D | UNIT-QUANT |
| `system_prompt_media.md` | Media / Content | UNIT-MARKET |
| `system_prompt_ecommerce.md` | E-Commerce | UNIT-MARKET |
| `system_prompt_telecom.md` | Telecom | UNIT-GEO |
| `system_prompt_publicsector.md` | Public Sector | UNIT-COMPLIANCE |

---

## SSM Persona Sets by Domain

| Domain | Personas Simulated |
|--------|------------------|
| Trading | Institutional investor, retail trader, regulator, competing fund, risk manager |
| Legal | Opposing counsel, judge, regulator, affected party, in-house counsel |
| Financial | VC, credit analyst, acquiring CFO, minority shareholder, financial press |
| Cloud | CTO, security lead, enterprise customer, data regulator, competing SaaS CEO |
| E-Commerce | Marketplace platform, end consumer, logistics provider, algorithm, competitor |
| Agriculture | Community leader, environmental regulator, commodity buyer, worker, NGO |
| Public Sector | Political opposition, taxpayer, state auditor, monitoring body, journalist |

---

## Verdict Decision Table

| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL | 🔴 INVIABLE |
| 0F + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0F + 0S + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs | 🟢 SOLID UNDER PRESSURE |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v2.9.0]
[TRIBUNAL: ACTIVE — 1/3/5/7 agents]
[SSM: ACTIVE — MICRO/MESO/MACRO scales]
[TRANSPARENCY_REPORT: ACTIVE — every session]
[DOMAIN_CATALOG: 14 prompts + 1 base + 1 router]
[SUB_AGENTS: 8 permanent + dynamic temporary]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
```

---

## License

MIT License — Open Source.
