"""
Dark Strategist — SSM Module
Simulación Social Masiva — Phase 3
Version: 2.9.0
"""

from .persona_factory import PersonaFactory
from .interaction_engine import InteractionEngine
from .social_report import SocialReport
from .budget_ssm import SSMBudgetController


class SimulacionSocialMasiva:
    """
    Main SSM entry point.
    Called by the AFO when verdict qualifies for social simulation.

    Activation logic:
      VIABLE WITH CRITICAL CORRECTIONS → auto-activate
      VIABLE WITH ADJUSTMENTS          → auto-activate
      SOLID UNDER PRESSURE             → optional (--ssm flag)
      INVIABLE                         → blocked
    """

    SSM_AUTO_VERDICTS = [
        "VIABLE WITH CRITICAL CORRECTIONS",
        "VIABLE WITH ADJUSTMENTS",
    ]

    SSM_OPTIONAL_VERDICTS = [
        "SOLID UNDER PRESSURE",
    ]

    SSM_BLOCKED_VERDICTS = [
        "INVIABLE",
        "DO NOT DEPLOY",
        "DO NOT EXECUTE",
    ]

    def __init__(self, config: dict):
        self.config = config
        self.budget = SSMBudgetController(config)
        self.factory = PersonaFactory()
        self.engine = InteractionEngine(config)
        self.reporter = SocialReport()

    def should_activate(self, tribunal_verdict: str, forced: bool = False) -> tuple:
        """
        Returns (should_run: bool, reason: str).
        forced=True means --ssm flag was passed explicitly.
        """
        verdict_upper = tribunal_verdict.upper()

        for blocked in self.SSM_BLOCKED_VERDICTS:
            if blocked in verdict_upper:
                return False, f"SSM blocked — Tribunal verdict is {blocked}"

        for auto in self.SSM_AUTO_VERDICTS:
            if auto in verdict_upper:
                return True, f"SSM auto-activated — verdict qualifies ({auto})"

        for optional in self.SSM_OPTIONAL_VERDICTS:
            if optional in verdict_upper:
                if forced:
                    return True, "SSM activated — SOLID UNDER PRESSURE + --ssm flag"
                return False, "SSM available but not forced — use --ssm flag to activate"

        # Unknown verdict — default to optional
        if forced:
            return True, "SSM activated by --ssm flag"
        return False, "SSM not activated — verdict not recognized as qualifying"

    def run(self, document: str, domain: str,
            tribunal_verdict: str, session_id: str,
            scale: str = "MESO") -> str:
        """
        Runs the full SSM pipeline and returns the REPORTE DE IMPACTO SOCIAL.

        scale: MICRO (5-10 personas), MESO (20), MACRO (50)
        """
        print(f"\n[SSM] Iniciando Simulación Social Masiva")
        print(f"[SSM] Domain: {domain} | Scale: {scale} | Session: {session_id}")

        # Generate personas
        personas = self.factory.generate(domain=domain, scale=scale)
        print(f"[SSM] {len(personas)} personas generated")
        self.budget.record_persona()

        # Run 4 interaction rounds
        personas = self.engine.run(document=document, personas=personas)

        # Generate social report
        report = self.reporter.generate(
            personas=personas,
            domain=domain,
            tribunal_verdict=tribunal_verdict,
            session_id=session_id
        )

        self.budget.print_summary()
        return report


__all__ = ["SimulacionSocialMasiva", "PersonaFactory",
           "InteractionEngine", "SocialReport", "SSMBudgetController"]
