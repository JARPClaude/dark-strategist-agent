# CLAUDE.md — Dark Strategist Agent
# Instructions for Claude when operating within this repository

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 2.7.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent

---

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md                                    ← This file
├── CHANGELOG.md
├── DEPLOY.md                                    ← NEW v2.7.0
├── prompts/
│   ├── system_prompt.md                         ← Base — sectoral agnostic
│   ├── system_prompt_router.md                  ← NEW v2.7.0 — Router Agent
│   ├── system_prompt_trading.md                 ← v2.6.1
│   ├── system_prompt_legal.md                   ← v2.6.1
│   ├── system_prompt_code.md                    ← NEW v2.7.0
│   ├── system_prompt_financial.md               ← NEW v2.7.0
│   ├── system_prompt_cloud.md                   ← NEW v2.7.0
│   ├── system_prompt_cybersecurity.md           ← NEW v2.7.0
│   ├── system_prompt_agro.md                    ← NEW v2.7.0
│   ├── system_prompt_realestate.md              ← NEW v2.7.0
│   ├── system_prompt_science.md                 ← NEW v2.7.0
│   ├── system_prompt_media.md                   ← NEW v2.7.0
│   ├── system_prompt_ecommerce.md               ← NEW v2.7.0
│   ├── system_prompt_telecom.md                 ← NEW v2.7.0
│   └── system_prompt_publicsector.md            ← NEW v2.7.0
├── orchestrator/                                ← NEW v2.7.0
│   ├── main.py
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   └── config.example.json
├── infrastructure/                              ← NEW v2.7.0
│   └── cloud_function/
│       ├── main.py
│       └── requirements.txt
├── examples/
├── docs/
│   └── sat_intelligence_doctrine.md
└── skills/
    ├── kac-assumption-audit/SKILL.md
    ├── ach-competing-explanations/SKILL.md
    ├── deception-detection/SKILL.md
    └── verdict-verification/SKILL.md
```

---

## Which System Prompt to Use

| Use Case | File |
|----------|------|
| Unknown / General | `prompts/system_prompt.md` |
| Auto-detect (API) | `prompts/system_prompt_router.md` |
| Trading / Bot | `prompts/system_prompt_trading.md` |
| Legal / Compliance | `prompts/system_prompt_legal.md` |
| Code / ABAP / Architecture | `prompts/system_prompt_code.md` |
| Financial / M&A / Valuation | `prompts/system_prompt_financial.md` |
| Cloud / SaaS / PaaS / IaaS | `prompts/system_prompt_cloud.md` |
| Cybersecurity / Systems Audit | `prompts/system_prompt_cybersecurity.md` |
| Agriculture / Livestock / Mining | `prompts/system_prompt_agro.md` |
| Real Estate / Property | `prompts/system_prompt_realestate.md` |
| Science / R&D / Clinical | `prompts/system_prompt_science.md` |
| Media / Content Creators | `prompts/system_prompt_media.md` |
| E-Commerce / Marketplaces | `prompts/system_prompt_ecommerce.md` |
| Telecom / Infrastructure | `prompts/system_prompt_telecom.md` |
| Public Sector / Government | `prompts/system_prompt_publicsector.md` |

### Autonomous (API + Orchestrator)

```bash
python orchestrator/main.py --document path/to/document.txt
```

---

## Router & UNKNOWN_DOMAIN Protocol

When no catalog prompt matches:
1. Router activates `UNKNOWN_DOMAIN_DETECTED`
2. Builds dynamic calibration on `system_prompt.md`
3. Executes full 7-level audit
4. Appends `DOMAIN_EXPANSION_RECOMMENDED` to report
5. Auto-dispatches: Slack → GitHub Issue → Google Sheets

---

## Skills (v2.6.0)

- `skills/kac-assumption-audit/SKILL.md` — Mandatory before FATAL/SERIOUS
- `skills/ach-competing-explanations/SKILL.md` — When 2+ contradictory conclusions
- `skills/deception-detection/SKILL.md` — When author has high stakes
- `skills/verdict-verification/SKILL.md` — Mandatory gate before VERDICT block

---

## Rules for extending this agent

1. Increment version in `CHANGELOG.md` on any modification
2. Self-audit every candidate version — REPORT_ID logged in CHANGELOG
3. Do not soften the critical tone
4. Domain variants → `prompts/system_prompt_[domain].md`
5. New domain prompts must be registered in `system_prompt_router.md`
6. New skills → `skills/[skill-name]/SKILL.md` + reference here
7. Infrastructure → `orchestrator/` or `infrastructure/`

---

## Protocol Status

**ACTIVE — v2.7.0** | See `docs/deprecation.md` for deprecation conditions.
