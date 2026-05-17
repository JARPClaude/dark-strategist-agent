"""
Dark Strategist v3.1.0 — GOAP A* Planner
Goal-Oriented Action Planning for the Agente Forense Orquestador (AFO).

Replaces the fixed Swarm Activation Score with dynamic A* planning:
  - Takes a GOAL STATE (e.g., "produce reliable verdict for this document")
  - Evaluates CURRENT STATE (domain, complexity, regime, budget)
  - Uses A* search to find the OPTIMAL ACTION SEQUENCE
  - Returns an EXECUTION PLAN (which agents, in what order, with what config)

Why GOAP over fixed rules:
  - Fixed: "IF INVIABLE → 5 agents" (rigid, doesn't consider budget or domain)
  - GOAP:  "Given budget=15 calls, domain=Legal, regime=adversarial →
            ROL:3 + FORENSE:3 + UNIT-INQUISITOR:1 + SSM:MESO" (adaptive)
"""

import heapq
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


# ─── STATE ────────────────────────────────────────────────────────────────────

@dataclass
class WorldState:
    """
    Represents the current state of the audit world.
    GOAP plans transitions from current state → goal state.
    """
    # Document properties
    domain: str = "General"
    subscenario: str = ""
    regime: str = "standard"
    document_complexity: str = "MEDIUM"  # LOW | MEDIUM | HIGH | CRITICAL

    # Budget
    budget_remaining: int = 30
    calls_used: int = 0

    # Analysis state
    initial_audit_done: bool = False
    preliminary_verdict: str = ""  # INVIABLE | VIABLE_CRITICAL | VIABLE_ADJUST | SOLID
    rol_layer_done: bool = False
    forense_layer_done: bool = False
    synthesis_done: bool = False
    ssm_done: bool = False

    # Agent counts deployed
    rol_agents_deployed: int = 0
    forense_agents_deployed: int = 0
    n2_agents_deployed: int = 0

    # Quality flags
    conflicts_detected: bool = False
    unknown_domain: bool = False
    high_stakes: bool = False  # True when regime=adversarial or domain=Legal/Financial

    def __hash__(self):
        return hash((
            self.domain, self.regime, self.preliminary_verdict,
            self.initial_audit_done, self.rol_layer_done,
            self.forense_layer_done, self.synthesis_done, self.ssm_done,
            self.rol_agents_deployed, self.forense_agents_deployed
        ))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    @property
    def is_goal(self) -> bool:
        return self.synthesis_done


@dataclass
class GoalState:
    """Defines what a successful audit looks like."""
    synthesis_done: bool = True
    min_verdict_confidence: str = "MODERATE"  # LOW | MODERATE | HIGH
    ssm_required: bool = False  # Only if verdict is VIABLE


# ─── ACTIONS ──────────────────────────────────────────────────────────────────

@dataclass
class Action:
    """A single action the AFO can take during planning."""
    name: str
    cost: int                        # Token/call cost
    preconditions: dict              # State fields that must be True
    effects: dict                    # State fields that change after action
    description: str = ""

    def is_applicable(self, state: WorldState) -> bool:
        """Check if this action can be applied to the current state."""
        for key, value in self.preconditions.items():
            if getattr(state, key, None) != value:
                return False
        if state.budget_remaining < self.cost:
            return False
        return True

    def apply(self, state: WorldState) -> WorldState:
        """Apply this action and return the new state."""
        import copy
        new_state = copy.copy(state)
        for key, value in self.effects.items():
            if key.endswith("_delta"):
                field = key[:-6]
                current = getattr(new_state, field, 0)
                setattr(new_state, field, current + value)
            else:
                setattr(new_state, key, value)
        new_state.budget_remaining -= self.cost
        new_state.calls_used += self.cost
        return new_state


# ─── ACTION LIBRARY ───────────────────────────────────────────────────────────

def build_action_library(ctx) -> list:
    """
    Builds the action library based on the current RuntimeContext.
    Actions are calibrated to domain, regime, and budget.
    """
    domain = getattr(ctx, "domain", "General")
    regime = getattr(ctx, "regime", "standard")
    budget = getattr(ctx, "tribunal_size", 5) * 5  # Approximate budget

    # High-stakes domains get extra weight
    high_stakes_domains = {"Legal", "Financial", "Trading", "Medical", "Cybersecurity"}
    is_high_stakes = domain in high_stakes_domains or regime == "adversarial"

    actions = [

        # ── Initial audit ──────────────────────────────────────────────────
        Action(
            name="INITIAL_AUDIT",
            cost=1,
            preconditions={"initial_audit_done": False},
            effects={
                "initial_audit_done": True,
                "preliminary_verdict": "UNKNOWN"  # Set by actual audit
            },
            description="Run single initial audit to get preliminary verdict and Swarm Score"
        ),

        # ── Rol layer options ──────────────────────────────────────────────
        Action(
            name="ROL_LAYER_MINIMAL",
            cost=2,
            preconditions={"initial_audit_done": True, "rol_layer_done": False},
            effects={"rol_layer_done": True, "rol_agents_deployed": 2},
            description="Deploy 2 Rol agents — minimum for simple documents"
        ),
        Action(
            name="ROL_LAYER_STANDARD",
            cost=3,
            preconditions={"initial_audit_done": True, "rol_layer_done": False},
            effects={"rol_layer_done": True, "rol_agents_deployed": 3},
            description="Deploy 3 Rol agents — standard coverage"
        ),
        Action(
            name="ROL_LAYER_FULL",
            cost=5,
            preconditions={"initial_audit_done": True, "rol_layer_done": False},
            effects={"rol_layer_done": True, "rol_agents_deployed": 5},
            description="Deploy 5 Rol agents — full domain simulation"
        ),

        # ── Forense layer options ──────────────────────────────────────────
        Action(
            name="FORENSE_LAYER_MINIMAL",
            cost=2,
            preconditions={"rol_layer_done": True, "forense_layer_done": False},
            effects={"forense_layer_done": True, "forense_agents_deployed": 2},
            description="Deploy 2 Forense agents — minimum forensic coverage"
        ),
        Action(
            name="FORENSE_LAYER_STANDARD",
            cost=3,
            preconditions={"rol_layer_done": True, "forense_layer_done": False},
            effects={"forense_layer_done": True, "forense_agents_deployed": 3},
            description="Deploy 3 Forense agents — standard forensic audit"
        ),
        Action(
            name="FORENSE_LAYER_FULL",
            cost=5,
            preconditions={"rol_layer_done": True, "forense_layer_done": False},
            effects={"forense_layer_done": True, "forense_agents_deployed": 5},
            description="Deploy 5 Forense agents — full adversarial pressure"
        ),

        # ── N2 sub-agents ──────────────────────────────────────────────────
        Action(
            name="SPAWN_N2_TARGETED",
            cost=2,
            preconditions={"forense_layer_done": True},
            effects={"n2_agents_deployed_delta": 2},
            description="Spawn 2 targeted N2 sub-agents for specialized analysis"
        ),
        Action(
            name="SPAWN_N2_FULL",
            cost=4,
            preconditions={"forense_layer_done": True},
            effects={"n2_agents_deployed_delta": 4},
            description="Spawn 4 N2 sub-agents — full specialized coverage"
        ),

        # ── Synthesis ──────────────────────────────────────────────────────
        Action(
            name="SYNTHESIZE",
            cost=1,
            preconditions={"forense_layer_done": True, "synthesis_done": False},
            effects={"synthesis_done": True},
            description="AFO synthesizes all outputs → VEREDICTO FORENSE UNIFICADO"
        ),

        # ── SSM ────────────────────────────────────────────────────────────
        Action(
            name="SSM_MICRO",
            cost=5,
            preconditions={"synthesis_done": True, "ssm_done": False},
            effects={"ssm_done": True},
            description="Run SSM with MICRO scale (5-10 personas)"
        ),
        Action(
            name="SSM_MESO",
            cost=10,
            preconditions={"synthesis_done": True, "ssm_done": False},
            effects={"ssm_done": True},
            description="Run SSM with MESO scale (20 personas)"
        ),
        Action(
            name="SSM_MACRO",
            cost=20,
            preconditions={"synthesis_done": True, "ssm_done": False},
            effects={"ssm_done": True},
            description="Run SSM with MACRO scale (50 personas)"
        ),
    ]

    return actions


# ─── A* SEARCH ────────────────────────────────────────────────────────────────

@dataclass(order=True)
class PlanNode:
    """A node in the A* search tree."""
    f_score: float
    g_score: float = field(compare=False)
    state: WorldState = field(compare=False)
    actions: list = field(compare=False, default_factory=list)

    def __hash__(self):
        return hash(self.state)


def heuristic(state: WorldState, goal: GoalState, ctx) -> float:
    """
    A* heuristic: estimates remaining cost to reach goal state.
    Admissible (never overestimates) — guarantees optimal plan.
    """
    h = 0.0
    domain = getattr(ctx, "domain", "General")
    high_stakes = domain in {"Legal", "Financial", "Trading", "Medical", "Cybersecurity"}

    if not state.initial_audit_done:
        h += 1
    if not state.rol_layer_done:
        h += 3 if high_stakes else 2
    if not state.forense_layer_done:
        h += 3 if high_stakes else 2
    if not state.synthesis_done:
        h += 1
    if goal.ssm_required and not state.ssm_done:
        h += 5

    return h


def astar_plan(initial_state: WorldState, goal: GoalState,
               actions: list, ctx, max_iterations: int = 500) -> list:
    """
    A* search for optimal action sequence.
    Returns list of Action objects representing the optimal plan.
    """
    start_node = PlanNode(
        f_score=heuristic(initial_state, goal, ctx),
        g_score=0,
        state=initial_state,
        actions=[]
    )

    open_set = [start_node]
    visited = set()
    iterations = 0

    while open_set and iterations < max_iterations:
        iterations += 1
        current = heapq.heappop(open_set)

        if current.state in visited:
            continue
        visited.add(current.state)

        # Goal check
        if current.state.synthesis_done:
            if not goal.ssm_required or current.state.ssm_done:
                return current.actions

        # Expand actions
        for action in actions:
            if not action.is_applicable(current.state):
                continue

            new_state = action.apply(current.state)
            if new_state in visited:
                continue

            g = current.g_score + action.cost
            h = heuristic(new_state, goal, ctx)
            f = g + h

            new_node = PlanNode(
                f_score=f,
                g_score=g,
                state=new_state,
                actions=current.actions + [action]
            )
            heapq.heappush(open_set, new_node)

    # No plan found — return minimal fallback plan
    return _fallback_plan(actions)


def _fallback_plan(actions: list) -> list:
    """Returns a minimal safe plan when A* fails."""
    plan_names = ["INITIAL_AUDIT", "ROL_LAYER_STANDARD",
                  "FORENSE_LAYER_STANDARD", "SYNTHESIZE"]
    action_map = {a.name: a for a in actions}
    return [action_map[n] for n in plan_names if n in action_map]


# ─── GOAP PLANNER ─────────────────────────────────────────────────────────────

class GOAPPlanner:
    """
    Main GOAP planner for the AFO.
    Replaces fixed Swarm Activation Score with dynamic A* planning.
    """

    def __init__(self, config: dict):
        self.config = config
        self.budget = config.get("tribunal", {}).get("max_calls_total", 40)

    def plan(self, ctx, run_ssm: bool = False,
             preliminary_verdict: str = "") -> dict:
        """
        Plans the optimal execution strategy for a given RuntimeContext.

        Returns:
            {
                "plan": [Action, ...],
                "total_cost": int,
                "rol_agents": int,
                "forense_agents": int,
                "ssm_scale": str | None,
                "tribunal_label": str,
                "reasoning": str
            }
        """
        # Build initial world state
        initial_state = WorldState(
            domain=getattr(ctx, "domain", "General"),
            subscenario=getattr(ctx, "subscenario", ""),
            regime=getattr(ctx, "regime", "standard"),
            budget_remaining=self.budget,
            preliminary_verdict=preliminary_verdict,
            high_stakes=getattr(ctx, "domain", "") in {
                "Legal", "Financial", "Trading", "Medical", "Cybersecurity"
            } or getattr(ctx, "regime", "") == "adversarial"
        )

        # Define goal
        ssm_required = run_ssm and preliminary_verdict in [
            "VIABLE WITH CRITICAL CORRECTIONS",
            "VIABLE WITH ADJUSTMENTS",
            "SOLID UNDER PRESSURE"
        ]
        goal = GoalState(
            synthesis_done=True,
            ssm_required=ssm_required
        )

        # Build action library
        actions = build_action_library(ctx)

        # Run A* search
        plan = astar_plan(initial_state, goal, actions, ctx)

        # Extract plan metadata
        total_cost = sum(a.cost for a in plan)
        rol_agents = next(
            (a.effects.get("rol_agents_deployed", 0)
             for a in plan if "ROL_LAYER" in a.name), 0
        )
        forense_agents = next(
            (a.effects.get("forense_agents_deployed", 0)
             for a in plan if "FORENSE_LAYER" in a.name), 0
        )
        ssm_action = next((a for a in plan if "SSM_" in a.name), None)
        ssm_scale = ssm_action.name.split("_")[-1] if ssm_action else None

        # Determine tribunal label
        total_agents = rol_agents + forense_agents
        if total_agents <= 2:
            tribunal_label = "SINGLE"
        elif total_agents <= 4:
            tribunal_label = "TRIBUNAL_LIGHT"
        elif total_agents <= 8:
            tribunal_label = "TRIBUNAL_FULL"
        else:
            tribunal_label = "TRIBUNAL_MAX"

        reasoning = self._explain_plan(plan, ctx, initial_state)

        return {
            "plan": plan,
            "total_cost": total_cost,
            "rol_agents": rol_agents,
            "forense_agents": forense_agents,
            "ssm_scale": ssm_scale,
            "ssm_required": ssm_required,
            "tribunal_label": tribunal_label,
            "reasoning": reasoning
        }

    def _explain_plan(self, plan: list, ctx, state: WorldState) -> str:
        """Generates human-readable explanation of the GOAP plan."""
        domain = getattr(ctx, "domain", "General")
        regime = getattr(ctx, "regime", "standard")
        steps = [f"{i+1}. {a.name} (cost={a.cost})" for i, a in enumerate(plan)]
        total = sum(a.cost for a in plan)
        return (
            f"GOAP A* plan for {domain}/{regime} "
            f"({len(plan)} actions, {total}/{self.budget} budget):\n"
            + "\n".join(steps)
        )

    def print_plan(self, plan_result: dict):
        """Prints plan summary to console."""
        print(f"\n[GOAP PLANNER] Execution Plan")
        print(f"  Tribunal:     {plan_result['tribunal_label']}")
        print(f"  Rol agents:   {plan_result['rol_agents']}")
        print(f"  Forense:      {plan_result['forense_agents']}")
        print(f"  SSM:          {plan_result['ssm_scale'] or 'NOT ACTIVATED'}")
        print(f"  Budget used:  {plan_result['total_cost']}")
        print(f"  Actions:      {len(plan_result['plan'])}")
        print(f"  Reasoning:\n{plan_result['reasoning']}")
