# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.2.0] — 2026-05-15

### Major Release — Adaptive Autonomous Drive + 5 New Domains

#### 1. Skill: Adaptive Autonomous Drive

**`skills/adaptive-autonomous-drive/SKILL.md`**

Formalizes the autonomous operational layer of Dark Strategist as an official skill. The skill grants the AFO and all forensic agents the capacity to expand analysis beyond the initial prompt, generate internal goals dynamically, and activate sub-agents without user instruction.

Six internal modules:
- GoalEngine — maintains and generates internal audit goals (G1-G5)
- MotivationModel — determines where highest adversarial value remains
- StateMemory — registers analysis progress to avoid redundancy
- AutonomousLoop — executes additional rounds without user intervention
- SafetyGuard — hard rules preventing uncontrolled autonomy
- SelfEvaluation — forces self-assessment before closing analysis

System prompt integration block provided. Pseudocode provided. Fully integrated with AFO, TribunalTransversal, SubAgentSpawner, and GOAPPlanner.

Naming convention: `adaptive-autonomous-drive` (kebab-case, English — consistent with existing skills).

---

#### 2. Five New Domain Variants

| File | Domain | Primary Unit | Rules |
|------|--------|--------------|-------|
| `system_prompt_marketing.md` | Marketing | UNIT-MARKET | MK1–MK4 |
| `system_prompt_operations.md` | Operations | UNIT-TECH | OP1–OP4 |
| `system_prompt_hr.md` | Human Resources | UNIT-COMPLIANCE | HR1–HR4 |
| `system_prompt_strategy.md` | Strategy | UNIT-MARKET | ST1–ST4 |
| `system_prompt_startup.md` | Startup | UNIT-QUANT | SU1–SU5 |

Each domain includes: document taxonomy (7 types), Phase 0 intake protocol, severity taxonomy with domain rules, 7-level forensic analysis, failure catalog with auto-severity, and War Room orchestration table.

**Marketing (P16):** CAC attribution audit, ROAS validation, funnel math, claim verifiability. RULE MK1: growth >50% MoM without basis → SERIOUS. RULE MK3: >70% budget single channel → SERIOUS.

**Operations (P17):** Bottleneck detection, supplier concentration, SoD compliance, SOP executability. RULE OP1: single supplier >70% critical input → FATAL. RULE OP3: linear cost assumption in scaling → SERIOUS.

**Human Resources (P18):** Pay equity analysis, labor law compliance, culture claim validation, performance bias detection. RULE HR1: pay gap without documented justification → FATAL. RULE HR4: financial approval and execution in same role → FATAL (SoD).

**Strategy (P19):** Assumption single-point-of-failure check, mirror imaging detection, competitive response modeling. RULE ST1: single assumption that invalidates entire plan → FATAL. RULE ST2: competitive analysis ignoring adjacent disruptors → SERIOUS.

**Startup (P20):** CAC/LTV payback, PMF retention check, TAM methodology audit, runway modeling. RULE SU1: CAC payback >24 months without improvement path → FATAL. RULE SU2: PMF claim without 90-day retention data → FATAL.

---

#### 3. Catalogs Updated

**`orchestrator/catalogs.py`** — v3.2.0:
- ROLE_CATALOG: 5 new domains added (Marketing, Operations, Human Resources, Strategy, Startup) — each with Rol agents + Forense agents
- SSM_CATALOG: 5 new domain persona sets added
- DOMAIN_MAP: 30+ new keyword mappings for new domains
- DOMAIN_TOOLS: 5 new domain tool sets added
- SKILLS_CATALOG: new section — maps all 5 active skills including adaptive-autonomous-drive

**Total domains: 21** (16 previous + Medical added in v3.0 + 5 new in v3.2)

---

#### Domain Catalog — Complete Reference v3.2.0

| ID | Prompt | Domain | Primary Unit |
|----|--------|--------|--------------|
| P01 | system_prompt.md | General | Contextual |
| P02 | system_prompt_trading.md | Trading | UNIT-QUANT |
| P03 | system_prompt_legal.md | Legal (12 sub-areas) | UNIT-INQUISITOR |
| P04 | system_prompt_code.md | Code | UNIT-TECH |
| P05 | system_prompt_financial.md | Financial | UNIT-QUANT |
| P06 | system_prompt_cloud.md | Cloud | UNIT-TECH |
| P07 | system_prompt_cybersecurity.md | Cybersecurity | UNIT-TECH |
| P08 | system_prompt_agro.md | Agriculture | UNIT-BIO |
| P09 | system_prompt_realestate.md | Real Estate | UNIT-MARKET |
| P10 | system_prompt_science.md | Science | UNIT-QUANT |
| P11 | system_prompt_media.md | Media | UNIT-MARKET |
| P12 | system_prompt_ecommerce.md | E-Commerce | UNIT-MARKET |
| P13 | system_prompt_telecom.md | Telecom | UNIT-GEO |
| P14 | system_prompt_publicsector.md | Public Sector | UNIT-COMPLIANCE |
| P15 | system_prompt_medical.md | Medical | UNIT-INQUISITOR |
| P16 | system_prompt_marketing.md | Marketing | UNIT-MARKET |
| P17 | system_prompt_operations.md | Operations | UNIT-TECH |
| P18 | system_prompt_hr.md | Human Resources | UNIT-COMPLIANCE |
| P19 | system_prompt_strategy.md | Strategy | UNIT-MARKET |
| P20 | system_prompt_startup.md | Startup | UNIT-QUANT |

---

#### Skills Catalog — Complete Reference v3.2.0

| Skill | File | Version |
|-------|------|---------|
| kac-assumption-audit | skills/kac-assumption-audit/SKILL.md | v2.6.0 |
| ach-competing-explanations | skills/ach-competing-explanations/SKILL.md | v2.6.0 |
| deception-detection | skills/deception-detection/SKILL.md | v2.6.0 |
| verdict-verification | skills/verdict-verification/SKILL.md | v2.6.0 |
| adaptive-autonomous-drive | skills/adaptive-autonomous-drive/SKILL.md | v3.2.0 |

---

## [3.1.0] — 2026-05-15

GOAP A* Planner + Legal 12 Sub-area Taxonomy (L01-L12 including L07 AI Governance).

---

## [3.0.0] — 2026-05-14

Tribunal Transversal + Dynamic Prompt Engine + Pydantic VerdictOutput + Medical domain.

---

## [2.9.0] — 2026-05-13

SSM + Transparency Report. 4-round interaction. MICRO/MESO/MACRO.

---

## [2.8.0] — 2026-05-13

AFO + Tribunal Adversarial. Budget Controller. Sub-Agent Spawner. Verdict Synthesizer.

---

## [2.7.0] — 2026-05-12

Autonomous Router + 11 Domain Prompts + Python Infrastructure.

---

## [2.6.x] — 2026-05-05/06

SAT Intelligence Doctrine + 4 Skills. Trading + Legal domain variants.

---

## [2.0.0] — 2026-04-19

Foundation: system prompt, Phase 0, severity taxonomy, Blocks 0–6.
