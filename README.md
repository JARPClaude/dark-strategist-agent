# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-2.8.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)
![Domains](https://img.shields.io/badge/domains-14-blue)
![Tribunal](https://img.shields.io/badge/tribunal-adversarial-black)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

**v2.8.0 introduces the Tribunal Adversarial:** multiple Agentes Forenses auditing the same document in parallel, blind to each other, coordinated by the Agente Forense Orquestador (AFO) that synthesizes all findings into a single unified verdict.

---

### Version 2.8.0 — Major Release

| Feature | Status |
|---|---|
| 7-Level Forensic Analysis | ✅ |
| SAT Intelligence Doctrine (CIA Tradecraft) | ✅ v2.6.0 |
| KAC / ACH / Deception Detection / Verdict Verification | ✅ v2.6.0 |
| Domain Variant — Trading / Legal | ✅ v2.6.1 |
| Router Agent — Autonomous Domain Detection | ✅ v2.7.0 |
| 11 Domain Variants | ✅ v2.7.0 |
| UNKNOWN_DOMAIN → Slack + GitHub + Sheets | ✅ v2.7.0 |
| Google Cloud Function | ✅ v2.7.0 |
| **Agente Forense Orquestador (AFO)** | ✅ **v2.8.0** |
| **Tribunal Adversarial (1/3/5/7 agents parallel)** | ✅ **v2.8.0** |
| **Swarm Activation Score (auto-sizing)** | ✅ **v2.8.0** |
| **Sub-agentes Forenses Permanentes (8 UNITs)** | ✅ **v2.8.0** |
| **Sub-agentes Forenses Temporales + notification** | ✅ **v2.8.0** |
| **Budget Controller** | ✅ **v2.8.0** |
| **Verdict Synthesizer — unified verdict** | ✅ **v2.8.0** |

---

## Agent Hierarchy

```
N0 — Agente Forense Orquestador (AFO)
      Directs, consolidates, emits VEREDICTO FORENSE UNIFICADO
              │
    ┌─────────┼─────────┐
    │         │         │
  AF-01     AF-02     AF-03     ← N1: Agentes Forenses
(parallel) (parallel) (parallel)    (blind to each other)
    │         │         │
  ┌─┴─┐     ┌─┴─┐     ┌─┴─┐
  N2  N2    N2  N2    N2  N2   ← N2: Sub-agentes Forenses
 Perm/Temp Perm/Temp Perm/Temp     (on demand)
```

---

## Swarm Activation Score

| Initial Verdict | Mode | Agents |
|----------------|------|--------|
| SOLID / VIABLE WITH ADJUSTMENTS | SINGLE | 1 |
| VIABLE WITH CRITICAL CORRECTIONS | TRIBUNAL_LIGHT | 3 |
| INVIABLE | TRIBUNAL_FULL | 5 |
| INVIABLE + War Room | TRIBUNAL_MAX | 7 |

---

## Quick Start

```bash
cd orchestrator
pip install -r requirements.txt
cp config.example.json config.json

# Single mode
python main.py --document doc.txt

# Tribunal auto-size
python main.py --document doc.txt --tribunal

# Tribunal forced (5 agents)
python main.py --document doc.txt --tribunal --agents 5

# Full verbose
python main.py --document doc.txt --tribunal --verbose
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

## Sub-agent Catalog (N2)

| Unit | Specialization |
|------|---------------|
| UNIT-QUANT | Statistical, financial, quantitative |
| UNIT-INQUISITOR | Legal, regulatory, compliance |
| UNIT-TECH | Technical, security, systems |
| UNIT-PSYCH | Cognitive bias, behavioral |
| UNIT-GEO | Geopolitical, jurisdictional |
| UNIT-MARKET | Commercial, competitive |
| UNIT-COMPLIANCE | Governance, SoD, audit |
| UNIT-BIO | Agricultural, biological |
| **TEMP-[domain]** | Dynamic — unknown domains → notifies owner |

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

| Phase | Version | Status |
|-------|---------|--------|
| SAT Intelligence Doctrine | v2.6.0 | ✅ |
| Domain Variants + Infrastructure | v2.7.0 | ✅ |
| AFO + Tribunal Adversarial | v2.8.0 | ✅ |
| Simulación Social Masiva (SSM) | v2.9.0 | 🔲 Planned |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v2.8.0]
[TRIBUNAL: ACTIVE — 1/3/5/7 agents]
[DOMAIN_CATALOG: 14 prompts + 1 base + 1 router]
[SUB_AGENTS: 8 permanent + dynamic temporary]
[UNKNOWN_DOMAIN_HANDLER: ACTIVE]
[NOTIFICATION_CHANNELS: SLACK + GITHUB + SHEETS]
[SSM: ROADMAP v2.9.0]
```

---

## License

MIT License — Open Source.
