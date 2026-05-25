# CHANGELOG — Dark Strategist Agent

All significant changes documented here.
Format: [VERSION] — DATE — Description

---

## [3.2.2] — 2026-05-24

### Patch — DS-CERT-v3.2.0 Batch Closure (PA-20260524-002)

Triggered by the JARP DEEP Level 1 audit batch `DS-CERT-v3.2.0` executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001). Sub-batches B3 through B8 found 19 SERIOUS bloqueantes across 17 of 19 domain variants. v3.2.2 resolves all 19 via a single architectural intervention — the Domain Variant Contract (§4.14.1) — applied uniformly across the catalog.

#### Architectural intervention — §4.14.1 Domain Variant Contract (new)

Added a new sub-section to `system_prompt.md` §4.14 PROTOCOL GOVERNANCE: **Domain Variant Contract**. The Contract binds every `prompts/system_prompt_<domain>.md` to four sub-contracts:

- **Output Format Contract** — every variant must declare an `## OUTPUT FORMAT` section that explicitly inherits BLOCK 0–6 from base. Variants may extend BLOCK 1 with domain-specific fields and may add BLOCKs ≥7 for domain-mandatory sections (e.g., Legal BLOCK 7 = AI_DISCLAIMER). Implicit inheritance is no longer permitted.
- **Footer Contract** — every variant ends with the canonical footer block:
  ```
  [PROTOCOL_STATUS: ACTIVE — vX.Y.Z-DOMAIN]
  [BASE_PROTOCOL: system_prompt.md vA.B.C]
  [CONTRACT: §4.14.1 — Domain Variant Contract]
  ```
- **Severity Mapping Contract** — Failure Catalog rows must be internally consistent with the variant's Severity Taxonomy definitions. Geofence escalation rules must be monotonic — severity escalates by N tiers capped at FATAL, never skipping tiers or leaving input severities undefined.
- **Naming Convention Contract** — generic rules use numeric IDs (RULE 01–10 reserved for base). Domain-specific rules use 2-letter prefix + number: T for Trading, LG for Legal, CY for Cybersecurity, CL for Cloud, A for Agro, RE for RealEstate, S for Science, M for Media, EC for Ecommerce, TC for Telecom (distinct from T), PS for PublicSector, MD for Medical, MK for Marketing, OP for Operations, HR for HR, ST for Strategy, SU for Startup, C for Code, F for Financial. Two-letter prefixes are immutable.
- **Versioning Contract** — domain variant version stamps track the composed-agent minor version; BASE_PROTOCOL footer references must always point to the current composed-agent base version.

#### Resolved findings — 19 SERIOUS bloqueantes

**Pattern #SIS-1 — Output Format absent (15 SERIOUS resolved):**
Variants P04 Code, P05 Financial, P06 Cloud, P07 Cybersecurity, P08 Agro, P09 RealEstate, P10 Science, P11 Media, P12 Ecommerce, P13 Telecom, P14 PublicSector, P15 Medical, P16 Marketing, P17 Operations, P18 HR, P19 Strategy, P20 Startup — all received an explicit `## OUTPUT FORMAT` section declaring base inheritance + domain extensions per the Contract. P02 Trading (already compliant) and P03 Legal (already compliant with BLOCK 7 AI_DISCLAIMER) updated for consistency only.

**Pattern #SIS-2 — Naming collision risk (15 LATENT resolved):**
All domain variants renumbered to the §4.14.1 Naming Convention. Specifically: P13 Telecom rules T1-T4 → TC01-TC04 (eliminates direct collision with P02 Trading T1-T3). All other variants normalized to 2-digit padded numbering (e.g., CY1 → CY01, MD1 → MD01, ST1 → ST01).

**Pattern #SIS-3 — BASE_PROTOCOL footer inconsistency (15 LATENT resolved):**
All 19 variants now declare the canonical footer per the Footer Contract, pointing to `system_prompt.md v3.2.2`. Stale references (v2.5.1, v2.6.1) and missing references (P04 Code, P05 Financial, others) all corrected uniformly.

**Punctual fix — P03 Legal Geofence non-monotonic (1 SERIOUS resolved — B3.2.1):**
Geofence severity calibration table replaced with monotonic tier-shift rules. Each qualifying condition adds N tiers to underlying finding severity, capped at FATAL. Applied conditions stack additively. Pre-shift severity recorded in finding for traceability. The previous fixed-mapping rows (which left SERIOUS input severities undefined under "no independent judiciary") are replaced.

**Punctual fix — P08 Agro Yield mis-classified (1 SERIOUS resolved — B4 finding):**
"Yield above regional benchmark without documented justification" reclassified from 🔴 FATAL → 🟠 SERIOUS. The previous FATAL contradicted the variant's own severity taxonomy definition (FATAL = biological impossibility). Yield overestimation is overstatement, not impossibility. With documented justification (technical irrigation, improved seeds), the finding is removed entirely rather than escalated.

#### Findings deferred to v3.3 (non-blocking)

- 38 MODERATE findings from the batch (sub-area Failure Catalogs missing for Legal L05/L06/L09/L10/L11/L12; multi-day batch resumption rules in prompt-architect-agent; comparative mode Phase 0 collection scope; etc.)
- 22 LATENT findings (most resolved at root by §4.14.1 — residuals tracked for v3.3)
- 1 LATENT residual from B2-RE.1 ("v2.5.1 forensic base" wording in ARCHITECTURAL LAYERS section)

#### Cascade impact recorded

- `PA-20260426-002` (Dark Strategist v2.5.1 certification, issued by `prompt-architect-agent` v1.0.0 before its decertification) → **VOID** as of this release. Superseded by v3.2.2 certification pending re-audit.
- The DS-CERT-v3.2.0 batch master `PA-20260524-002` is closed with this release. New certification under v3.2.2 will require a re-audit pass against the auditor v1.1.0 standards — to be scheduled in the next session.

#### Files modified

- `prompts/system_prompt.md` — v3.2.0 → v3.2.2 + §4.14.1 Domain Variant Contract added + BLOCK 1 dual-language label rule
- `prompts/system_prompt_trading.md` — v2.6.0-TRADING → v3.2.2-TRADING + footer
- `prompts/system_prompt_legal.md` — v3.1.0-LEGAL → v3.2.2-LEGAL + monotonic Geofence + LG-series naming + footer
- `prompts/system_prompt_code.md` — v2.7.0-CODE → v3.2.2-CODE + Output Format + C-series + footer + ABAP guideline reference
- `prompts/system_prompt_financial.md` — v2.7.0-FINANCIAL → v3.2.2-FINANCIAL + Output Format + F-series + threshold ladder + footer
- `prompts/system_prompt_cloud.md` — v2.7.0-CLOUD → v3.2.2-CLOUD + Output Format + CL-series + footer
- `prompts/system_prompt_cybersecurity.md` — v2.7.0-CYBERSECURITY → v3.2.2-CYBERSECURITY + Output Format + CY-series + footer
- `prompts/system_prompt_agro.md` — v2.7.0-AGRO → v3.2.2-AGRO + Output Format + A-series + Yield reclassified SERIOUS + footer
- `prompts/system_prompt_realestate.md` — v2.7.0-REALESTATE → v3.2.2-REALESTATE + Output Format + RE-series + footer
- `prompts/system_prompt_science.md` — v2.7.0-SCIENCE → v3.2.2-SCIENCE + Output Format + S-series + footer
- `prompts/system_prompt_media.md` — v2.7.0-MEDIA → v3.2.2-MEDIA + Output Format + M-series + footer
- `prompts/system_prompt_ecommerce.md` — v2.7.0-ECOMMERCE → v3.2.2-ECOMMERCE + Output Format + EC-series + footer
- `prompts/system_prompt_telecom.md` — v2.7.0-TELECOM → v3.2.2-TELECOM + Output Format + TC-series (renamed from T to avoid Trading collision) + footer
- `prompts/system_prompt_publicsector.md` — v2.7.0-PUBLICSECTOR → v3.2.2-PUBLICSECTOR + Output Format + PS-series + footer
- `prompts/system_prompt_medical.md` — v3.0.0-MEDICAL → v3.2.2-MEDICAL + Output Format + MD-series + footer
- `prompts/system_prompt_marketing.md` — v3.2.0-MARKETING → v3.2.2-MARKETING + Output Format + MK-series + footer
- `prompts/system_prompt_operations.md` — v3.2.0-OPERATIONS → v3.2.2-OPERATIONS + Output Format + OP-series + footer
- `prompts/system_prompt_hr.md` — v3.2.0-HR → v3.2.2-HR + Output Format + HR-series + footer
- `prompts/system_prompt_strategy.md` — v3.2.0-STRATEGY → v3.2.2-STRATEGY + Output Format + ST-series + footer
- `prompts/system_prompt_startup.md` — v3.2.0-STARTUP → v3.2.2-STARTUP + Output Format + SU-series + footer
- `CHANGELOG.md` — this entry

Total files modified: **21** (1 base + 19 domain variants + CHANGELOG).

#### Version bump rationale

Patch (`3.2.1` → `3.2.2`). The changes resolve declared gaps in v3.2.0 (Output Format inconsistencies across the domain catalog, naming collision risks, footer drift). One architectural addition (§4.14.1 Contract) but no new agent capability, no orchestrator change, no new domain. Patch is the honest bump — neither minor (would imply new features) nor major (would imply architecture change). The Contract is governance enforcement of pre-existing intent.

---

## [3.2.1] — 2026-05-24

### Patch — B2 Sub-batch Fixes (DS-CERT-v3.2.0 batch / PA-20260524-002 / B2/B9)

Triggered by the JARP DEEP Level 1 audit batch `DS-CERT-v3.2.0` executed by `prompt-architect-agent` v1.1.0 (JARP_CERTIFIED PA-20260524-001). Sub-batch B2/B9 found 1 CRITICAL + 2 SERIOUS findings affecting `prompts/system_prompt.md` and `prompts/system_prompt_router.md`. This patch resolves the bloqueantes; remaining MODERATE findings are deferred to v3.3.

#### Resolved findings

**🔴 CRITICAL — B2.5 (router):** PROMPT CATALOG and Step 2 keyword extraction had not been updated since v2.7.0-ROUTER (12/05/2026). 6 of 20 domain prompts (P15 medical, P16 marketing, P17 operations, P18 hr, P19 strategy, P20 startup) were physically present in `prompts/` but unreachable via routing — 30% of the catalog was operationally inaccessible.

- Extended PROMPT CATALOG with P15-P20 rows.
- Extended Step 2 keyword catalog with domain-specific signals.
- Added Disambiguation Rules section for overlapping signals.
- Added new routing rule R8: catalog completeness.

**🟠 SERIOUS — B2.1 (system_prompt.md):** File header stamped v2.5.1 while composed agent was at v3.2.0.

- Updated version stamp from `2.5.1` to `3.2.0`.
- Added section `ARCHITECTURAL LAYERS — v3.2.0` documenting composition.
- Updated final status block.

**🟠 SERIOUS — B2.6 (router):** Router version stamp out of sync with composed agent.

- Bumped router header to `Version: 3.2.0-ROUTER`.
- Updated `CATALOG_VERSION` to `3.2.0 — 19 domain prompts + 1 base (P01 General)`.
- Added rule in `system_prompt.md` §4.14: router version stamp must match composed agent minor version.

---

## [3.2.0] — 2026-05-15

### Major Release — Adaptive Autonomous Drive + 5 New Domains

#### 1. Skill: Adaptive Autonomous Drive

**`skills/adaptive-autonomous-drive/SKILL.md`**

Formalizes the autonomous operational layer of Dark Strategist as an official skill. Six internal modules: GoalEngine, MotivationModel, StateMemory, AutonomousLoop, SafetyGuard, SelfEvaluation.

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

---

#### 3. Catalogs Updated

**`orchestrator/catalogs.py`** — v3.2.0:
- ROLE_CATALOG: 5 new domains added
- SSM_CATALOG: 5 new domain persona sets added
- DOMAIN_MAP: 30+ new keyword mappings for new domains
- DOMAIN_TOOLS: 5 new domain tool sets added
- SKILLS_CATALOG: maps all 5 active skills including adaptive-autonomous-drive

**Total domains: 20**

---

#### Patch — 2026-05-23 (documental, no version bump)

- Fixed inconsistent domain count claim in v3.2.0 section
- Default LLM model in orchestrator updated to `claude-opus-4-7`

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
