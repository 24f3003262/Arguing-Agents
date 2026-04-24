"""
agents/base.py
--------------
A single Agent class that both buyer and seller are instances of.
Role, personality, and price limits are set at construction time.
"""

import json


PERSONALITY_HINTS = {
    "conservative": "You are cautious and price-sensitive. Move in small steps.",
    "aggressive":   "You want to close fast. Make bigger moves to reach a deal quickly.",
    "balanced":     "You negotiate fairly and aim for a reasonable middle ground.",
}


class Agent:
    def __init__(
        self,
        role: str,                    # "buyer" or "seller"
        personality: str = "balanced",
        min_price: float | None = None,
        max_price: float | None = None,
    ):
        self.role = role
        self.personality = personality
        self.min_price = min_price
        self.max_price = max_price

    # ------------------------------------------------------------------ #

    def build_prompt(self, context: str) -> str:
        if self.role == "buyer":
            goal = "Try to get the price as LOW as possible."
            limit = f"You will NEVER pay more than {self.max_price}."
        else:
            goal = "Try to get the price as HIGH as possible."
            limit = f"You will NEVER accept less than {self.min_price}."

        personality_hint = PERSONALITY_HINTS.get(
            self.personality, PERSONALITY_HINTS["balanced"]
        )

        return f"""You are a {self.role} negotiating a deal.

Personality: {personality_hint}

Rules:
- {goal}
- {limit}
- Respond ONLY with valid JSON, no extra text:
{{
  "message": "...",
  "offer_price": <number>,
  "status": "counter" | "accept" | "cancel"
}}

Negotiation so far:
{context}
"""

    async def respond(self, context: str, call_llm) -> dict:
        prompt = self.build_prompt(context)
        raw = await call_llm(prompt)
        return json.loads(raw)