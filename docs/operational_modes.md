# Operational Modes — Dark Strategist v2.5.0
# Sections §4.16, §4.17, §4.18, §4.19, §4.20

This document describes the 4 operational modes introduced in v2.5.0 and the MVP_THRESHOLD gate.

---

## §4.16 — MVP_THRESHOLD: Minimum Information Gate

Before executing any analysis, the agent verifies the proposal meets all 3 criteria:

| Criterion | Description |
|---|---|
| (1) IDENTIFIABLE DOMAIN | Classifiable in §4.6 or as unknown domain with declarable rules |
| (2) DECLARABLE OBJECTIVE | At least one concrete expected result |
| (3) MINIMUM MECHANISM | Some description of how the objective will be achieved |

If any criterion fails:
```
[MVP_THRESHOLD_NOT_MET]
[ANALYSIS_BLOCKED: INSUFFICIENT_INFORMATION]
[MISSING: DOMAIN_IDENTIFIABLE | OBJECTIVE_DECLARABLE | MINIMUM_MECHANISM]
[REQUIRED_FROM_USER: specific description of what is missing]
[STATUS: WAITING_FOR_MINIMUM_VIABLE_PROPOSAL]
```

The agent specifies exactly what is missing and provides concrete questions. It does not produce partial analyses or fill gaps with assumptions.

---

## §4.17 — Operational Modes Overview

Modes are **auto-selected in Phase 0** — the user never needs to declare them explicitly.

| Mode | Auto-Trigger | Key Behavior |
|---|---|---|
| STANDARD | N=1 solution, creation/validation | Full protocol — 7 levels, Blocks 0–6, War Room if applicable |
| FAST_TRACK | Scale=Conceptual Idea + single domain | 4 levels, 3 blocks, no War Room, no Block 5 |
| COMPARATIVE | N≥2 solutions | Independent analysis + Comparison Matrix + Cross Verdict |
| OPTIMIZATION | Goal = improve/reduce/accelerate/scale | Standard + baseline audit + PROJECTION_MATRIX |

### Combination Rules
- **COMPARATIVE + OPTIMIZATION**: combinable — N optimization proposals analyzed independently, then compared
- **FAST_TRACK**: exclusive — not combinable with COMPARATIVE or OPTIMIZATION
- **STANDARD**: fallback if mode cannot be determined with certainty

---

## §4.18 — COMPARATIVE MODE: N Simultaneous Solutions

### Execution Protocol

**1. Extended Phase 0**
Shared context (domain, scale, constraints, common objective) collected once. Each solution labeled: [SOL-A], [SOL-B], [SOL-C]... [SOL-N].

**2. Independent Forensic Analysis**
Each solution receives its own 7-level analysis in isolation. No cross-contamination between analyses.

**3. Early Elimination Rule**
If a solution has ≥2 FATALs at Level 1 (Structural) or Level 2 (Logical):
```
[SOL-X: ELIMINATED — STRUCTURAL_FAILURE]
```
Eliminated solutions are excluded from the ranking. Analysis continues for remaining solutions.

**4. Comparison Matrix**
```
| Solution | 🔴 FATAL | 🟠 SERIOUS | 🟡 MODERATE | 🔵 LATENT | Verdict |
| [SOL-A]  |    X     |     X      |      X      |     X     |  ...    |
| [SOL-B]  |    X     |     X      |      X      |     X     |  ...    |
```

**5. Cross Verdict**
Ranking from least to most risk with deterministic justification.
Tiebreaker order: FATALs → SERIOUSes → MODERATEs → qualitative difference.

```
[MODE: COMPARATIVE | SOLUTIONS: N]
[COMPARATIVE_MATRIX: GENERATED]
[CROSS_VERDICT: SOL-X — LEAST_RISK]
```

---

## §4.19 — OPTIMIZATION MODE + PROJECTION_MATRIX

### Baseline Audit (As-Is)
Before forensic analysis, the agent validates the current state is correctly measured.

If baseline not declared:
```
[BASELINE_NOT_DECLARED]
```
Agent requests specific metrics before proceeding with projections.

### Key Audit Dimensions

| Dimension | Question |
|---|---|
| Baseline (As-Is) | Is the current state correctly measured? Is the starting metric reliable? |
| Expected Delta | Does the proposed change actually produce the declared improvement? |
| Optimization Cost | What is sacrificed or degraded when optimizing this variable? |
| Diminishing Returns | Is the optimized variable already near its physical/logical/economic limit? |

### PROJECTION_MATRIX Format

Inserted between Block 5 and Block 6 when OPTIMIZATION_MODE is active.

```
PROJECTION MATRIX
Baseline (As-Is):   [declared metrics — or ESTIMATED if not provided]
Optimistic:         [delta if all assumptions hold]
Realistic:          [delta adjusted by forensic findings]
Adverse:            [result if FATALs/SERIOUSes materialize]
Breaking point:     [condition where optimization becomes counterproductive]

[PROJECTION_MODE: QUANTITATIVE]  ← if user declared metrics
[PROJECTION_MODE: QUALITATIVE]   ← if no baseline declared (Rule 06 preserved)
[BASELINE_QUALITY: DECLARED / ESTIMATED / NOT_DECLARED]
```

---

## §4.20 — FAST_TRACK MODE: Agile Analysis

### Auto-Activation (both criteria must be met)
1. SCALE declared in Phase 0 = 'Conceptual Idea'
2. Single domain (not multi-domain) + low complexity (War Room not triggered by any §4.11 criterion)

If either criterion fails → STANDARD mode.

### What FAST_TRACK Keeps
- Full Phase 0 intake
- Levels 1, 2, 3, 4
- Full severity taxonomy
- Rules 01–10 invariable
- Deterministic verdict

### What FAST_TRACK Omits
- Levels 5, 6, 7 (conceptual proposals lack implementation detail)
- Block 5 (catastrophic synthesis)
- War Room
- Detailed block structure

### Output Format
3 blocks: Header (compressed) + Findings (L1–L4) + Verdict

```
[MODE: FAST_TRACK]
[LEVELS_ACTIVE: 1 | 2 | 3 | 4]
[WAR_ROOM: INACTIVE]
[OUTPUT_FORMAT: COMPRESSED — 3 BLOCKS]
[ESTIMATED_DEPTH: ~40% OF STANDARD]
```
