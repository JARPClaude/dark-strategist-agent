# CLAUDE.md — Dark Strategist Agent
# Version: 2.8.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 2.8.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent

---

## Agent Hierarchy

```
N0 — Agente Forense Orquestador (AFO)
      orchestrator/tribunal.py
      └── Directs, consolidates, emits unified verdict

N1 — Agentes Forenses (parallel, blind to each other)
      1 / 3 / 5 / 7 agents (Swarm Activation Score)

N2 — Sub-agentes Forenses
      Permanent: 8 UNITs from catalog
      Temporary: dynamic → SUB_AGENT_EXPANSION_RECOMMENDED
```

---

## Repository Structure

```
dark-strategist-agent/
├── README.md
├── CLAUDE.md
├── CHANGELOG.md
├── DEPLOY.md
├── prompts/                         ← 15 system prompts
│   ├── system_prompt.md
│   ├── system_prompt_router.md
│   ├── system_prompt_trading.md
│   ├── system_prompt_legal.md
│   ├── system_prompt_code.md
│   ├── system_prompt_financial.md
│   ├── system_prompt_cloud.md
│   ├── system_prompt_cybersecurity.md
│   ├── system_prompt_agro.md
│   ├── system_prompt_realestate.md
│   ├── system_prompt_science.md
│   ├── system_prompt_media.md
│   ├── system_prompt_ecommerce.md
│   ├── system_prompt_telecom.md
│   └── system_prompt_publicsector.md
├── orchestrator/                    ← Full Python pipeline
│   ├── main.py                      ← Entry point
│   ├── tribunal.py                  ← AFO (NEW v2.8.0)
│   ├── budget_controller.py         ← NEW v2.8.0
│   ├── sub_agent_spawner.py         ← NEW v2.8.0
│   ├── verdict_synthesizer.py       ← NEW v2.8.0
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   └── config.example.json
├── infrastructure/
│   └── cloud_function/
│       ├── main.py
│       └── requirements.txt
├── docs/
│   └── sat_intelligence_doctrine.md
└── skills/
    ├── kac-assumption-audit/SKILL.md
    ├── ach-competing-explanations/SKILL.md
    ├── deception-detection/SKILL.md
    └── verdict-verification/SKILL.md
```

---

## Tribunal Mode — Swarm Activation Score

| Verdict from initial audit | Mode | N1 Agents |
|---------------------------|------|-----------|
| SOLID / VIABLE WITH ADJUSTMENTS | SINGLE | 1 |
| VIABLE WITH CRITICAL CORRECTIONS | TRIBUNAL_LIGHT | 3 |
| INVIABLE | TRIBUNAL_FULL | 5 |
| INVIABLE + War Room | TRIBUNAL_MAX | 7 |

---

## Usage

```bash
# Single mode
python main.py --document doc.txt

# Tribunal auto-size
python main.py --document doc.txt --tribunal

# Tribunal forced size
python main.py --document doc.txt --tribunal --agents 5

# Verbose (budget summary)
python main.py --document doc.txt --tribunal --verbose

# Domain expansion report
python main.py --report
```

---

## Budget Control

```json
"tribunal": {
    "max_agents": 7,
    "max_calls_total": 30,
    "max_n2_per_n1": 3,
    "alert_at_percent": 80
}
```

---

## Skills

- `skills/kac-assumption-audit/SKILL.md` — Before any FATAL/SERIOUS
- `skills/ach-competing-explanations/SKILL.md` — When 2+ contradictory conclusions
- `skills/deception-detection/SKILL.md` — When author has high stakes
- `skills/verdict-verification/SKILL.md` — Mandatory before VERDICT block

---

## Rules for extending

1. Increment version in CHANGELOG.md on any modification
2. Self-audit every candidate version — REPORT_ID logged
3. Do not soften the critical tone
4. Domain variants → `prompts/system_prompt_[domain].md`
5. New domain prompts must be registered in `system_prompt_router.md`
6. New skills → `skills/[skill-name]/SKILL.md` + reference here
7. Infrastructure → `orchestrator/` or `infrastructure/`
8. The name `dark-strategist-agent` does not change under any circumstance

---

## Roadmap

- ✅ v2.6.0 — SAT Intelligence Doctrine + 4 Audit Skills
- ✅ v2.6.1 — Trading + Legal Domain Variants
- ✅ v2.7.0 — Autonomous Router + 11 Domains + Infrastructure
- ✅ v2.8.0 — AFO + Tribunal Adversarial
- 🔲 v2.9.0 — Phase 3: Simulación Social Masiva (SSM)

---

**ACTIVE — v2.8.0**
