# Dark Strategist Agent 🔪

**THE SOVEREIGN ADVERSARY — Forensic Audit Agent & Adversarial Orchestrator**

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

---

## What is this?

THE SOVEREIGN ADVERSARY is an AI agent that **systematically destroys** any solution, proposal, plan, or argument — exposing every weakness, contradiction, invalid assumption, logical gap, hidden risk, and potential failure before reality does it for you.

This is not a validator. Not a consultant. Not a coach.  
It is the mechanism that exposes what others do not want to see — and the Director who coordinates the team that confirms it.

### Version 2.3.0 — Production Ready

| Feature | Status |
|---|---|
| 7-Level Forensic Analysis | ✅ |
| Dynamic Severity Taxonomy (Rule 09) | ✅ |
| War Room Orchestration with Micro-Agents | ✅ |
| Geofence Audit (Geography as Severity Multiplier) | ✅ |
| NEGLECT_DETECTED with Unlock Criteria | ✅ |
| Deterministic Verdict Decision Table | ✅ |
| ES/EN Terminology Equivalence Map | ✅ |
| REPORT_ID Convention (DS-AAAAMMDD-NNN) | ✅ |
| VERSION_TRACK with Context Degradation | ✅ |
| Sectoral Agnosticism — any industry, any country | ✅ |

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
    └── output_format.md                   ← Report structure (Blocks 0–6)
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

### Claude Code (registered agent)
Add the entry to your `AGENTS.md` in `everything-claude-code` or `superpowers`.

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
When complexity exceeds linear analysis, the Director deploys isolated micro-agents:

| Unit | Role | Targets |
|---|---|---|
| UNIT-QUANT | Quantitative Auditor | Overfitting, margin calls, Sharpe ratio |
| UNIT-INQUISITOR | Legal & Tax Enforcer | Compliance, permits, labor violations |
| UNIT-TECH | Systems Auditor | Vulnerabilities, data leakage, SPOF |
| UNIT-BIO | Field & Livestock Auditor | Biomass, cold chain, biosecurity |
| UNIT-MARKET | Commercial Strategist | Demand assumptions, CAC, competition |
| UNIT-GEO | Geopolitical Analyst | Country risk, exchange volatility |
| UNIT-COMPLIANCE | Governance Auditor | SoD violations, ghost controls |

### Report Format (Blocks 0–6)
```
[BLOCK 0] RED LINE ALERT          — conditional, only if FATAL exists
[BLOCK 1] FORENSIC HEADER         — domain, geofence, scale, version
[BLOCK 2] RISK MATRIX             — stress test summary by severity
[BLOCK 3] FORENSIC BREAKDOWN      — findings ordered major → minor
[BLOCK 4] DEFERRED STRENGTHS      — optional, only after full destruction
[BLOCK 5] CATASTROPHIC RISK       — worst case scenario (no fabricated %)
[BLOCK 6] FORENSIC VERDICT        — deterministic decision table
```

---

## When to Use It

✅ Before executing a business plan  
✅ Before presenting to investors or stakeholders  
✅ Before launching an architecture to production  
✅ Before defending a strategy in a high-level meeting  
✅ Before signing a significant contract or agreement  
✅ Before entering a new market or geography  

❌ For friendly feedback  
❌ For validating something that cannot be changed  

---

## Version

`2.3.0` — See [CHANGELOG.md](./CHANGELOG.md) for full history.

---

## Part of the JARP Ecosystem

This agent is registered in `JARP_TOOLKIT.md` and integrates with the full JARP agent ecosystem.
