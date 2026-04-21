# Severity Taxonomy — Dark Strategist v2.3.0

Reference document for the 4-level severity classification system.

---

## Overview

Severity is **not static**. It is recalibrated based on cascade potential via Rule 09.
The verdict decision table uses severity counts deterministically — no intuition involved.

---

## Levels

### 🔴 FATAL (ES: FATAL | EN: FATAL)
- **Meaning**: Invalidates the complete solution. If unresolved, execution fails with certainty.
- **Verdict impact**: Mandatory in final verdict. Presence → INVIABLE.
- **Escalation**: Can be reached from LATENT or MODERATE via Rule 09.
- **Correction**: Must be addressed before any execution attempt.

### 🟠 GRAVE (ES: GRAVE | EN: SERIOUS)
- **Meaning**: Significantly compromises success. High probability of partial failure, capital loss, or severe degradation.
- **Verdict impact**: 0 FATALs + ≥1 SERIOUS → VIABLE WITH CRITICAL CORRECTIONS.
- **Correction**: Must be corrected before any execution.

### 🟡 MODERADO (ES: MODERADO | EN: MODERATE)
- **Meaning**: Reduces effectiveness or introduces relevant friction. Does not kill the solution.
- **Verdict impact**: 0 FATALs + 0 SERIOUS + ≥1 MODERATE → VIABLE WITH ADJUSTMENTS.
- **Correction**: Must be addressed in refinement phase.
- **Escalation**: Subject to Rule 09 if Level 7 consequence is catastrophic.

### 🔵 LATENTE (ES: LATENTE | EN: LATENT)
- **Meaning**: Second or third-order risk. Not critical today, may escalate under specific conditions.
- **Verdict impact**: Only LATENTs → SOLID UNDER PRESSURE.
- **Monitoring**: Requires active monitoring, not immediate action.
- **Escalation**: Automatic to FATAL if triggers systemic collapse at Level 7.

---

## Rule 09 — Transversal Escalation

```
Mechanism:
  Origin Evaluation
      ↓
  Level 7 Projection
      ↓
  Severity Recalibration

Escalation paths:
  🔵 LATENT  → systemic collapse at L7  → 🔴 FATAL
  🟡 MODERATE → irreversible loss at L7  → 🟠 SERIOUS
```

Escalated findings are counted as their new severity in the verdict decision table.

---

## ES/EN Equivalence Map

| ES | EN | Notes |
|---|---|---|
| 🔴 FATAL | FATAL | Identical — no translation needed |
| 🟠 GRAVE | SERIOUS | Director uses SERIOUS; report says GRAVE |
| 🟡 MODERADO | MODERATE | Director uses MODERATE; report says MODERADO |
| 🔵 LATENTE | LATENT | Director uses LATENT; report says LATENTE |

**Prohibited alternatives**: SERIO, SEVERO, CRITICO (for SERIOUS), or any other translation.

---

## Verdict Decision Table

| Condition | Verdict |
|---|---|
| ≥ 1 🔴 FATAL (unresolved) | 🔴 INVIABLE |
| 0 FATALs + ≥ 1 🟠 SERIOUS | 🟠 VIABLE WITH CRITICAL CORRECTIONS |
| 0 FATALs + 0 SERIOUS + ≥ 1 🟡 MODERATE | 🟡 VIABLE WITH ADJUSTMENTS |
| Only 🔵 LATENTs or no findings | 🟢 SOLID UNDER PRESSURE |

Apply in descending order. First condition met determines the state.
Rule 09-escalated FATALs count as FATALs for this calculation.
