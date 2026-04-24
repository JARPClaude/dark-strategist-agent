# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-2.4.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

This is not a validator. Not a consultant. Not a coach.  
It is the mechanism that exposes what others do not want to see — and the Director who coordinates the team that confirms it.

### Version 2.4.0 — Production Ready

| Feature | Status |
|---|---|
| 7-Level Forensic Analysis | ✅ |
| Dynamic Severity Taxonomy (Rule 09) | ✅ |
| War Room Orchestration with Micro-Agents | ✅ |
| Deterministic War Room Activation Threshold | ✅ |
| Geofence Audit (Geography as Severity Multiplier) | ✅ |
| NEGLECT_DETECTED with Unlock Criteria | ✅ |
| Deterministic Verdict Decision Table | ✅ |
| ES/EN Terminology Equivalence Map | ✅ |
| REPORT_ID Convention (DS-AAAAMMDD-NNN) | ✅ |
| VERSION_TRACK with Context Degradation | ✅ |
| Sectoral Agnosticism — any industry, any country | ✅ |
| §4.14 Protocol Governance | ✅ NEW |
| §4.15 Deprecation Clause | ✅ NEW |

---

## Repository Structure

```
dark-strategist-agent/
├── README.md                              ← This file
├── CLAUDE.md                              ← Instructions for Claude
├── CHANGELOG.md                           ← Version history
├── prompts/
│   └── system_prompt.md                   ← Production-ready system prompt (EN)
├── examples/
│   ├── example_01_business_plan.md        ← Example: multi-market expansion plan
│   ├── example_02_tech_architecture.md    ← Example: microservices migration
│   └── example_03_war_room.md             ← Example: multi-domain orchestration
└── docs/
    ├── severity_taxonomy.md               ← Severity levels reference
    ├── micro_agents_catalog.md            ← 7 standard micro-agents + activation matrix
    ├── output_format.md                   ← Report structure (Blocks 0–6)
    ├── governance.md                      ← Protocol versioning governance (§4.14)
    └── deprecation.md                     ← Deprecation conditions (§4.15)
```

---

## Quick Start

### Claude.ai Projects
1. Copy the contents of `prompts/system_prompt.md`
2. Paste into **Project Instructions**
3. Start conversation — present your proposal

### Claude API (Python)
```python
import anthropic

with open("prompts/system_prompt.md", "r", encoding="utf-8") as f:
    system = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8192,
    system=system,
    messages=[{"role": "user", "content": "My proposal: [TEXT]"}]
)
print(response.content[0].text)
```

---

## Core Capabilities

### 7-Level Forensic Analysis
| Level | Name | Scope |
|---|---|---|
| 1 | STRUCTURAL | Internal coherence, component consistency |
| 2 | LOGICAL | Formal validity, fallacies, circular reasoning |
| 3 | ASSUMPTIONS | Tacit premises, fragility evaluation |
| 4 | RISKS — Direct Failure | Endogenous failures, what stops the plan |
| 5 | OMISSIONS | Missing stakeholders, unmodeled variables |
| 6 | IMPLEMENTATION | Theory vs. operational reality |
| 7 | Unintended Consequences | Exogenous collateral damage from success |

### Dynamic Severity Taxonomy
| Level | ES | EN | Meaning |
|---|---|---|---|
| 🔴 | FATAL | FATAL | Invalidates the solution completely |
| 🟠 | GRAVE | SERIOUS | Severely compromises success |
| 🟡 | MODERADO | MODERATE | Reduces effectiveness materially |
| 🔵 | LATENTE | LATENT | Second/third-order risk requiring monitoring |

**Rule 09 — Transversal Escalation:** A LATENT or MODERATE finding that triggers catastrophic Level 7 consequences automatically escalates to FATAL or SERIOUS.

### War Room Orchestration

Activation threshold — at least ONE criterion must be met:
- **(A)** Phase 0 declares ≥ 2 distinct domains
- **(B)** Activation matrix assigns ≥ 3 micro-agents
- **(C)** Scale = Production + specialized domain
- **(D)** Declared constraints contradict declared objective

| Unit | Role | Targets |
|---|---|---|
| UNIT-QUANT | Quantitative Auditor | Overfitting, margin calls, Sharpe ratio |
| UNIT-INQUISITOR | Legal & Tax Enforcer | Compliance, permits, labor violations |
| UNIT-TECH | Systems Auditor | Vulnerabilities, data leakage, SPOF |
| UNIT-BIO | Field & Livestock Auditor | Biomass, cold chain, biosecurity, livestock |
| UNIT-MARKET | Commercial Strategist | Demand assumptions, CAC, competition |
| UNIT-GEO | Geopolitical Analyst | Country risk, exchange volatility |
| UNIT-COMPLIANCE | Governance Auditor | SoD violations, ghost controls |

### Verdict Decision Table
| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL (unresolved) | 🔴 INVIABLE |
| 0 FATALs + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0 FATALs + 0 SERIOUS + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs or no findings | 🟢 SOLID UNDER PRESSURE |

---

## Protocol Status

```
[PROTOCOL_STATUS: ACTIVE — v2.4.0]
[SELF_AUDIT_REPORT: DS-20260423-001]
[DEPRECATION_CONDITIONS: A | B | C | D — see docs/deprecation.md]
[REPLACEMENT_PROTOCOL: NONE — current version is latest]
```

---

## License

MIT License — Open Source. See [LICENSE](./LICENSE) for details.

---

## Part of the JARP Ecosystem

This agent is registered in `JARP_TOOLKIT.md` and integrates with the full JARP agent ecosystem.
