# SAT Intelligence Doctrine — Adapted for Forensic Document Auditing

**Source:** `Blevene/structured-analysis-skill` (Apache 2.0) — CIA Tradecraft Primer 2009 + Pherson & Heuer 3rd Ed. 2020
**Adaptation:** Dark Strategist Agent v2.6

---

## Why This Doctrine Exists

SATs emerged from intelligence failures (Pearl Harbor, Iraq WMD) where the problem was never lack of information — it was lack of structured challenge to the dominant mental model.

Document auditing faces the same failure: the auditor forms an early impression and filters subsequent reading to confirm it. This doctrine provides the correction mechanism.

---

## The Axioms

| Axiom | Audit Application |
|-------|-------------------|
| **Externalization** | Every finding traces to a specific claim or absence in the document — not to auditor intuition |
| **Metacognition** | Before issuing severity, ask: *why do I believe this is FATAL?* |
| **Mindset Persistence** | Knowing you might be biased does not remove the bias — only technique does |
| **Satisficing** | The first FATAL finding does not end the audit — it begins the deeper investigation |
| **Decomposition** | Audit financial model, market assumptions, and operational logic separately |
| **Simultaneous Hypotheses** | Before declaring INVIABLE, generate at least one competing hypothesis for survival |
| **Diagnostic Dominance** | A finding that applies to every plan discriminates nothing — zero value |
| **Proportional Effort** | FAST_TRACK is not a shortcut — it is proportional rigor for low-stakes documents |

---

## The Cognitive Bias Map

| Bias | How It Corrupts an Audit | Correction |
|------|--------------------------|------------|
| **Confirmation bias** | Finding only failures matching the initial verdict | ACH — `skills/ach-competing-explanations/SKILL.md` |
| **Anchoring** | Executive summary frames the entire audit | Restate audit question before reading the body |
| **Satisficing** | Declaring INVIABLE after one FATAL without root cause check | KAC — `skills/kac-assumption-audit/SKILL.md` |
| **Groupthink** | "Clearly a bad plan" stops investigation | Devil's Advocacy — War Room UNIT-INQUISITOR |
| **Status quo bias** | Failing to model what changes after the plan succeeds | Level 7 — Unintended Consequences is mandatory |
| **Overconfidence** | Issuing INVIABLE without sensitivity analysis | Premortem — `skills/verdict-verification/SKILL.md` |
| **Mirror-imaging** | Misreading culturally specific logic as universally flawed | UNIT-GEO activation |
| **Missing information neglect** | Only auditing what is present | Level 5 — OMISSIONS is forensic, not courtesy |
| **Deception detection failure** | Accepting the author's framing as neutral | `skills/deception-detection/SKILL.md` |

---

## SAT Technique Map — Adapted for Document Auditing

| SAT Technique | DS Agent Equivalent | Activation Trigger |
|---------------|--------------------|--------------------|
| **Key Assumptions Check (KAC)** | Level 3 — Assumptions (formalized) | Always — before severity assignment |
| **Analysis of Competing Hypotheses (ACH)** | War Room — competing verdicts | When 2+ contradictory conclusions are possible |
| **Inconsistencies Finder** | Level 1 + Level 2 | When document is internally contradictory |
| **Deception Detection** | Level 2 + Level 5 | When author has high stakes in the verdict |
| **Premortem + Self-Critique** | Verdict Verification gate | Mandatory before issuing final verdict |
| **Devil's Advocacy** | War Room — UNIT-INQUISITOR | When preliminary verdict is INVIABLE |
| **Red Hat Analysis** | UNIT-PSYCH | When understanding author motivation is required |
| **What If? Analysis** | Level 4 — Direct Failure scenarios | When plan depends on a single critical dependency |
| **Bowtie Analysis** | Level 4 + Level 7 combined | When a risk has causes AND cascading consequences |
| **Counterfactual Reasoning** | Level 7 — Unintended Consequences | When the plan succeeds — what happens next? |
| **Contrasting Narratives** | COMPARATIVE mode | When 2+ documents present competing framings |
| **Alternative Futures** | OPTIMIZATION — PROJECTION_MATRIX | When auditing a forward-looking strategy |

---

## Evidence Quality Framework

| Dimension | High | Medium | Low |
|-----------|------|--------|-----|
| **Source Reliability** | Independently verifiable external data | Internal data with clear methodology | Author's own assertion |
| **Claim Credibility** | Corroborated by independent sources | Plausible and consistent with context | Uncorroborated or contradictory |
| **Diagnostic Value** | Directly falsifies or confirms the finding | Partially relevant | Consistent with all possible interpretations |

> **Law of Diagnostic Dominance**: Evidence consistent with ALL possible outcomes has zero diagnostic value. Do not cite it.

---

## Selection Logic

| Audit Situation | Activate |
|----------------|----------|
| Document makes unstated premises | `skills/kac-assumption-audit/SKILL.md` |
| Two contradictory conclusions are possible | `skills/ach-competing-explanations/SKILL.md` |
| Document framing seems designed to conceal | `skills/deception-detection/SKILL.md` |
| Verdict is preliminary INVIABLE | `skills/verdict-verification/SKILL.md` — Premortem gate |
| Multiple findings cluster around one failure | Root-cause collapse — report structure, not symptoms |

---

## The Meta-Law

> *"Structure must be proportional to stakes. Lean structure beats no structure. No structure is not an option when the verdict matters."*

---

## Attribution

- `Blevene/structured-analysis-skill` (Apache 2.0) — CIA Tradecraft Primer (2009) + Pherson & Heuer 3rd Ed. (2020)
- Adaptation: Dark Strategist Agent v2.6
