---
name: adaptive-autonomous-drive
version: 3.2.0
description: Official skill formalizing the AFO autonomous operational layer. Six internal modules (GoalEngine, MotivationModel, StateMemory, AutonomousLoop, SafetyGuard, SelfEvaluation) that expand analysis autonomously when gaps are detected, without user instruction.
origin: dark-strategist-agent — native
---

# Adaptive Autonomous Drive
# Skill for Dark Strategist — Official Technical Specification
# Location: skills/adaptive-autonomous-drive/SKILL.md

---

## Purpose

The **Adaptive Autonomous Drive** skill grants Dark Strategist a layer of operational autonomy, enabling it to:

- Generate internal goals dynamically based on detected gaps
- Expand analysis beyond the initial prompt
- Activate sub-agents by its own criterion, without user instruction
- Reorder priorities according to evolving context
- Execute additional adversarial rounds when gaps, omissions, or underexplored risks are detected

This skill does not create consciousness. It creates **autonomous strategic behavior** — which is exactly what an adversarial forensic audit system requires to operate at maximum depth.

---

## Architecture — 6 Internal Modules

### 1. GoalEngine — Internal Goal Engine
Maintains, adjusts, and generates internal audit goals during execution.

Base goals:
- G1: Maximize detection of FATAL and SERIOUS risks
- G2: Expose fragile assumptions and critical omissions
- G3: Stress-test geofences and regulatory contexts
- G4: Identify Level 7 unintended consequences
- G5: Detect underexplored domains and force additional analysis

Key capability: Generate dynamic sub-goals at runtime, for example:
- "Re-examine governance in emerging markets"
- "Stress-test supply chain assumptions in LATAM"
- "Re-evaluate financial projections under adverse regime"

### 2. MotivationModel — Artificial Motivation Model
Determines where deeper analysis delivers the highest adversarial value.

Adversarial value criteria:
- Potential severity of the risk
- Uncertainty or absence of data
- Geographic and regulatory impact
- Structural fragility
- Systemic risk potential

### 3. StateMemory — State Memory
Registers analysis progress to avoid redundancy and detect coverage gaps.

Registers: domains audited, risks classified, sub-agents activated,
geofences stress-tested, assumptions challenged.

### 4. AutonomousLoop — Autonomous Decision Loop
Allows Dark Strategist to continue analyzing without user intervention.

Cycle:
1. Read active goals (GoalEngine)
2. Review state memory (StateMemory)
3. Evaluate where highest adversarial value remains pending
4. Activate sub-agents as needed
5. Execute new demolition round
6. Update memory and goals
7. Repeat until SafetyGuard limits reached

### 5. SafetyGuard — Security Guards
Prevents autonomy from becoming uncontrolled.

Hard rules:
- Do not modify severity taxonomies or Rule 09
- Do not fabricate specific data about real entities
- Do not exit the domain of the input document
- Do not soften critical risks
- Do not enter infinite loops — enforce maximum round limit
- Do not contradict the adversarial purpose of Dark Strategist

### 6. SelfEvaluation — Internal Self-Evaluation
Forces the agent to assess whether analysis is sufficient before closing.

Internal questions:
- Are there underexplored geofences?
- Are there omitted actors or stakeholders?
- Are there latent risks that should be escalated?
- Are there assumptions that have not been stress-tested?
- Are there domains without assigned sub-agents?

If gaps detected → generate new internal goals → execute another round.

---

## Integration with Dark Strategist

### With the AFO (Agente Forense Orquestador)

| Layer | Function |
|-------|----------|
| Reactive | Standard 7-level forensic analysis |
| Autonomous | Dynamic expansion via Adaptive Autonomous Drive |

### With N2 Sub-agents

| Sub-agent | Activation trigger |
|-----------|-------------------|
| UNIT-GEO | Geopolitical risk signals |
| UNIT-INQUISITOR | Legal or regulatory risk signals |
| UNIT-TECH | Technical architecture failure signals |
| UNIT-MARKET | Commercial model fragility signals |
| UNIT-BIO | Field or biological risk signals |
| UNIT-COMPLIANCE | Governance or control gap signals |
| UNIT-QUANT | Quantitative or statistical risk signals |
| UNIT-PSYCH | Cognitive bias or deception signals |

Activation is autonomous — not dependent on user instruction.

---

## Execution Flow

```
Document received
      ↓
Standard Tribunal Transversal analysis
      ↓
Adaptive Autonomous Drive reviews output
      ↓
Detects gaps, omissions, underexplored risks
      ↓
Generates additional internal goals
      ↓
Activates sub-agents as needed
      ↓
Executes additional adversarial rounds (max = SafetyGuard)
      ↓
Final report — deeper, more complete, higher coverage
```

---

## Limits

### Technical
- Does not modify base architecture
- Does not alter severity taxonomies or behavioral rules
- Does not execute code or interact with real systems
- Does not persist beyond active session without external infrastructure

### Conceptual
- No consciousness or real desires
- No agency outside user/orchestrator-initiated cycle
- Does not redefine adversarial purpose

### Practical
- More autonomous rounds → more tokens → higher cost
- Risk of over-analysis if unconstrained
- Requires explicit round and depth limits via BudgetController

---

## Pseudocode

```python
class AdaptiveAutonomousDrive:

    def __init__(self):
        self.goals = GoalEngine()
        self.memory = StateMemory()
        self.motivation = MotivationModel()
        self.safety = SafetyGuard()
        self.self_eval = SelfEvaluation()
        self.max_rounds = 3  # configurable via BudgetController

    def run(self, initial_analysis: str) -> str:
        self.memory.register(initial_analysis)
        for round_n in range(self.max_rounds):
            if not self.safety.can_proceed():
                break
            goals = self.goals.generate(self.memory)
            if not goals:
                break
            priority = self.motivation.prioritize(goals)
            sub_agents = self.activate_sub_agents(priority)
            new_findings = self.demolish(sub_agents)
            self.memory.register(new_findings)
            if self.self_eval.is_complete(self.memory):
                break
        return self.memory.export_report()
```

---

## System Prompt Integration Block

```
[SKILL: ADAPTIVE AUTONOMOUS DRIVE — ACTIVE]

The agent must:
- Generate dynamic internal goals based on detected gaps
- Activate sub-agents autonomously without waiting for user instruction
- Execute additional adversarial rounds when detecting:
  omissions, fragile assumptions, underexplored geofences,
  latent risks, domains without coverage
- Reorder priorities by severity and context
- Maintain internal memory of already-analyzed domains
- Respect limits: do not fabricate data, do not modify taxonomies,
  do not soften risks, do not enter infinite loops
- Stop when: all internal goals are met, no relevant gaps remain,
  or the maximum autonomous round limit is reached
```

---

```
[SKILL_STATUS: ACTIVE — v3.2.0]
[INTEGRATED_WITH: AFO | TribunalTransversal | SubAgentSpawner | GOAPPlanner]
[SAFETY: BudgetController hard limits enforced]
```
