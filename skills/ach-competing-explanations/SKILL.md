---
name: ach-competing-explanations
description: Use when two or more contradictory conclusions are possible for the same document. Builds a hypothesis matrix and ranks explanations by least falsified — not most confirmed. Prevents confirmation bias from locking in a premature verdict.
origin: dark-strategist-agent — adapted from CIA Tradecraft Primer 2009 / Blevene/structured-analysis-skill (Apache 2.0)
---

# ACH — Analysis of Competing Explanations (Audit Edition)

## Overview

Confirmation bias is the auditor's primary failure mode. Once a preliminary verdict forms, subsequent reading filters evidence to confirm it. The result is a report that looks rigorous but is actually rationalization.

**ACH defeats confirmation bias by inverting the question:** instead of asking "what supports my verdict?", it asks "which verdict has the fewest pieces of evidence contradicting it?"

**The winner is not the hypothesis with the most support. It is the hypothesis that survives the most attacks.**

---

## The Iron Law

```
RANK EXPLANATIONS BY INCONSISTENCY COUNT — NOT CONFIRMATION COUNT
```

A verdict supported by 20 pieces of evidence but contradicted by 3 is weaker than a verdict supported by 5 and contradicted by 0.

---

## When to Activate

- Two contradictory verdicts are both plausible after initial reading
- Document evidence seems to support opposite conclusions depending on framing
- Preliminary INVIABLE verdict feels too easy — the plan is not obviously bad
- COMPARATIVE mode: 2+ solutions being evaluated simultaneously
- War Room units are producing conflicting findings

---

## The ACH Protocol — 8 Steps

### Step 1: Frame the Audit Question Neutrally
State the question without presupposing the answer.

> ❌ "Why does this plan fail?"
> ✅ "What is the most accurate assessment of this plan's viability?"

### Step 2: Generate ALL Competing Explanations
Minimum 3 hypotheses. Always include:
- **H-VIABLE**: The plan works as stated
- **H-INVIABLE**: The plan fails at a fundamental level
- **H-CONDITIONAL**: The plan works only under specific conditions not guaranteed
- **H-NULL**: Insufficient information to assess
- **H-DECEPTION**: The document is designed to mislead (activate when author has high stakes)

### Step 3: List ALL Evidence and Absences
Include:
- Positive evidence (what the document claims)
- Negative evidence (what is absent but should be present)
- Contradictory evidence (claims that conflict with each other)

> **Do not skip negative evidence.** A business plan that never mentions competition is not neutral — the absence IS evidence.

### Step 4: Build the Matrix

| Evidence Item | H-VIABLE | H-INVIABLE | H-CONDITIONAL | H-NULL | H-DECEPTION |
|--------------|----------|------------|--------------|--------|-------------|
| [Evidence 1] | C / I / N | C / I / N | C / I / N | C / I / N | C / I / N |

Rating key:
- **C** = Consistent (does not contradict this hypothesis)
- **I** = Inconsistent (directly contradicts this hypothesis)
- **N** = Neutral (irrelevant to this hypothesis)

### Step 5: Tally Inconsistencies Per Hypothesis
Count **I** ratings per column. Fewest **I** ratings = most defensible hypothesis.

> **Law of Diagnostic Dominance**: Evidence rated C or N for ALL hypotheses = zero value. Remove it from the matrix.

### Step 6: Sensitivity Analysis
Identify the 2–3 evidence items with highest diagnostic value. Flag them:
- What if this evidence is wrong?
- What if the author fabricated it?
- What if the context has changed since it was written?

### Step 7: State the Winner — With Caveats
Declare the hypothesis with fewest inconsistencies as preliminary verdict. State explicitly:
- What evidence would change the verdict
- What information is missing that would resolve uncertainty
- Confidence level (HIGH / MODERATE / LOW)

### Step 8: Map to Severity
- H-INVIABLE with LOW sensitivity → 🔴 FATAL
- H-INVIABLE with HIGH sensitivity → 🟠 SERIOUS
- H-CONDITIONAL → 🟠 SERIOUS or 🟡 MODERATE depending on condition likelihood
- H-NULL → activate §4.16 MVP_THRESHOLD / NEGLECT_DETECTED

---

## ACH Output Template

```
COMPETING EXPLANATIONS ANALYSIS

Audit Question: [neutral statement]

Hypotheses:
  H1: VIABLE — [specific claim]
  H2: INVIABLE — [specific failure mode]
  H3: CONDITIONAL — [condition required]
  H4: NULL — [information gap]

Matrix: [table]

Inconsistency Count: H1=X, H2=X, H3=X, H4=X

Least-inconsistent hypothesis: [H?]
Diagnostic sensitivity: [HIGH/MODERATE/LOW]

Preliminary verdict: [INVIABLE / VIABLE WITH CONDITIONS / INSUFFICIENT DATA]
Confidence: [HIGH / MODERATE / LOW]

What would change this verdict: [specific evidence or condition]
```

---

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "There's only one possible explanation" | You haven't generated alternatives. Minimum 3 hypotheses. |
| "The evidence clearly points to INVIABLE" | Tally the inconsistencies. Clarity is a bias signal, not a finding. |
| "H-DECEPTION is paranoid" | Documents with high author stakes have structural incentive to mislead. Include it. |
| "Negative evidence isn't evidence" | Absence of expected content IS evidence. Include absences in the matrix. |
| "This takes too long" | ACH on a 3-hypothesis matrix: 20–40 minutes. Retracting a wrong verdict costs more. |

---

## Source

- CIA Tradecraft Primer (2009) — Analysis of Competing Hypotheses
- Richards J. Heuer Jr. — *Psychology of Intelligence Analysis* (1999)
- `Blevene/structured-analysis-skill` (Apache 2.0) — modernization and empirical updates
