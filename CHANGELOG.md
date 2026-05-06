# CHANGELOG — Dark Strategist Agent

All significant changes to the system prompt and agent structure are documented here.
Format: [VERSION] — DATE — Description

---

## [2.6.0] — 2026-05-05

### Major Release — SAT Intelligence Doctrine + 4 New Audit Skills

**Source repos synthesized:**
- `Blevene/structured-analysis-skill` (Apache 2.0) — CIA Tradecraft Primer 2009 + Pherson & Heuer 3rd Ed. 2020
- `obra/superpowers` (MIT) — verification-before-completion methodology
- `affaan-m/everything-claude-code` — Agent-First orchestration philosophy (referenced in architecture)

---

#### New Files

1. **`docs/sat_intelligence_doctrine.md`** — Structured Analytic Techniques (SATs) adapted for forensic document auditing.
   - The Axioms: Externalization, Metacognition, Mindset Persistence, Satisficing, Decomposition, Simultaneous Hypotheses, Diagnostic Dominance, Proportional Effort
   - Cognitive Bias Map: 9 biases with specific corrections mapped to existing DS protocol elements
   - SAT Technique Map: 12 techniques cross-referenced to DS Agent levels and modes
   - Evidence Quality Framework: 3-dimension rating system (Source Reliability, Claim Credibility, Diagnostic Value)
   - Selection Logic: audit situation → technique routing table
   - The Meta-Law: proportional effort doctrine

2. **`skills/kac-assumption-audit/SKILL.md`** — Key Assumptions Check for document auditing.
   - Formalizes Level 3 (Assumptions) of the 7-level forensic protocol
   - 6-step protocol: Core Claim → Extract Premises → Challenge → Classify → Isolate Linchpins → Map to Findings
   - Assumption Classification Table output format
   - Linchpin assumption identification (load-bearing premises)
   - Iron Law: no FATAL or SERIOUS rating without completing KAC first

3. **`skills/ach-competing-explanations/SKILL.md`** — Analysis of Competing Explanations for document auditing.
   - ACH from the CIA tradition adapted to verdict competition
   - 5 mandatory hypotheses: H-VIABLE, H-INVIABLE, H-CONDITIONAL, H-NULL, H-DECEPTION
   - 8-step protocol including negative evidence, matrix construction, sensitivity analysis
   - Law of Diagnostic Dominance applied to finding quality
   - Iron Law: rank by inconsistency count — not confirmation count

4. **`skills/deception-detection/SKILL.md`** — Structured deception analysis for document auditing.
   - 5 checks: Mirror-Imaging, Selective Evidence, Framing Analysis, Adversarial Consistency, Counterfactual Integrity
   - Deception Severity Classification table with audit impact
   - Distinction between random weakness (incompetence) and structured concealment (deception)
   - Direct integration with UNIT-INQUISITOR and UNIT-PSYCH activation

5. **`skills/verdict-verification/SKILL.md`** — The final gate before any VERDICT block.
   - Adapted from obra/superpowers verification doctrine
   - Full checklist: Evidence Integrity, Root Cause vs. Symptom, Severity Consistency, Completeness, Premortem Gate, Output Format
   - 6-step gate function with Premortem stress-test mandatory
   - Iron Law: no VERDICT block without completing the checklist

---

#### Architecture Impact

- UNIT-PSYCH is now backed by a 9-bias cognitive map with specific technique corrections
- Level 3 (Assumptions) gains a formal protocol (KAC)
- War Room gains structured triggering conditions from ACH H-DECEPTION hypothesis
- Verdict issuance now has a mandatory pre-flight gate
- All new skills reference each other and the existing 7-level protocol — no orphaned documents

---

#### Pending — v2.6 Roadmap (unchanged)

- [ ] `prompts/system_prompt_legal.md` — legal/compliance domain variant
- [ ] `prompts/system_prompt_trading.md` — trading strategy domain variant
- [ ] COMPARATIVE MODE worked example (example_04)
- [ ] OPTIMIZATION MODE worked example (example_05)
- [ ] UNIT-PSYCH extended bias catalog

---

## [2.5.1] — 2026-04-25

### Patch Release — §4.22 Industry & Business Taxonomy

1. **docs/industry_taxonomy.md** — NEW document. Complete unified taxonomy for domain classification in Phase 0:
   - §4.22.A: 22 industries across 4 groups (Energía y Recursos Naturales, Manufactura y Construcción, Servicios y Conocimiento) — including E-commerce, Content Creators, R&D, and Public Sector
   - §4.22.B: 23 business lines (giros) across 5 categories (Comercial, Industrial, Servicios, Tecnológico y Digital, Gubernamental y Público)
   - §4.22.C: Giro → micro-agent supplementary mapping (complements §4.13)
   - §4.22.D: 7 Phase 0 classification examples with industry + giro + micro-agent notes
2. **prompts/system_prompt.md** — Phase 0 updated: DOMAIN field split into INDUSTRY (§4.22.A) + GIRO DE NEGOCIO (§4.22.B). Domain Classification Note added. Block 1 header updated to include Industry and Giro fields.
3. **prompts/system_prompt.md** — §4.6 Domain Calibration expanded: added Media/Content Creators, Real Estate, Telecommunications, Education, SaaS/Digital Business calibration rows. Added reference to full §4.22 taxonomy.
4. **prompts/system_prompt.md** — §4.12 Sectoral Agnosticism updated: explicitly references 22 industries and 23 giros de negocio.
5. **prompts/system_prompt.md** — §4.13 micro-agent matrix: added reference to §4.22.C for giro-based supplementary activation.

---

## [2.5.0] — 2026-04-25

### Major Version — 6 New Capabilities

1. **§4.16 MVP_THRESHOLD** — Minimum information gate before analysis proceeds.
2. **§4.17 Operational Modes** — 4 modes auto-selected: STANDARD, FAST_TRACK, COMPARATIVE, OPTIMIZATION.
3. **§4.18 COMPARATIVE_MODE** — N≥2 simultaneous solutions with Cross Verdict and deterministic ranking.
4. **§4.19 OPTIMIZATION_MODE + PROJECTION_MATRIX** — As-Is vs. To-Be audit with 4-scenario projections.
5. **§4.20 FAST_TRACK MODE** — Agile analysis for Conceptual Idea + single domain.
6. **§4.21 UNIT-PSYCH + Block 4 verifiable criteria** — Behavioral Bias Auditor micro-agent.

---

## [2.4.0] — 2026-04-24

### Self-Audit Reference: DS-20260423-001

1. Classification updated — OPEN SOURCE MIT License.
2. §4.6 Extractivo/Agro/Ganadero expanded.
3. Rule 01 corrected — Bloque 4, not Bloque 3.
4. §4.6 Auditoría de Sistemas / Ciberseguridad expanded.
5. §4.14 Protocol Governance added.
6. Footer updated with GitHub URL.
7. §4.15 Deprecation Clause added.

---

## [2.3.0] — 2026-04-21

1. Executive Summary updated to v2.3.
2. ES/EN Terminology Map in §4.4.
3. War Room Activation Threshold — 4 deterministic criteria.
4. Geofence Field expanded — 5 variables.
5. VERSION_TRACK Context Degradation — 3-step instruction.
6. UNIT-BIO extended to Livestock.
7. REPORT_ID Convention documented.

---

## [2.2.0] — 2026-04-20

1. Block Numbering synchronized.
2. Deterministic Verdict Logic — Block 6 decision table.
3. Rule 10 Evidence Standard — 3 explicit criteria.
4. NEGLECT_DETECTED Unlock Criteria + 3-attempt counter.
5. §4.13 Activation Matrix — 9 domain rows.
6. Block 5 Integrity Rule — no fabricated N% probability.
7. §4.6 Domain Expansion — Capital Markets, Systems Audit, Business/Commercial.

---

## [2.1.0] — 2026-04-20

Added: War Room (§4.11), Sectoral Agnosticism (§4.12), Micro-Agent Catalog (§4.13), Geofence Audit (§4.3.1), Sub-Protocol Unknown Domain, Epistemic Honesty (§4.3.2), Rule 09, Rule 10, NEGLECT_DETECTED, Red Line Rule, Block 5, Deferred Strengths, Domain Calibration (§4.6).

---

## [2.0.0] — 2026-04-19

Foundation: complete system prompt, Phase 0 intake, 4-level severity taxonomy, 8 behavioral rules, Blocks 0–6, Dual-Language Protocol, THE SOVEREIGN ADVERSARY identifier.

---

## [Pending — v2.6.0 Roadmap]

- [ ] `prompts/system_prompt_legal.md` — legal/compliance domain variant
- [ ] `prompts/system_prompt_trading.md` — trading strategy domain variant
- [ ] COMPARATIVE MODE worked example (example_04)
- [ ] OPTIMIZATION MODE worked example (example_05)
- [ ] UNIT-PSYCH extended bias catalog
