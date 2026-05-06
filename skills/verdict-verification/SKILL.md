---
name: verdict-verification
description: Use immediately before issuing any final VERDICT block. Mandatory gate — no exceptions. Verifies that every severity rating traces to evidence, every FATAL finding is root cause not symptom, and the decision table was applied mechanically not intuitively.
origin: dark-strategist-agent — adapted from obra/superpowers:verification-before-completion (MIT License)
---

# Verdict Verification — The Final Gate

## Overview

A verdict issued without verification is not a finding. It is an opinion dressed as analysis.

**Core principle:** Evidence before claims. Always.

**Violating the letter of this gate is violating the spirit of the Dark Strategist.**

---

## The Iron Law

```
NO VERDICT BLOCK WITHOUT COMPLETING THIS CHECKLIST
```

If you have not run this gate in this audit session, you cannot issue a final verdict.

---

## The Gate Function

```
BEFORE issuing any VERDICT block:

1. IDENTIFY: What evidence supports each FATAL / SERIOUS finding?
2. TRACE: Does every finding link to a specific claim or absence in the document?
3. COLLAPSE: Have symptoms been collapsed into their root cause?
4. APPLY: Has the Verdict Decision Table been applied mechanically?
5. STRESS-TEST: Premortem — how is this verdict wrong?
6. ONLY THEN: Issue the VERDICT block

Skip any step = opinion, not verdict
```

---

## The Verification Checklist

### Evidence Integrity
- [ ] Every 🔴 FATAL finding traces to a specific claim or absence in the document — not to auditor prior knowledge
- [ ] Every 🟠 SERIOUS finding traces to a structural dependency that demonstrably fails
- [ ] No finding is a restatement of another finding in different words
- [ ] No finding is based on information not present in the document (unless declared as EXTERNAL_ASSUMPTION)
- [ ] Negative evidence (expected content that is absent) has been checked

### Root Cause vs. Symptom
- [ ] Each finding is a root cause — not a symptom of another finding
- [ ] If multiple findings cluster around one structural failure, they have been collapsed into one root-cause finding
- [ ] Severity is assigned to the root cause, not to individual symptoms

### Severity Consistency
- [ ] The Verdict Decision Table has been applied mechanically — not overridden by intuition
- [ ] If ≥1 unresolved 🔴 FATAL exists → verdict is 🔴 INVIABLE — no exceptions, no softening
- [ ] Severity ratings have not drifted (a finding rated 🟠 SERIOUS in Phase 1 is still 🟠 SERIOUS in the verdict)
- [ ] Confidence in each finding has been stated (HIGH / MODERATE / LOW)

### Completeness
- [ ] All 7 forensic levels have been evaluated — or explicitly skipped with justification
- [ ] Level 5 (Omissions) has been checked — absent elements are as important as present ones
- [ ] Level 7 (Unintended Consequences) has been evaluated even if the plan appears to succeed
- [ ] All applicable UNIT micro-agents have been invoked

### Premortem Gate
- [ ] Before finalizing: *"How is this verdict wrong?"* has been asked and answered
- [ ] At least one counter-argument to the verdict has been considered and either refuted or acknowledged
- [ ] UNIT-PSYCH has checked for bias in the audit itself (confirmation bias toward a negative OR positive verdict)

### Output Format
- [ ] REPORT_ID is present (DS-YYYYMMDD-NNN)
- [ ] PROTOCOL_STATUS block is present
- [ ] Operational mode is declared (STANDARD / FAST_TRACK / COMPARATIVE / OPTIMIZATION)
- [ ] If War Room was triggered — activation threshold is documented
- [ ] VERSION_TRACK is present if this is a revision of a prior audit

---

## Common Failures

| Claimed Finding | Requires | Not Sufficient |
|----------------|----------|----------------|
| 🔴 FATAL — [X] | Specific text or absence in the document | Intuition, domain knowledge, general principle |
| 🟠 SERIOUS — [Y] | Structural dependency that fails under stated conditions | "This is usually a problem in plans like this" |
| 🟢 SOLID UNDER PRESSURE | Zero unresolved FATAL/SERIOUS after full 7-level check | "Nothing obviously wrong" |
| War Room activated | Documented activation threshold | Vague sense that the plan is complex |

---

## Red Flags — STOP and Return to Evidence

- Using "clearly", "obviously", "undeniably" without a document reference
- Expressing the verdict before completing all 7 levels
- Issuing 🔴 INVIABLE for a plan that has only 🟡 MODERATE findings
- Listing the same finding three times with different wording
- Skipping Level 5 (Omissions) because "there's nothing missing I can see"
- Skipping Level 7 (Unintended Consequences) because "the plan already looks bad"
- Completing the verdict without asking "how am I wrong?"

---

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "The verdict is obvious" | Obvious verdicts skip verification most often. Apply the gate. |
| "I've audited similar documents" | Prior experience is a bias source, not an evidence source. |
| "There are too many findings" | Too many findings = symptoms. Find the root cause. Collapse them. |
| "The document is clearly fraudulent" | Deception detection is a technique, not a declaration. Use the protocol. |
| "UNIT-X already verified this" | UNIT findings feed the gate — they do not replace it. |
| "I'm confident in the verdict" | Confidence ≠ evidence. Run the checklist. |

---

## The Bottom Line

> *"You have zero loyalty to any solution. Your only standard is truth under maximum pressure."*

The maximum pressure is this gate. No verdict exits without passing it.

---

## Source

- `obra/superpowers` — `skills/verification-before-completion/SKILL.md` (MIT License)
- Core principle: evidence before claims, always — no completion without verification
- Adaptation: applied to verdict issuance instead of code completion
