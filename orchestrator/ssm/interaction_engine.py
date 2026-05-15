"""
Dark Strategist — SSM Interaction Engine
Orchestrates 4 rounds of persona interaction with the document.
Version: 2.9.0

Round 1: Each persona reads the plan → forms individual opinion
Round 2: Personas exchange opinions → some change stance
Round 3: Coalitions form (FOR / AGAINST / NEUTRAL)
Round 4: Dominant coalition acts (invest, block, abandon, attack)
"""

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import anthropic


ROUND_SYSTEM_PROMPTS = {
    1: """You are simulating a {role} evaluating a proposal.
Profile: {profile}
Bias: {bias}
Objective: {objective}
Key question: {question}

Read the proposal and form your initial opinion.
Be authentic to your role — don't be neutral if your role wouldn't be.
Respond in JSON only:
{{"stance": "FOR|AGAINST|NEUTRAL", "reasoning": "1-2 sentences", "concern": "main worry", "interest": "what appeals to you"}}""",

    2: """You are a {role} who initially felt {stance} about this proposal.
Your reasoning: {reasoning}

You have now heard these perspectives from others:
{other_opinions}

Does hearing these perspectives change your stance?
Respond in JSON only:
{{"stance": "FOR|AGAINST|NEUTRAL", "changed": true|false, "new_reasoning": "1-2 sentences", "influenced_by": "which perspective moved you most, if any"}}""",

    3: """You are a {role} with stance: {stance}
Your reasoning: {reasoning}

Based on your position, which coalition do you join?
- BLOCKING_COALITION: actively working to stop or kill this proposal
- SUPPORT_COALITION: actively backing and promoting this proposal
- WAIT_AND_SEE: monitoring but not committing either way

Respond in JSON only:
{{"coalition": "BLOCKING_COALITION|SUPPORT_COALITION|WAIT_AND_SEE", "action_intent": "what you plan to do", "timeline": "immediate|short_term|long_term"}}""",

    4: """You are a {role} in the {coalition}.
Your intended action: {action_intent}
Timeline: {timeline}

Execute your action. What do you actually do?
Be specific and realistic to your role.
Respond in JSON only:
{{"action": "specific action taken", "impact": "expected impact on the proposal", "severity": "HIGH|MEDIUM|LOW"}}"""
}


class InteractionEngine:
    """
    Orchestrates 4 rounds of persona-document interaction.
    Personas are blind to each other within each round,
    then share opinions between rounds.
    """

    def __init__(self, config: dict):
        self.config = config
        self.client = anthropic.Anthropic(api_key=config["anthropic"]["api_key"])
        self.max_workers = config.get("ssm", {}).get("max_parallel_personas", 5)

    def run(self, document: str, personas: list) -> list:
        """
        Runs all 4 rounds and returns enriched personas with results.
        """
        print(f"  [SSM] Starting {len(personas)} personas × 4 rounds")

        # Round 1: Individual reading
        personas = self._round_1(document, personas)
        print(f"  [SSM] Round 1 complete — stances: {self._stance_summary(personas)}")

        # Round 2: Exchange of opinions
        personas = self._round_2(document, personas)
        print(f"  [SSM] Round 2 complete — stances: {self._stance_summary(personas)}")

        # Round 3: Coalition formation
        personas = self._round_3(personas)
        print(f"  [SSM] Round 3 complete — coalitions: {self._coalition_summary(personas)}")

        # Round 4: Action
        personas = self._round_4(personas)
        print(f"  [SSM] Round 4 complete — actions recorded")

        return personas

    def _round_1(self, document: str, personas: list) -> list:
        """Each persona reads the plan and forms individual opinion."""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._call_persona, persona, 1,
                                document=document): persona["id"]
                for persona in personas
            }
            for future in as_completed(futures):
                pid = futures[future]
                persona = next(p for p in personas if p["id"] == pid)
                try:
                    result = future.result(timeout=60)
                    persona["round_1"] = result
                    persona["stance"] = result.get("stance", "NEUTRAL")
                    persona["reasoning"] = result.get("reasoning", "")
                except Exception as e:
                    persona["round_1"] = {"stance": "NEUTRAL", "reasoning": f"Error: {e}"}
                    persona["stance"] = "NEUTRAL"
                    persona["reasoning"] = ""
        return personas

    def _round_2(self, document: str, personas: list) -> list:
        """Personas exchange opinions and may change stance."""
        # Build opinion summary (blind — only stance + reasoning, not identity)
        other_opinions = "\n".join([
            f"- A {p['role']} feels {p['stance']}: {p.get('reasoning', '')}"
            for p in personas
        ])

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._call_persona, persona, 2,
                                other_opinions=other_opinions): persona["id"]
                for persona in personas
            }
            for future in as_completed(futures):
                pid = futures[future]
                persona = next(p for p in personas if p["id"] == pid)
                try:
                    result = future.result(timeout=60)
                    persona["round_2"] = result
                    persona["stance"] = result.get("stance", persona["stance"])
                    persona["reasoning"] = result.get("new_reasoning", persona["reasoning"])
                except Exception as e:
                    persona["round_2"] = {"changed": False}
        return personas

    def _round_3(self, personas: list) -> list:
        """Personas form coalitions based on their final stance."""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._call_persona, persona, 3): persona["id"]
                for persona in personas
            }
            for future in as_completed(futures):
                pid = futures[future]
                persona = next(p for p in personas if p["id"] == pid)
                try:
                    result = future.result(timeout=60)
                    persona["round_3"] = result
                    persona["coalition"] = result.get("coalition", "WAIT_AND_SEE")
                    persona["action_intent"] = result.get("action_intent", "")
                    persona["timeline"] = result.get("timeline", "long_term")
                except Exception as e:
                    persona["round_3"] = {"coalition": "WAIT_AND_SEE"}
                    persona["coalition"] = "WAIT_AND_SEE"
        return personas

    def _round_4(self, personas: list) -> list:
        """Dominant coalition executes actions."""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._call_persona, persona, 4): persona["id"]
                for persona in personas
            }
            for future in as_completed(futures):
                pid = futures[future]
                persona = next(p for p in personas if p["id"] == pid)
                try:
                    result = future.result(timeout=60)
                    persona["round_4"] = result
                    persona["action"] = result.get("action", "")
                    persona["impact"] = result.get("impact", "")
                    persona["impact_severity"] = result.get("severity", "LOW")
                except Exception as e:
                    persona["round_4"] = {"action": "No action taken"}
                    persona["action"] = "No action taken"
        return personas

    def _call_persona(self, persona: dict, round_num: int, **kwargs) -> dict:
        """Makes a single Claude API call for a persona in a given round."""
        system = ROUND_SYSTEM_PROMPTS[round_num].format(
            role=persona["role"],
            profile=persona["profile"],
            bias=persona["bias"],
            objective=persona["objective"],
            question=persona["question"],
            stance=persona.get("stance", "NEUTRAL"),
            reasoning=persona.get("reasoning", ""),
            coalition=persona.get("coalition", "WAIT_AND_SEE"),
            action_intent=persona.get("action_intent", ""),
            timeline=persona.get("timeline", "long_term"),
            **kwargs
        )

        doc_excerpt = kwargs.get("document", "")[:2000]
        user_content = f"Proposal:\n{doc_excerpt}" if round_num == 1 else "Proceed as instructed."

        response = self.client.messages.create(
            model=self.config["anthropic"]["model"],
            max_tokens=512,
            system=system,
            messages=[{"role": "user", "content": user_content}]
        )

        text = response.content[0].text.strip()
        # Strip markdown fences if present
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        try:
            return json.loads(text)
        except Exception:
            return {"raw": text, "stance": "NEUTRAL"}

    def _stance_summary(self, personas: list) -> str:
        counts = {"FOR": 0, "AGAINST": 0, "NEUTRAL": 0}
        for p in personas:
            counts[p.get("stance", "NEUTRAL")] = counts.get(p.get("stance", "NEUTRAL"), 0) + 1
        return f"FOR={counts['FOR']} AGAINST={counts['AGAINST']} NEUTRAL={counts['NEUTRAL']}"

    def _coalition_summary(self, personas: list) -> str:
        counts = {}
        for p in personas:
            c = p.get("coalition", "WAIT_AND_SEE")
            counts[c] = counts.get(c, 0) + 1
        return " | ".join([f"{k}={v}" for k, v in counts.items()])
