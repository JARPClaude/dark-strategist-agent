# CLAUDE.md — Dark Strategist Agent
# Instructions for Claude when operating within this repository

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 2.6.0 — Major Release  
**License:** MIT — Open Source  
**Repository:** https://github.com/JARPClaude/dark-strategist-agent

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md                          ← This file
├── CHANGELOG.md
├── prompts/
│   └── system_prompt.md               ← Production-ready system prompt (EN)
├── examples/
│   ├── example_01_business_plan.md
│   ├── example_02_tech_architecture.md
│   └── example_03_war_room.md
├── docs/
│   ├── severity_taxonomy.md
│   ├── micro_agents_catalog.md
│   ├── output_format.md
│   ├── governance.md
│   ├── deprecation.md
│   ├── operational_modes.md
│   └── sat_intelligence_doctrine.md   ← NEW v2.6
└── skills/                            ← NEW v2.6
    ├── kac-assumption-audit/
    │   └── SKILL.md
    ├── ach-competing-explanations/
    │   └── SKILL.md
    ├── deception-detection/
    │   └── SKILL.md
    └── verdict-verification/
        └── SKILL.md
```

## Skills (v2.6)

Before issuing any finding, severity, or verdict, Claude reads the relevant skill:

- **`skills/kac-assumption-audit/SKILL.md`** — Mandatory before assigning FATAL or SERIOUS. Extracts and challenges all stated and unstated premises.
- **`skills/ach-competing-explanations/SKILL.md`** — Use when 2+ contradictory conclusions are possible. Ranks by least falsified hypothesis.
- **`skills/deception-detection/SKILL.md`** — Use when author has high stakes in the verdict. Distinguishes honest gaps from deliberate concealment.
- **`skills/verdict-verification/SKILL.md`** — Mandatory gate before issuing any VERDICT block. 18-point checklist + Premortem.

## Operational Modes (v2.5)

Modes are auto-selected in Phase 0 — user never declares them explicitly:

- **STANDARD**: N=1 solution, creation/validation → full protocol
- **FAST_TRACK**: Scale=Conceptual Idea + single domain → 4 levels, 3 blocks
- **COMPARATIVE**: N≥2 solutions → independent analysis + Comparison Matrix + Cross Verdict
- **OPTIMIZATION**: improving existing → standard + baseline audit + PROJECTION_MATRIX

COMPARATIVE + OPTIMIZATION combinable. FAST_TRACK exclusive.

## How to use this agent

### Option A — Claude.ai Projects
Paste `prompts/system_prompt.md` into Project Instructions.

### Option B — Claude API
```python
import anthropic
with open("prompts/system_prompt.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=8192,
    system=system_prompt,
    messages=[{"role": "user", "content": "Here is my proposal: [YOUR PROPOSAL]"}]
)
```

## Rules for extending this agent

1. Any modification must increment the version in `CHANGELOG.md`
2. Every candidate version must be self-audited before publication — REPORT_ID logged in CHANGELOG
3. Do not add instructions that soften the critical tone
4. Domain variants go in `prompts/system_prompt_[domain].md`
5. The ES/EN terminology map must be maintained in any language variant
6. New skills go in `skills/[skill-name]/SKILL.md` and must be referenced in this file

## Protocol Status

**ACTIVE — v2.6.0** | See `docs/deprecation.md` for deprecation conditions.
