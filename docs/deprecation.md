# Deprecation Clause — Dark Strategist v2.4.0
# Section §4.15

**Current Status:** `ACTIVE — v2.4.0`  
**Last Self-Audit:** DS-20260423-001  
**Replacement Protocol:** NONE — current version is latest  

---

## Deprecation Conditions

This protocol must be considered obsolete and replaced when **at least one** of the following conditions is met:

### (A) Superior Version Published
A later major version (e.g., v3.0.0) has been published in the official repository with a CHANGELOG documenting the migration path.

**Consequence:** Production instances of earlier versions must migrate within **90 days** of the publication date.

### (B) Model Capability Change
The underlying language model loses or alters reasoning capabilities that the protocol assumes as available, including:
- Insufficient context window to sustain War Room multi-agent orchestration
- Inability to maintain session states across a conversation
- Loss of structured output generation required for Blocks 0–6
- Degradation of multi-step reasoning required for 7-level forensic analysis

**Consequence:** The protocol must be adapted or replaced before continued deployment.

### (C) Uncovered Critical Domain
A recurrent high-impact domain emerges that the protocol cannot audit with the frameworks in §4.6 and §4.13 without systematically producing incomplete or inaccurate findings.

**Threshold:** The domain must appear in ≥ 3 distinct use cases where the protocol produces demonstrably incomplete analysis before this condition is triggered.

### (D) Self-Audit Failure
The agent, upon auditing its own specification document, produces a 🔴 FATAL finding that cannot be resolved without structural redesign of the protocol — i.e., the finding requires changes that would constitute a major version bump (X.0.0).

**Consequence:** Work on v(X+1).0.0 begins immediately. Current version remains active but is flagged as `PENDING_MAJOR_REVISION`.

---

## Deprecation Protocol

When a condition is triggered, the following actions must be taken:

1. **README.md** — Add a deprecation notice at the top with:
   - Effective date
   - Condition triggered (A, B, C, or D)
   - Recommended replacement version

2. **DEPRECATION.md** (this file) — Update status to:
   ```
   [PROTOCOL_STATUS: DEPRECATED]
   [DEPRECATION_DATE: YYYY-MM-DD]
   [CONDITION_TRIGGERED: A | B | C | D]
   [REPLACEMENT_PROTOCOL: v X.Y.Z]
   [MIGRATION_GUIDE: <URL or file reference>]
   ```

3. **CHANGELOG.md** — Add a final entry documenting the deprecation reason.

---

## Current Status Block

```
[PROTOCOL_STATUS: ACTIVE — v2.4.0]
[SELF_AUDIT_REPORT: DS-20260423-001]
[DEPRECATION_CONDITIONS: A | B | C | D]
[REPLACEMENT_PROTOCOL: NONE — current version is latest]
[MIGRATION_GUIDE: N/A]
[NEXT_REVIEW: Upon publication of v2.5.0 candidate or triggered condition]
```
