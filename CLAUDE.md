# CLAUDE.md — Dark Strategist Agent
# Version: 2.9.0

## What is this repo

`dark-strategist-agent` is THE SOVEREIGN ADVERSARY — a forensic audit agent and adversarial orchestrator.

**Version:** 2.9.0 — Major Release
**License:** MIT — Open Source
**Repository:** https://github.com/JARPClaude/dark-strategist-agent
**Name:** dark-strategist-agent — immutable, does not change under any circumstance.

---

## Full Pipeline

```
FASE 1 — AUDITORÍA FORENSE (Tribunal Adversarial)
  N0: Agente Forense Orquestador (AFO)
      ↓ routes document, calculates Swarm Score
  N1: Agentes Forenses (1/3/5/7 — parallel, blind)
      ↓ each spawns N2 sub-agents as needed
  N2: Sub-agentes Forenses
      Permanent: 8 UNITs | Temporary: dynamic → notify owner
      ↓ Verdict Synthesizer consolidates
  VEREDICTO FORENSE UNIFICADO emitted
      ↓ (if VIABLE)

FASE 2 — SIMULACIÓN SOCIAL MASIVA (SSM)
  PersonaFactory generates domain-specific personas
      ↓ 4 rounds of interaction
  Round 1: Individual opinion (blind)
  Round 2: Exchange → stance changes
  Round 3: Coalition formation
  Round 4: Dominant coalition acts
      ↓
  REPORTE DE IMPACTO SOCIAL emitted
      ↓

FASE 3 — TRANSPARENCY REPORT
  Full operational metadata:
  AFO + Tribunal + Sub-agents + SSM + Budget + Notifications
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
├── orchestrator/
│   ├── main.py                      ← Entry point (v2.9.0)
│   ├── tribunal.py                  ← AFO + Tribunal + SSM integration
│   ├── budget_controller.py         ← Tribunal budget
│   ├── sub_agent_spawner.py         ← N2 permanent + temporary
│   ├── verdict_synthesizer.py       ← Multi-verdict consolidation
│   ├── router.py
│   ├── notifier.py
│   ├── sheets_logger.py
│   ├── requirements.txt
│   ├── config.example.json
│   └── ssm/                         ← NEW v2.9.0
│       ├── __init__.py              ← SimulacionSocialMasiva entry
│       ├── persona_factory.py       ← Domain persona generation
│       ├── interaction_engine.py    ← 4 rounds orchestration
│       ├── social_report.py         ← REPORTE DE IMPACTO SOCIAL
│       └── budget_ssm.py            ← SSM budget control
├── infrastructure/
│   └── cloud_function/
├── docs/
└── skills/
```

---

## CLI Reference

```bash
# Single mode
python main.py --document doc.txt

# Tribunal (auto-size via Swarm Activation Score)
python main.py --document doc.txt --tribunal

# Tribunal forced size
python main.py --document doc.txt --tribunal --agents 5

# Tribunal + SSM (MESO = 20 personas, default)
python main.py --document doc.txt --tribunal --ssm

# Tribunal + SSM forced scale
python main.py --document doc.txt --tribunal --ssm --ssm-scale MACRO

# Full verbose
python main.py --document doc.txt --tribunal --ssm --verbose

# Domain expansion report
python main.py --report
```

---

## SSM Activation Logic

| Tribunal Verdict | SSM |
|-----------------|-----|
| 🔴 INVIABLE | ❌ Blocked |
| 🟠 VIABLE WITH CRITICAL CORRECTIONS | ✅ Auto |
| 🟡 VIABLE WITH ADJUSTMENTS | ✅ Auto |
| 🟢 SOLID UNDER PRESSURE | ⚙️ Optional (--ssm flag) |

---

## Swarm Activation Score

| Verdict | Tribunal Mode | Agents |
|---------|--------------|--------|
| SOLID / VIABLE WITH ADJUSTMENTS | SINGLE | 1 |
| VIABLE WITH CRITICAL CORRECTIONS | TRIBUNAL_LIGHT | 3 |
| INVIABLE | TRIBUNAL_FULL | 5 |
| INVIABLE + War Room | TRIBUNAL_MAX | 7 |

---

## Budget Configuration

```json
"tribunal": {
    "max_agents": 7,
    "max_calls_total": 30,
    "max_n2_per_n1": 3,
    "alert_at_percent": 80
},
"ssm": {
    "max_personas": 20,
    "max_rounds": 4,
    "max_parallel_personas": 5,
    "alert_at_percent": 80
}
```

---

## Roadmap

| Phase | Version | Status |
|-------|---------|--------|
| SAT Intelligence Doctrine + Skills | v2.6.0 | ✅ |
| Domain Variants + Infrastructure | v2.7.0 | ✅ |
| AFO + Tribunal Adversarial | v2.8.0 | ✅ |
| SSM + Transparency Report | v2.9.0 | ✅ |

---

## Rules for extending

1. Increment version in CHANGELOG.md
2. Self-audit every candidate version
3. Do not soften the critical tone
4. Domain variants → `prompts/system_prompt_[domain].md`
5. New prompts must be registered in `system_prompt_router.md`
6. New skills → `skills/[skill-name]/SKILL.md`
7. SSM persona sets → `orchestrator/ssm/persona_factory.py`
8. The name `dark-strategist-agent` does not change under any circumstance

**ACTIVE — v2.9.0**
