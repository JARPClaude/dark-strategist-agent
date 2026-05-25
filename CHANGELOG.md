# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.2.1] — 2026-05-24

### Patch — B2 Sub-batch Fixes (DS-CERT-v3.2.0 batch / PA-20260524-002 / B2/B9)

Triggered by the JARP DEEP Level 1 audit batch `DS-CERT-v3.2.0` executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001). Sub-batch B2/B9 found 1 CRITICAL + 2 SERIOUS findings affecting `prompts/system_prompt.md` and `prompts/system_prompt_router.md`. This patch resolves the bloqueantes; remaining MODERATE findings are deferred to v3.3.

#### Resolved findings

**🔴 CRITICAL — B2.5 (router):** PROMPT CATALOG and Step 2 keyword extraction had not been updated since v2.7.0-ROUTER (12/05/2026). 6 of 20 domain prompts (P15 medical, P16 marketing, P17 operations, P18 hr, P19 strategy, P20 startup) were physically present in `prompts/` but unreachable via routing — 30% of the catalog was operationally inaccessible. A user submitting documents with these domains' classic signals would receive zero keyword matches and fall back to UNKNOWN_DOMAIN, then receive DYNAMIC_TEMPORARY using the General prompt instead of the specialized domain audit. The final block would emit `DOMAIN_EXPANSION_RECOMMENDED` proposing the creation of a prompt file that already existed.

- Extended PROMPT CATALOG with P15-P20 rows.
- Extended Step 2 keyword catalog with domain-specific signals (clinical trial, HIPAA, FDA, EHR for medical; CAC, LTV, ROAS, funnel for marketing; supplier concentration, bottleneck, SOP, throughput for operations; pay equity, attrition, DEI for HR; competitive moat, five forces, M&A thesis for strategy; PMF, runway, CAC payback, Series A/B/C for startup).
- Added Disambiguation Rules section for overlapping signals (MRR cloud/startup; TAM/SAM/SOM strategy/startup; CAC/LTV marketing/startup; SoD cybersecurity/operations).
- Added new routing rule R8: catalog completeness — any prompt physically present in `prompts/` must be reachable via Step 2 keywords; new domain prompts trigger mandatory router patch in the same release.

**🟠 SERIOUS — B2.1 (system_prompt.md):** The file header stamped version `2.5.1`, while the composed agent was at v3.2.0. The prompt's architecture description corresponded to v2.5.1 and did NOT mention Tribunal Transversal (v3.0), AFO/Sub-Agent Spawner (v2.8), AAD (v3.2), GOAPPlanner (v3.1), BudgetController, or VerdictSynthesizer. A reader of the prompt in isolation believed the agent was v2.5.1.

- Updated version stamp from `2.5.1` to `3.2.0`.
- Added section `ARCHITECTURAL LAYERS — v3.2.0` documenting composition: base layer (this file) + skills layer (5 skills with version) + orchestration layer (`main.py`, `catalogs.py`, `tribunal*.py`) + domain layer (P02-P20 via router) + default model `claude-opus-4-7` + hard limits (Tribunal_MAX=7, max_calls_total=40, max_n2_per_n1=3, aad_max_rounds=3) + backward compatibility statement.
- Updated final status block to reflect v3.2.0 composed architecture and default model.

**🟠 SERIOUS — B2.6 (router):** Router version stamp `2.7.0-ROUTER` would have remained out of sync with the composed agent v3.2.0 even after B2.5 fix. No protocol governance rule bound the two version labels.

- Bumped router header to `Version: 3.2.0-ROUTER` and final status to `[PROTOCOL_STATUS: ACTIVE — v3.2.0-ROUTER]`.
- Updated `CATALOG_VERSION` to `3.2.0 — 19 domain prompts + 1 base (P01 General)`.
- Added rule in `system_prompt.md` §4.14 PROTOCOL GOVERNANCE: router version stamp must match composed agent minor version at all times; mismatch is a SERIOUS finding under self-audit.

#### Findings deferred to v3.3 (non-blocking)

- **🟡 B2.2** — §4.X cross-reference scheme not fully resolved internally (some §4.X items defined inline, others reference external docs, others undefined location). Resolution: build "Section 4 — Reference Index" mapping every §4.X to its location.
- **🟡 B2.3** — Rule 09 defined in two sections (SEVERITY TAXONOMY + BEHAVIORAL RULES) with consistent but non-identical wording. Resolution: consolidate in ONE location with cross-reference.
- **🟡 B2.4** — No long-context degradation mitigation mechanism (no anti-degradation reiteration of Rules 01/04/10 across long sessions). Resolution: add `ASEPTIC_INTEGRITY` reiteration to SESSION STATE.
- **🟡 B2.7** — UNKNOWN_DOMAIN protocol Phase B/C boundary unmarked (no `[AUDIT_REPORT_END]` marker between audit findings and expansion recommendation). Resolution: add explicit closing marker before Phase C.

#### Cascade impact recorded

- `PA-20260426-002` (Dark Strategist v2.5.1 certification, issued by `prompt-architect-agent` v1.0.0 before its decertification) → remains **SUSPECT**. Will be **VOID** upon successful completion of `DS-CERT-v3.2.0` batch and emission of v3.2.1 certification.
- Sub-batches B0/B9 (Self-Audit of auditor — completed) and B1/B9 (5 DS Skills — passed with notes) remain valid against `PA-20260524-002` master.
- Sub-batch B2/B9 status moves from DENIED → re-audit pending against this patch.

#### Files modified

- `prompts/system_prompt.md` — v2.5.1 stamp → v3.2.0 + ARCHITECTURAL LAYERS section + §4.14 router-stamp consistency rule
- `prompts/system_prompt_router.md` — v2.7.0-ROUTER → v3.2.0-ROUTER + 6 new catalog rows + extended keyword catalog + Disambiguation Rules + R8 rule
- `CHANGELOG.md` — this entry

#### Version bump rationale

Patch (`3.2.0` → `3.2.1`). The changes resolve declared gaps in v3.2.0 (router missed 6 domains added in v3.0 + v3.2.0) and align version stamps. No new agent capabilities. No architectural change. Patch is the honest bump — neither minor (would imply new features) nor major (would imply architecture change).

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

**Total domains: 20** (P01 General + P02-P15 fourteen pre-v3.0 domains + Medical added in v3.0 + 5 new in v3.2)

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

#### Patch — 2026-05-23 (documental, no version bump)

- Fixed inconsistent domain count claim in v3.2.0 section: previous text stated "Total domains: 21 (16 previous + Medical added in v3.0 + 5 new in v3.2)" — arithmetic incorrect and inconsistent with the 20-row Domain Catalog table. Corrected to "Total domains: 20".
- Default LLM model in `orchestrator/main.py` and `orchestrator/config.example.json` updated from `claude-opus-4-6` to `claude-opus-4-7` (current Anthropic Opus flagship as of 23/05/2026).

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
