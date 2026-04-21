# CHANGELOG — Dark Strategist Agent

All significant changes to the system prompt and agent structure are documented here.
Format: [VERSION] — DATE — Description

---

## [2.3.0] — 2026-04-21

### Corrections Applied (7 total)
1. **Executive Summary** — Updated to v2.3. Eliminated stale v2.1 reference from first content block.
2. **ES/EN Terminology Map in §4.4** — Explicit equivalence table: GRAVE↔SERIOUS, MODERADO↔MODERATE, LATENTE↔LATENT. Rule: no alternative translations permitted.
3. **War Room Activation Threshold in §4.11** — 4 deterministic criteria: (A) ≥2 declared domains, (B) matrix assigns ≥3 agents, (C) Scale=Production + specialized domain, (D) constraints contradict objective. No criterion = linear analysis.
4. **Geofence Field Expanded in Block 1** — From 1 line to 5 variables with severity indicators: Legal Security, Exchange Volatility, Infrastructure, Social Conflict, Audit Mode.
5. **VERSION_TRACK Context Degradation** — 3-step instruction when no previous context available: notify, request, degrade to first-version analysis with `[VERSION_TRACK: CONTEXT_UNAVAILABLE]`. Simulating comparison without data prohibited.
6. **UNIT-BIO Extended to Livestock** — Renamed "The Field & Livestock Auditor". Expanded scope: animal biosecurity, seasonal production cycles, capture quotas, biological commodity dependency. §4.13 matrix row updated.
7. **REPORT_ID Convention Documented** — Format `DS-AAAAMMDD-NNN` with real example. `[PREVIOUS_REPORT_ID]` field integrated in Block 0 for VERSION_TRACK cross-referencing.

---

## [2.2.0] — 2026-04-20

### Corrections Applied (7 total — 5 critical + 2 moderate)
1. **Block Numbering Synchronized** — Rule 04 corrected: references §4.9 instead of phantom "Block 5".
2. **Deterministic Verdict Logic** — Block 6 decision table with 4 cascading conditions. Rule 09-escalated FATALs count as FATALs.
3. **Rule 10 Evidence Standard** — 3 explicit criteria: (a) empirical data, (b) structural change, (c) unconsidered Phase 0 constraint. "This doesn't apply in our case" without evidence explicitly rejected.
4. **NEGLECT_DETECTED Unlock Criteria** — 3 unlock paths + 3-attempt counter before abandon recommendation.
5. **§4.13 Activation Matrix** — 9 domain rows with deterministic agent assignments. No intuition.
6. **Block 5 Integrity Rule** — Fabricated N% probability prohibited. Qualitative severity scale alternative provided.
7. **§4.6 Domain Expansion** — Added: Capital Markets, Systems Audit, Business/Commercial. Synchronized with Phase 0 domain list.

---

## [2.1.0] — 2026-04-20

### Added (integrated from Gemini sessions + original gaps)
- War Room Orchestration model (§4.11) — 3 phases: Instantiation, Isolated Interrogation, Orchestration
- Sectoral Agnosticism (§4.12) — explicit principle, applicability, limitation, geography
- Standard Micro-Agent Catalog (§4.13) — 7 units with missions and targets
- Geofence Audit (§4.3.1) — Geography as Severity Multiplier with 4 variables
- Sub-Protocol for Unknown Domains — Rules of the Game + Survival Metric
- Epistemic Honesty Note (§4.3.2) — protects Rule 06 against sectoral hallucination
- Rule 09 — Transversal Escalation (dynamic severity)
- Rule 10 — Aseptic Inflexibility (with Rule 06 conflict corrected)
- NEGLECT_DETECTED state (active blocking)
- Red Line Rule + Block 5 Catastrophic Risk Synthesis
- Deferred Strengths block (Block 4)
- Domain Calibration (§4.6) — 6 specialized frameworks

---

## [2.0.0] — 2026-04-19

### Foundation
- Complete system prompt with identity, mission, 7-level forensic process
- Phase 0 mandatory intake (domain, scale, constraints, objective, version)
- 4-level severity taxonomy: Fatal / Serious / Moderate / Latent
- 8 behavioral rules including anti-hallucination and version tracking
- Standardized output format: header + body per problem + verdict
- Correction Plan section (on explicit demand)
- Depth calibration based on proposal complexity
- Dual-Language Protocol: English for system layer, user language for output
- THE SOVEREIGN ADVERSARY protocol identifier
- Domain Specialist Calibration (§4.6)

### Base
- Original JARP prompt as starting point
- 7 gap improvements incorporated:
  1. Structured intake
  2. Depth calibration
  3. Version tracking
  4. Final verdict with viability sentence
  5. Specialized domain support
  6. Explicit severity taxonomy
  7. Anti-hallucination rule

---

## [Pending — v2.4.0 Roadmap]

- [ ] `prompts/system_prompt_legal.md` — legal/compliance domain variant
- [ ] `prompts/system_prompt_trading.md` — trading strategy domain variant
- [ ] `prompts/system_prompt_tech.md` — software architecture domain variant
- [ ] Comparative mode: analyze two solutions simultaneously, identify which fails less
- [ ] Integration with n8n-mcp for automated review workflows
- [ ] UNIT-PSYCH micro-agent: behavioral bias audit for strategy proposals
