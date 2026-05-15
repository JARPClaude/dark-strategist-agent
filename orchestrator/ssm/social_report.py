"""
Dark Strategist — SSM Social Report
Consolidates swarm behavior into the REPORTE DE IMPACTO SOCIAL.
Version: 2.9.0
"""

from datetime import datetime


class SocialReport:
    """
    Analyzes persona results from all 4 rounds and produces
    the REPORTE DE IMPACTO SOCIAL for the AFO.
    """

    def generate(self, personas: list, domain: str,
                 tribunal_verdict: str, session_id: str) -> str:
        """
        Generates the full REPORTE DE IMPACTO SOCIAL.
        """
        stats = self._compute_stats(personas)
        dominant = self._dominant_coalition(personas)
        hostile = self._most_hostile(personas)
        favorable = self._most_favorable(personas)
        adoption = self._estimate_adoption(personas)
        friction = self._main_friction(personas)
        scenarios = self._build_scenarios(personas, stats)

        report = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPORTE DE IMPACTO SOCIAL — SIMULACIÓN SOCIAL MASIVA
Session: {session_id} | Domain: {domain}
Tribunal Verdict: {tribunal_verdict}
Personas simulated: {len(personas)} | Rounds: 4
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STANCE DISTRIBUTION (after Round 2)
  FOR:     {stats['for_pct']}% ({stats['for_count']} personas)
  AGAINST: {stats['against_pct']}% ({stats['against_count']} personas)
  NEUTRAL: {stats['neutral_pct']}% ({stats['neutral_count']} personas)

COALITION FORMATION (Round 3)
  BLOCKING:     {stats['blocking_pct']}% ({stats['blocking_count']} personas)
  SUPPORT:      {stats['support_pct']}% ({stats['support_count']} personas)
  WAIT_AND_SEE: {stats['wait_pct']}% ({stats['wait_count']} personas)
  Dominant coalition: {dominant}

ADOPTION PROJECTION
  Estimated adoption: {adoption}% (vs. assumed in plan)
  Confidence: {'HIGH' if len(personas) >= 10 else 'MODERATE'}

MAIN FRICTION POINT
  {friction}

MOST HOSTILE PERSONA
  {hostile}

MOST FAVORABLE PERSONA
  {favorable}

ACTIONS TAKEN (Round 4)
{self._format_actions(personas)}

SCENARIO ANALYSIS
  Most likely:    {scenarios['likely']}
  Best case:      {scenarios['best']}
  Worst case:     {scenarios['worst']}

SOCIAL VIABILITY ASSESSMENT
  {self._social_verdict(stats, dominant)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        return report

    def _compute_stats(self, personas: list) -> dict:
        total = len(personas)
        if total == 0:
            return {k: 0 for k in ["for_count","against_count","neutral_count",
                                    "blocking_count","support_count","wait_count",
                                    "for_pct","against_pct","neutral_pct",
                                    "blocking_pct","support_pct","wait_pct"]}
        for_c = sum(1 for p in personas if p.get("stance") == "FOR")
        against_c = sum(1 for p in personas if p.get("stance") == "AGAINST")
        neutral_c = total - for_c - against_c
        blocking_c = sum(1 for p in personas if p.get("coalition") == "BLOCKING_COALITION")
        support_c = sum(1 for p in personas if p.get("coalition") == "SUPPORT_COALITION")
        wait_c = total - blocking_c - support_c

        return {
            "for_count": for_c, "against_count": against_c, "neutral_count": neutral_c,
            "blocking_count": blocking_c, "support_count": support_c, "wait_count": wait_c,
            "for_pct": round(for_c/total*100), "against_pct": round(against_c/total*100),
            "neutral_pct": round(neutral_c/total*100),
            "blocking_pct": round(blocking_c/total*100),
            "support_pct": round(support_c/total*100),
            "wait_pct": round(wait_c/total*100),
        }

    def _dominant_coalition(self, personas: list) -> str:
        blocking = sum(1 for p in personas if p.get("coalition") == "BLOCKING_COALITION")
        support = sum(1 for p in personas if p.get("coalition") == "SUPPORT_COALITION")
        wait = sum(1 for p in personas if p.get("coalition") == "WAIT_AND_SEE")
        if blocking > support and blocking > wait:
            return f"BLOCKING_COALITION ({blocking} personas) — HIGH RISK"
        if support > blocking and support > wait:
            return f"SUPPORT_COALITION ({support} personas) — FAVORABLE"
        return f"WAIT_AND_SEE ({wait} personas) — UNCERTAIN"

    def _most_hostile(self, personas: list) -> str:
        hostile = [p for p in personas if p.get("coalition") == "BLOCKING_COALITION"]
        if not hostile:
            return "No strongly hostile persona detected"
        h = max(hostile, key=lambda p: len(p.get("action", "")))
        return f"{h['role']} — Action: {h.get('action', 'N/A')[:150]}"

    def _most_favorable(self, personas: list) -> str:
        favorable = [p for p in personas if p.get("coalition") == "SUPPORT_COALITION"]
        if not favorable:
            return "No strongly favorable persona detected"
        f = max(favorable, key=lambda p: len(p.get("action", "")))
        return f"{f['role']} — Action: {f.get('action', 'N/A')[:150]}"

    def _estimate_adoption(self, personas: list) -> int:
        if not personas:
            return 0
        support = sum(1 for p in personas if p.get("coalition") == "SUPPORT_COALITION")
        wait = sum(1 for p in personas if p.get("coalition") == "WAIT_AND_SEE")
        # Support = full adoption, Wait = partial (50%), Blocking = 0
        effective = support + (wait * 0.3)
        return round(effective / len(personas) * 100)

    def _main_friction(self, personas: list) -> str:
        blockers = [p for p in personas if p.get("coalition") == "BLOCKING_COALITION"]
        if not blockers:
            return "No critical friction point detected"
        # Find the blocker with highest impact severity
        high = [p for p in blockers if p.get("impact_severity") == "HIGH"]
        target = high[0] if high else blockers[0]
        return f"{target['role']}: {target.get('impact', target.get('concern', 'Blocking action planned'))[:200]}"

    def _format_actions(self, personas: list) -> str:
        lines = []
        for p in personas:
            action = p.get("action", "No action")
            severity = p.get("impact_severity", "LOW")
            icon = "🔴" if severity == "HIGH" else "🟡" if severity == "MEDIUM" else "🔵"
            lines.append(f"  {icon} {p['role']}: {action[:120]}")
        return "\n".join(lines) if lines else "  No actions recorded"

    def _build_scenarios(self, personas: list, stats: dict) -> dict:
        blocking_pct = stats.get("blocking_pct", 0)
        support_pct = stats.get("support_pct", 0)

        if blocking_pct >= 50:
            likely = "Blocked or severely constrained by dominant opposition coalition"
            worst = "Complete blockage — regulatory action + negative press campaign"
            best = "Forced redesign accepted by 30% of blocking coalition"
        elif support_pct >= 50:
            likely = "Successful adoption with minor friction from blocking minority"
            worst = "Sustained opposition campaign slows adoption by 6-12 months"
            best = "Full adoption — blocking coalition neutralized by early wins"
        else:
            likely = "Uncertain adoption — outcome depends on early market signals"
            worst = "Blocking coalition gains momentum if early results disappoint"
            best = "Wait-and-see coalition converts to support after pilot success"

        return {"likely": likely, "best": best, "worst": worst}

    def _social_verdict(self, stats: dict, dominant: str) -> str:
        blocking_pct = stats.get("blocking_pct", 0)
        support_pct = stats.get("support_pct", 0)

        if blocking_pct >= 60:
            return "🔴 SOCIALLY INVIABLE — Dominant blocking coalition. External resistance will likely kill execution."
        if blocking_pct >= 40:
            return "🟠 HIGH SOCIAL RISK — Significant blocking coalition. Requires stakeholder strategy before launch."
        if support_pct >= 60:
            return "🟢 SOCIALLY VIABLE — Strong support coalition. External environment favorable for execution."
        return "🟡 SOCIALLY UNCERTAIN — Mixed signals. Monitor early adoption signals closely."
