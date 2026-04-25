# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

![Version](https://img.shields.io/badge/version-2.5.0-darkred)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-ACTIVE-brightgreen)

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

This is not a validator. Not a consultant. Not a coach.  
It is the mechanism that exposes what others do not want to see — and the Director who coordinates the team that confirms it.

### Version 2.5.0 — Major Release

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
| §4.14 Protocol Governance | ✅ |
| §4.15 Deprecation Clause | ✅ |
| §4.16 MVP_THRESHOLD — minimum info gate | ✅ NEW |
| §4.17 Operational Modes (Standard/Fast/Comparative/Optimization) | ✅ NEW |
| §4.18 COMPARATIVE_MODE — N simultaneous solutions | ✅ NEW |
| §4.19 OPTIMIZATION_MODE + PROJECTION_MATRIX | ✅ NEW |
| §4.20 FAST_TRACK MODE — agile analysis | ✅ NEW |
| §4.21 UNIT-PSYCH + verifiable Block 4 criteria | ✅ NEW |

---

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md
├── CHANGELOG.md
├── prompts/
│   └── system_prompt.md           ← Production-ready system prompt (EN)
├── examples/
│   ├── example_01_business_plan.md
│   ├── example_02_tech_architecture.md
│   └── example_03_war_room.md
└── docs/
    ├── severity_taxonomy.md
    ├── micro_agents_catalog.md
    ├── output_format.md
    ├── governance.md
    ├── deprecation.md
    └── operational_modes.md       ← NEW v2.5
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

## Operational Modes (v2.5 — Auto-selected in Phase 0)

| Mode | Trigger | Description |
|---|---|---|
| **STANDARD** | N=1 solution, creation/validation goal | Full protocol — 7 levels, Blocks 0–6, War Room if applicable |
| **FAST_TRACK** | Scale=Conceptual Idea + single domain | 4 levels, 3 blocks, ~40% of standard time |
| **COMPARATIVE** | N≥2 solutions declared | Independent analysis per solution + Comparison Matrix + Cross Verdict |
| **OPTIMIZATION** | Goal is improving something existing | Standard + baseline audit + PROJECTION_MATRIX (4 scenarios) |

Modes are **auto-selected** — user never needs to declare them explicitly.
COMPARATIVE + OPTIMIZATION are combinable. FAST_TRACK is exclusive.

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

### Micro-Agent Catalog (8 units)
| Unit | Role | Targets |
|---|---|---|
| UNIT-QUANT | Quantitative Auditor | Overfitting, margin calls, Sharpe ratio |
| UNIT-INQUISITOR | Legal & Tax Enforcer | Compliance, permits, labor violations |
| UNIT-TECH | Systems Auditor | Vulnerabilities, data leakage, SPOF |
| UNIT-BIO | Field & Livestock Auditor | Biomass, cold chain, biosecurity |
| UNIT-MARKET | Commercial Strategist | Demand assumptions, CAC, competition |
| UNIT-GEO | Geopolitical Analyst | Country risk, exchange volatility |
| UNIT-COMPLIANCE | Governance Auditor | SoD violations, ghost controls |
| UNIT-PSYCH | Behavioral Bias Auditor | Confirmation bias, groupthink, overconfidence |

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
[PROTOCOL_STATUS: ACTIVE — v2.5.0]
[DEPRECATION_CONDITIONS: A | B | C | D — see docs/deprecation.md]
[REPLACEMENT_PROTOCOL: NONE — current version is latest]
```

---

## License

MIT License — Open Source.
