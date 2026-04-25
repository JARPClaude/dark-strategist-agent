# CHANGELOG — Dark Strategist Agent

All significant changes to the system prompt and agent structure are documented here.
Format: [VERSION] — DATE — Description

---

## [2.5.0] — 2026-04-25

### Major Version — 6 New Capabilities

This is a major version. It adds new operational modes and a new micro-agent that alter the protocol architecture.

1. **§4.16 MVP_THRESHOLD** — Minimum information gate before analysis proceeds. 3 criteria: identifiable domain, declarable objective, minimum mechanism. Emits `[MVP_THRESHOLD_NOT_MET]` if any criterion fails.
2. **§4.17 Operational Modes** — 4 modes auto-selected in Phase 0: STANDARD, FAST_TRACK, COMPARATIVE, OPTIMIZATION. Combination rules: COMPARATIVE + OPTIMIZATION combinable; FAST_TRACK exclusive.
3. **§4.18 COMPARATIVE_MODE** — N≥2 simultaneous solutions. Independent forensic analysis per solution, Early Elimination Rule (≥2 FATALs at L1/L2), Comparison Matrix, Cross Verdict with deterministic ranking. Tiebreaker: FATALs → SERIOUSes → MODERATEs.
4. **§4.19 OPTIMIZATION_MODE + PROJECTION_MATRIX** — As-Is vs. To-Be audit. Validates baseline before projecting. PROJECTION_MATRIX inserted between Block 5 and Block 6: optimistic / realistic / adverse scenarios + breaking point. Quantitative if baseline declared, qualitative if not (Rule 06 preserved).
5. **§4.20 FAST_TRACK MODE** — Auto-activated for Scale=Conceptual Idea + single domain. Levels 1-4 only, 3-block output, no War Room, no Block 5. ~40% of standard analysis time.
6. **§4.21 UNIT-PSYCH + Block 4 verifiable criteria** — New micro-agent: The Behavioral Bias Auditor. Targets: confirmation bias, groupthink, founder overconfidence, optimism bias, Dunning-Kruger, sunk cost fallacy. Active in Business/Commercial and Public Sector (Scale ≥ Detailed Proposal) and in COMPARATIVE MODE with evidence of confirmation bias. Block 4 now requires verifiable criterion: (A) empirical support, (B) survived analysis, or (C) structural constraint. If none met → Block 4 omitted.

---

## [2.4.0] — 2026-04-24

### Self-Audit Reference
This version was produced after self-audit [REPORT_ID: DS-20260423-001].
All 7 issues from v2.3 audit resolved. 0 issues carried over from v2.3.

### Corrections Applied (7 total — 1 fatal, 2 serious, 3 moderate, 1 latent)
1. **Classification updated** — "USO RESTRINGIDO — JARP" replaced with "OPEN SOURCE — MIT License".
2. **§4.6 Extractivo/Agro expanded** — Renamed to "EXTRACTIVO / AGRO / GANADERO". Added animal biosecurity, seasonal cycles, biological commodity dependency.
3. **Rule 01 corrected** — Deferred Strengths reference fixed to Bloque 4 (not Bloque 3).
4. **§4.6 Auditoría de Sistemas expanded** — Renamed to "AUDITORÍA DE SISTEMAS / CIBERSEGURIDAD".
5. **§4.14 Protocol Governance added** — Change authority, version type criteria, pre-release self-audit.
6. **Footer updated** — GitHub repo URL.
7. **§4.15 Deprecation Clause added** — 4 conditions (A-D) + DEPRECATION.md protocol.

---

## [2.3.0] — 2026-04-21

### Corrections Applied (7 total)
1. Executive Summary updated to v2.3.
2. ES/EN Terminology Map in §4.4.
3. War Room Activation Threshold in §4.11 — 4 deterministic criteria.
4. Geofence Field Expanded in Block 1 — 5 variables with severity indicators.
5. VERSION_TRACK Context Degradation — 3-step instruction.
6. UNIT-BIO Extended to Livestock.
7. REPORT_ID Convention Documented.

---

## [2.2.0] — 2026-04-20

### Corrections Applied (7 total)
1. Block Numbering Synchronized.
2. Deterministic Verdict Logic — Block 6 decision table.
3. Rule 10 Evidence Standard — 3 explicit criteria.
4. NEGLECT_DETECTED Unlock Criteria — 3 unlock paths + 3-attempt counter.
5. §4.13 Activation Matrix — 9 domain rows.
6. Block 5 Integrity Rule — no fabricated N% probability.
7. §4.6 Domain Expansion — Capital Markets, Systems Audit, Business/Commercial.

---

## [2.1.0] — 2026-04-20

### Added
- War Room Orchestration model (§4.11)
- Sectoral Agnosticism (§4.12)
- Standard Micro-Agent Catalog (§4.13) — 7 units
- Geofence Audit (§4.3.1)
- Sub-Protocol for Unknown Domains
- Epistemic Honesty Note (§4.3.2)
- Rule 09 — Transversal Escalation
- Rule 10 — Aseptic Inflexibility
- NEGLECT_DETECTED state
- Red Line Rule + Block 5
- Deferred Strengths block (Block 4)
- Domain Calibration (§4.6)

---

## [2.0.0] — 2026-04-19

### Foundation
- Complete system prompt with identity, mission, 7-level forensic process
- Phase 0 mandatory intake
- 4-level severity taxonomy
- 8 behavioral rules
- Standardized output format Blocks 0–6
- Correction Plan section (on explicit demand)
- Dual-Language Protocol
- THE SOVEREIGN ADVERSARY protocol identifier

---

## [Pending — v2.6.0 Roadmap]

- [ ] `prompts/system_prompt_legal.md` — legal/compliance domain variant
- [ ] `prompts/system_prompt_trading.md` — trading strategy domain variant
- [ ] COMPARATIVE MODE worked example (example_04)
- [ ] OPTIMIZATION MODE worked example (example_05)
- [ ] UNIT-PSYCH extended bias catalog
