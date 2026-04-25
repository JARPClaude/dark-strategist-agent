# Protocol Governance — Dark Strategist v2.5.1
# Section §4.14

This document defines the rules for modifying, versioning, and maintaining the Dark Strategist protocol.

---

## Change Authority

Only the registered repository author (JARPClaude) may approve modifications to the production system prompt in `prompts/system_prompt.md`.

Any derived adaptation must:
- Fork into an independent repository
- Maintain its own CHANGELOG
- Not use the name "THE SOVEREIGN ADVERSARY" without attribution

---

## Version Type Criteria

### Major Version (X.0.0)
Changes that alter the protocol architecture:
- Adding or removing output blocks (Blocks 0–6)
- Adding, removing, or fundamentally changing invariable rules (Rules 01–10)
- Redesigning the forensic process (7-level structure)
- Changing the verdict decision table logic
- Adding or removing session states

### Minor Version (X.Y.0)
Corrections to existing sections without architectural change:
- Adding domains to §4.6 or §4.13
- Expanding micro-agent descriptions or scope
- Adjusting activation criteria without changing threshold logic
- Fixing cross-reference inconsistencies between sections

### Patch Version (X.Y.Z)
- Text corrections and typographical fixes
- Example updates in `examples/`
- Documentation clarifications that do not affect behavior
- Taxonomy additions (§4.22 and similar reference documents)
- README or CLAUDE.md updates

---

## Pre-Release Validation

Every candidate version MUST be self-audited by the agent before publication:

1. Apply all changes to a candidate build
2. Run the agent against its own document using the self-audit protocol
3. Resolve all FATAL and SERIOUS findings before publishing
4. Log the REPORT_ID of the self-audit in the CHANGELOG entry for that version

---

## Version History Reference

| Version | Date | Type | Self-Audit Report |
|---|---|---|---|
| 2.0.0 | 2026-04-19 | Major | N/A (foundation) |
| 2.1.0 | 2026-04-20 | Minor | N/A |
| 2.2.0 | 2026-04-20 | Minor | DS-00001 |
| 2.3.0 | 2026-04-21 | Minor | DS-00003 |
| 2.4.0 | 2026-04-24 | Minor | DS-20260423-001 |
| 2.5.0 | 2026-04-25 | Major | N/A |
| 2.5.1 | 2026-04-25 | Patch | N/A |
