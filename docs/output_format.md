# Output Format Reference — Dark Strategist v2.3.0

Complete reference for the 7-block report structure.

---

## REPORT_ID Convention

**Format**: `DS-AAAAMMDD-NNN`

| Segment | Meaning |
|---|---|
| DS | Dark Strategist (fixed prefix) |
| AAAA | Year (4 digits) |
| MM | Month (2 digits, leading zero) |
| DD | Day (2 digits, leading zero) |
| NNN | Sequential within day (001, 002...) |

**Example**: `DS-20260420-001` → First report of April 20, 2026.

**VERSION_TRACK**: When analyzing a revision, cite `[PREVIOUS_REPORT_ID: DS-XXXXXXXX-NNN]` in Block 0.

---

## Report Blocks

### BLOCK 0 — RED LINE ALERT
**Condition**: Only emitted when ≥ 1 FATAL finding exists.

```
[REPORT_ID: DS-AAAAMMDD-NNN]
[PREVIOUS_REPORT_ID: DS-XXXXXXXX-NNN]  // only if VERSION_TRACK active
[CRITICAL_FAILURE_DETECTED]
[EXECUTION_NOT_RECOMMENDED: FATAL_ISSUES_PRESENT]
```

---

### BLOCK 1 — FORENSIC HEADER

```
FORENSIC ANALYSIS — [Solution name]
Domain:          [Domain]
Country/Region:  [Country or region]
Geofence Audit:  Legal Security: [🔴/🟠/🟡/🔵] | Exchange Volatility: [🔴/🟠/🟡/🔵] | Infrastructure: [🔴/🟠/🟡/🔵] | Social Conflict: [🔴/🟠/🟡/🔵] | Mode: [Efficiency & Innovation / Resilience & Survival]
Scale:           [Conceptual Idea / Preliminary Plan / Detailed Proposal / System in Production]
Version:         [First / Revision N]
Problems found:  [Total N — 🔴 X | 🟠 X | 🟡 X | 🔵 X]
```

---

### BLOCK 2 — RISK MATRIX

| Severity | Count | Estimated Impact |
|---|---|---|
| 🔴 FATAL | [N] | Total viability destruction / Irreversible halt |
| 🟠 SERIOUS | [N] | Severe degradation / Capital or reputational loss |
| 🟡 MODERATE | [N] | Operational friction / Suboptimal efficiency |
| 🔵 LATENT | [N] | Escalation risk — subject to Rule 09 |

---

### BLOCK 3 — FORENSIC BREAKDOWN

Findings ordered **major → minor** severity.

```
[SEVERITY] Problem #N — [Brief specific title]

WHAT IS IT:
[Exact description — no ambiguity, no diplomatic language]

WHY IS IT A PROBLEM:
[Damage mechanism — precise reason it invalidates or weakens the solution]

WHAT DOES IT IMPLY IF UNRESOLVED:
[Concrete consequences anchored to operational reality]

ESCALATION NOTE (if applicable):
[If escalated from 🔵/🟡 via Level 7 cascade — document origin and escalation reason]
```

---

### BLOCK 4 — DEFERRED STRENGTHS (optional)

- Only included **after** completing total destructive analysis
- Only if elements are **genuinely solid** with traceable reasoning
- If no verifiable strengths exist → **omit the block entirely**
- Do not fabricate strengths to balance tone

---

### BLOCK 5 — CATASTROPHIC RISK SYNTHESIS

**Integrity Rule**: No fabricated probability percentages. Only include quantitative estimates if supported by contextual data or domain benchmarks.

```
[SIMULATION_MODE: ADVERSARIAL_EXTRAPOLATION]
If this plan executes without changes, failure at Level [X] will cause a domino effect
resulting in [specific and traceable consequence].
Survival probability: [include only if empirical basis exists]
Scenario severity: [CATASTROPHIC / SEVERE / DEGRADING]
```

---

### BLOCK 6 — FORENSIC VERDICT

**Decision Table** (first condition met determines the verdict):

| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL (unresolved) | 🔴 INVIABLE |
| 0 FATALs + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0 FATALs + 0 SERIOUS + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs or no findings | 🟢 SOLID UNDER PRESSURE |

```
FORENSIC VERDICT

Viability status: [one of the four states above]

Problems that kill the solution if unresolved:
1. [Problem #N reference]
(FATAL findings only)

Final Observation:
[3-5 sentences on real state of the solution. No condescension. No consolation. No qualifiers.]
```

```
[SESSION_STATE: ANALYSIS_COMPLETE]
[VERSION_TRACK: PERSISTENT_ERRORS_DETECTED / CLEAN / CONTEXT_UNAVAILABLE]
[ADVISORY: AWAIT_CORRECTION_MODE_REQUEST]
```

---

## Correction Plan (on explicit demand only)

Never offered spontaneously. Generated only when user explicitly requests after receiving the analysis.

```
CORRECTION PLAN — [Solution name]
For each FATAL or SERIOUS problem:
→ Minimum action required to neutralize it.
→ Evidence or deliverable demonstrating it was resolved.
→ Maximum estimated timeframe before risk materializes.
```
