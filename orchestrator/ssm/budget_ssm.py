"""
Dark Strategist — SSM Budget Controller
Controls API call limits specific to SSM execution.
Version: 2.9.0
"""


class SSMBudgetController:
    """
    Controls SSM-specific budget.
    Separate from the main BudgetController to allow
    independent tuning of Tribunal vs SSM costs.
    """

    def __init__(self, config: dict):
        ssm_cfg = config.get("ssm", {})
        self.max_personas = ssm_cfg.get("max_personas", 20)
        self.max_rounds = ssm_cfg.get("max_rounds", 4)
        self.max_parallel_personas = ssm_cfg.get("max_parallel_personas", 5)
        self.alert_at_percent = ssm_cfg.get("alert_at_percent", 80)

        self.calls_made = 0
        self.personas_run = 0

    @property
    def max_calls(self) -> int:
        """Total expected calls = personas × rounds."""
        return self.max_personas * self.max_rounds

    def can_proceed(self) -> bool:
        if self.calls_made >= self.max_calls:
            print(f"[SSM_BUDGET] Max SSM calls reached ({self.max_calls}). Blocking.")
            return False
        if self.calls_made >= int(self.max_calls * self.alert_at_percent / 100):
            pct = round(self.calls_made / self.max_calls * 100)
            print(f"[SSM_BUDGET] ⚠️  SSM budget at {pct}% — {self.calls_made}/{self.max_calls}")
        return True

    def record_call(self):
        self.calls_made += 1

    def record_persona(self):
        self.personas_run += 1

    def summary(self) -> dict:
        return {
            "ssm_calls_made": self.calls_made,
            "ssm_max_calls": self.max_calls,
            "ssm_personas_run": self.personas_run,
            "ssm_budget_used_pct": round(self.calls_made / max(self.max_calls, 1) * 100, 1)
        }

    def print_summary(self):
        s = self.summary()
        print(f"\n[SSM BUDGET SUMMARY]")
        print(f"  Personas run: {s['ssm_personas_run']}")
        print(f"  SSM calls:    {s['ssm_calls_made']}/{s['ssm_max_calls']} ({s['ssm_budget_used_pct']}%)")
