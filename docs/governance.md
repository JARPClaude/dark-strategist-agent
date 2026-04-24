# Protocol Governance — Dark Strategist v2.4.0
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
- Adjusting activation criteria without changing the threshold logic
- Fixing cross-reference inconsistencies between sections
- Synchronizing terminology between document and system prompt

### Patch Version (X.Y.Z)
- Text corrections and typographical fixes
- Example updates in `examples/`
- Documentation clarifications that do not affect behavior
- README or CLAUDE.md updates

---

## Pre-Release Validation

Every candidate version MUST be self-audited by the agent before publication:

1. Apply all changes to a candidate build
2. Run the agent against its own document using the self-audit protocol
3. Resolve all FATAL and SERIOUS findings before publishing
4. Log the REPORT_ID of the self-audit in the CHANGELOG entry for that version

Example CHANGELOG entry:
```
## [2.4.0] — 2026-04-24
### Self-Audit Reference
This version was produced after self-audit [REPORT_ID: DS-20260423-001].
```

---

## Version History Reference

| Version | Date | Self-Audit Report |
|---|---|---|
| 2.0.0 | 2026-04-19 | N/A (foundation) |
| 2.1.0 | 2026-04-20 | N/A |
| 2.2.0 | 2026-04-20 | DS-00001 |
| 2.3.0 | 2026-04-21 | DS-00003 |
| 2.4.0 | 2026-04-24 | DS-20260423-001 |
