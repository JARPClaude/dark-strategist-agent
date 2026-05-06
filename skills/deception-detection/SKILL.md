---
name: deception-detection
description: Use when the document's author has high personal, financial, or reputational stakes in the outcome. Applies structured deception analysis to distinguish honest gaps from deliberate concealment. Activates automatically with UNIT-INQUISITOR and UNIT-PSYCH when mirror-imaging risk is detected.
origin: dark-strategist-agent — adapted from CIA Tradecraft Primer 2009 / Blevene/structured-analysis-skill (Apache 2.0)
---

# Deception Detection — Audit Edition

## Overview

Not every weak document is accidentally weak. When an author has significant stakes in the reader's conclusion, the document may be structured to guide the auditor toward a specific verdict — regardless of the underlying reality.

**Deception detection does not assume fraud.** It applies structured analysis to determine whether weakness is random (incompetence, time pressure, scope limit) or structured (selective presentation, strategic omission, framing manipulation).

**The difference matters:** a randomly weak plan may be fixable. A deceptively structured one requires a fundamentally different response.

---

## The Iron Law

```
AUTHOR STAKE IN THE OUTCOME IS A DIAGNOSTIC SIGNAL — NOT A VERDICT
```

High author stake activates this protocol. It does not predetermine the finding.

---

## Activation Triggers

Activate when:
- Document is a proposal, pitch, or business case where the author benefits directly from approval
- Document presents a solution to a problem the author was responsible for creating
- Document is a self-evaluation or self-audit
- Prior versions exist and key unfavorable data has disappeared between versions
- Document framing shifts focus from verifiable claims toward emotion or authority
- ACH matrix produces H-DECEPTION as a live hypothesis

---

## The Deception Detection Protocol — 5 Checks

### Check 1: Mirror-Imaging
Mirror-imaging assumes the author reasons the same way the auditor does. Break this.

Ask: *What would this document look like if the author were optimizing for persuasion rather than accuracy?*

- Would the structure be different?
- Would the evidence selection be different?
- Would the assumptions be the same?

If the answer to any is "no" — flag for deeper analysis.

### Check 2: Selective Evidence
Map ALL evidence in the document. Then ask:
- What evidence would a reasonable opponent cite against this plan?
- Is any of that evidence present?
- If not: is its absence explained, or simply absent?

> **Unexplained absence of expected counter-evidence is a deception signal.**

### Check 3: Framing Analysis
Identify the document's framing devices:

- **Anchoring**: Does the document establish a favorable baseline before presenting data?
- **False dichotomy**: Does it present a binary choice where other options exist?
- **Authority substitution**: Does it cite credentials or testimonials where evidence should be?
- **Scope manipulation**: Does it define the problem narrowly to exclude unfavorable comparisons?
- **Temporal cherry-picking**: Does it select a favorable time window for data presentation?

Each device found does not prove deception. It shifts the burden of evidence onto the document.

### Check 4: Internal Consistency Under Adversarial Reading
Read the document as an adversary — not seeking to understand, but seeking to disprove.

- Do the numbers in Section 2 match the assumptions stated in Section 1?
- Do the implementation timelines in Section 4 match the resource commitments in Section 3?
- Does the conclusion follow from the analysis, or does it exceed what the evidence supports?

Inconsistencies under adversarial reading = structural weakness at minimum, deception at maximum.

### Check 5: Counterfactual Integrity
Ask: *If the plan were actually not viable, what would this document look like?*

If the answer is "exactly like this" — the document has zero discriminatory power. It would look the same whether the plan works or not.

A document with no counterfactual discriminatory power cannot be the primary basis for a verdict. Additional external evidence is required.

---

## Deception Severity Classification

| Finding | Classification | Audit Impact |
|---------|---------------|--------------|
| Evidence gaps that favor the author's conclusion | STRUCTURAL WEAKNESS | 🟠 SERIOUS — Level 5 Omissions |
| Framing devices substituting for evidence | PERSUASION STRUCTURE | 🟠 SERIOUS — document is advocacy, not analysis |
| Internal inconsistencies under adversarial reading | LOGICAL FAILURE | 🔴 FATAL if load-bearing |
| Counterfactual-free presentation | NULL DISCRIMINATORY VALUE | NEGLECT_DETECTED — insufficient basis for verdict |
| Systematic pattern across multiple checks | HIGH DECEPTION PROBABILITY | 🔴 FATAL + UNIT-INQUISITOR escalation |

---

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "I'm not here to accuse the author of fraud" | Deception detection is structural analysis — not accusation. Apply the protocol. |
| "The gaps might just be incompetence" | That is one of the hypotheses. The protocol distinguishes them. |
| "The document looks professional" | Professional presentation is a framing device, not evidence of accuracy. |
| "Assuming deception is unfair" | Detecting structural possibility is methodology. Concluding it requires evidence. |
| "The author has a good reputation" | Reputation is authority substitution. Not evidence about this document. |

---

## Connection to the 7-Level Protocol

- **Level 2 (Logical)**: Framing analysis and internal inconsistencies surface here
- **Level 3 (Assumptions)**: Mirror-imaging and counterfactual integrity are assumption-level checks
- **Level 5 (Omissions)**: Selective evidence and unexplained absences are the primary Level 5 signals
- **War Room**: High deception probability activates UNIT-INQUISITOR + UNIT-PSYCH simultaneously

---

## Source

- CIA Tradecraft Primer (2009) — Deception Detection technique
- `Blevene/structured-analysis-skill` (Apache 2.0) — Contrasting Narratives + ACH integration
