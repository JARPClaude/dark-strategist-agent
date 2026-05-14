"""
Dark Strategist — Budget Controller
Controls token and API call limits per session.
Version: 2.8.0
"""


class BudgetController:
    """
    Controls the budget of API calls per AFO session.
    Prevents runaway costs in Tribunal Mode.
    """

    def __init__(self, config: dict):
        tribunal_cfg = config.get("tribunal", {})
        self.max_agents = tribunal_cfg.get("max_agents", 7)
        self.max_calls_total = tribunal_cfg.get("max_calls_total", 30)
        self.max_n2_per_n1 = tribunal_cfg.get("max_n2_per_n1", 3)
        self.alert_at_percent = tribunal_cfg.get("alert_at_percent", 80)

        self.calls_made = {"single": 0, "n1": 0, "n2": 0, "synthesis": 0}
        self.agents_deployed = 0

    def can_proceed(self, call_type: str) -> bool:
        """Returns True if budget allows another call of the given type."""
        total = sum(self.calls_made.values())
        if total >= self.max_calls_total:
            print(f"[BUDGET_CONTROLLER] Max calls reached ({self.max_calls_total}). Blocking {call_type}.")
            return False
        if call_type == "n1" and self.agents_deployed >= self.max_agents:
            print(f"[BUDGET_CONTROLLER] Max agents reached ({self.max_agents}). Blocking N1.")
            return False
        if total >= int(self.max_calls_total * self.alert_at_percent / 100):
            print(f"[BUDGET_CONTROLLER] ⚠️  Budget at {self.alert_at_percent}% — {total}/{self.max_calls_total} calls used.")
        return True

    def record_call(self, call_type: str):
        """Records a completed API call."""
        self.calls_made[call_type] = self.calls_made.get(call_type, 0) + 1
        if call_type == "n1":
            self.agents_deployed += 1

    def remaining_agents(self) -> int:
        """Returns how many N1 agents can still be deployed."""
        return max(0, self.max_agents - self.agents_deployed)

    def summary(self) -> dict:
        """Returns budget consumption summary."""
        total = sum(self.calls_made.values())
        return {
            "calls_made": self.calls_made,
            "total_calls": total,
            "max_calls": self.max_calls_total,
            "agents_deployed": self.agents_deployed,
            "budget_used_percent": round(total / self.max_calls_total * 100, 1)
        }

    def print_summary(self):
        s = self.summary()
        print(f"\n[BUDGET SUMMARY]")
        print(f"  Total calls: {s['total_calls']}/{s['max_calls']} ({s['budget_used_percent']}%)")
        print(f"  Breakdown:   {s['calls_made']}")
        print(f"  Agents N1:   {s['agents_deployed']}")
