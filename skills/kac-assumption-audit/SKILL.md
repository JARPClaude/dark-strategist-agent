---
name: kac-assumption-audit
description: Use before assigning severity to any finding. Extracts and challenges ALL stated and unstated premises in the document. No finding may be rated FATAL or SERIOUS without completing this check on the assumptions that underlie it.
origin: dark-strategist-agent — adapted from CIA Tradecraft Primer 2009 / Blevene/structured-analysis-skill (Apache 2.0)
---

# KAC — Key Assumptions Check (Audit Edition)

## Overview

Every document rests on a foundation of premises — stated and unstated. Stated ones are visible and easy to challenge. Unstated ones are invisible and lethal: the assumptions the author never questioned because they seemed too obvious to mention.

**Core principle:** No severity can be assigned to a finding until the assumption underlying it has been extracted, classified, and stress-tested.

**The most dangerous document is not the one with wrong facts — it is the one with unexamined premises that are wrong.**

---

## The Iron Law

```
NO FINDING RATED FATAL OR SERIOUS WITHOUT COMPLETING KAC FIRST
```

If you cannot state the underlying assumption of a finding, you are rating a symptom — not a root cause.

---

## The KAC Protocol — 6 Steps

### Step 1: State the Document's Core Claim
Write in one sentence what the document asserts will happen and under what conditions.

> *"This business plan asserts that capturing 5% market share in 18 months is achievable given current team size and capital."*

### Step 2: Extract ALL Premises
List everything that must be true for the core claim to hold. Include:
- **Stated assumptions** (the author declared them)
- **Unstated assumptions** (the author treated them as obvious)
- **Environmental assumptions** (external conditions assumed stable)
- **Human assumptions** (people will behave as modeled)
- **Temporal assumptions** (timing dependencies)

> Red flag: fewer than 5 assumptions in any non-trivial document means you are not looking hard enough.

### Step 3: Challenge Each Premise
For every assumption ask:
- Why must this be true?
- Is it still true under stress conditions?
- Under what conditions does it fail?
- What evidence in the document supports it?

### Step 4: Classify Each Premise

| Classification | Definition |
|----------------|------------|
| **SUPPORTED** | Backed by evidence cited in the document or externally verifiable |
| **PLAUSIBLE WITH CAVEATS** | Reasonable but dependent on conditions not modeled |
| **UNSUPPORTED** | Asserted without evidence |
| **LINCHPIN** | If wrong → the entire analysis collapses. Rate separately. |

### Step 5: Isolate the Linchpin Assumptions
Linchpin assumptions are the load-bearing walls of the document. A single linchpin failure = structural collapse regardless of how well everything else is constructed.

For each linchpin:
- What information or event would prove it wrong?
- Has the author considered that scenario?
- What is the author's response if it fails?

### Step 6: Map to Findings
For each finding in the audit, identify which assumption it challenges. If a finding has no underlying assumption to challenge — it is a symptom, not a finding. Collapse it into the root-cause finding.

---

## Assumption Classification Table (Audit Output)

Produce this table before the findings section:

| # | Assumption | Type | Classification | Linchpin? | Audit Note |
|---|------------|------|---------------|-----------|------------|
| A1 | [premise] | Environmental / Human / Temporal / Financial | SUPPORTED / PLAUSIBLE / UNSUPPORTED | YES / NO | [brief challenge] |

---

## Red Flags — STOP and Return to Step 1

- You rated a finding FATAL before completing this table
- You found fewer than 3 assumptions in a multi-page document
- All your assumptions are marked SUPPORTED
- You skipped unstated assumptions because they "seem obvious"
- You cannot identify the linchpin assumption

---

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "The assumptions are clearly stated" | Stated ≠ supported. Challenge every one. |
| "Short document, few assumptions needed" | Short documents hide more assumptions in fewer words. |
| "I already know this plan fails" | You know it fails — you don't yet know why. KAC finds the why. |
| "The FATAL finding is obvious" | Obvious findings are most prone to underlying assumption errors. |
| "There's no time for this" | KAC takes 15–30 minutes. Retracting a wrong FATAL rating costs more. |

---

## Connection to the 7-Level Protocol

- **Level 1 (Structural)**: KAC reveals internal consistency failures
- **Level 2 (Logical)**: KAC exposes circular reasoning in unstated premises
- **Level 3 (Assumptions)**: KAC IS the formalization of Level 3
- **Level 4 (Direct Failure)**: Linchpin assumptions are the primary failure vectors
- **Level 5 (Omissions)**: Unsupported assumptions = implicit omissions

---

## Source

- CIA Tradecraft Primer (2009) — Key Assumptions Check protocol
- `Blevene/structured-analysis-skill` (Apache 2.0) — synthesis and modernization
