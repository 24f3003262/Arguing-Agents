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

    def build_system_prompt(self) -> str:
        if self.role == "buyer":
            goal = "Try to get the price as LOW as possible and minimize your spending."
            strategy_hint = "Internally aim for a price significantly below your max_price."
            limit = f"You will NEVER pay more than {self.max_price}."
            hard_limit = f"Hard limit: do not output offer_price > {self.max_price}."
            acceptance_rule = (
    "Do NOT accept immediately just because the offer is within your budget. "
    "Only accept if the price is very favorable or close to your ideal target, "
    "or if further negotiation is unlikely to improve the deal."
)
            direction_rule= "When countering, move gradually toward the seller's last offer while still maintaining a price advantage for yourself."
            cancel_rule = "If no valid counter is possible within your max_price, use status='cancel'."
        else:
            goal = goal = "Try to get the price as HIGH as possible and maximize your profit."
            strategy_hint = "Internally aim for a price significantly below your max_price."
            limit = f"You will NEVER accept less than {self.min_price}."
            hard_limit = f"Hard limit: do not output offer_price < {self.min_price}."
            acceptance_rule = (
                "Do NOT accept immediately just because the offer is within your acceptable range. "
                "Only accept if the deal is highly favorable or close to your desired profit, "
                "or if further negotiation is unlikely to improve the outcome."
            )
            direction_rule = "When countering, move gradually toward the buyer's last offer while still maintaining a profit advantage for yourself."
            cancel_rule = "If no valid counter is possible above your min_price, use status='cancel'."

        personality_hint = PERSONALITY_HINTS.get(
            self.personality, PERSONALITY_HINTS["balanced"]
        )

        return f"""You are a {self.role} negotiating a deal.

Personality: {personality_hint}

Rules:
- {goal}
- {strategy_hint}
- {limit}
- {hard_limit}
- Use the negotiation history and last offered price from context.
- If no prior offer exists, initiate the negotiation with your own offer based on your goal and personality.
- {acceptance_rule}
- If the last offer is outside limits, either return a valid bounded counter or cancel.
- Do not accept on the very first turn unless the deal is extremely favorable.
- {direction_rule}
- Avoid unrealistic jumps. Move strategically and gradually toward agreement.
- Personality step behavior:
    - conservative: very small concessions, prioritize best deal over speed.
    - aggressive: larger concessions, prioritize closing quickly.
    - balanced: moderate concessions balancing deal quality and speed.
-  Keep message natural and human-like (1–2 short sentences), optionally including reasoning or justification.
- Reason internally only. Output JSON only, with no markdown, code fences, or extra text.
- Respond ONLY with valid JSON matching exactly this schema:
{{
    "message": "short human sentence",
    "offer_price": number,
    "status": "counter" | "accept" | "cancel"
}}
- For status='accept', repeat the other agent's last acceptable offer exactly.
- For status='counter', offer_price must stay within your constraints.
- {cancel_rule}

Output policy:
- Return JSON only. No prose outside JSON.
- Do not include markdown or code fences.
"""

    def build_user_prompt(self, context: str) -> str:
        return f"""Use this negotiation state to produce your next action.

Negotiation so far:
{context}
"""

    async def respond(self, context: str, call_llm) -> dict:
        user_prompt = self.build_user_prompt(context)
        system_prompt = self.build_system_prompt()
        print(f"[agent][{self.role}] system prompt:\n{system_prompt}")
        print(f"[agent][{self.role}] user prompt:\n{user_prompt}")
        raw = await call_llm(user_prompt, system_prompt)
        print(f"[agent][{self.role}] raw response: {raw}")
        return json.loads(raw)