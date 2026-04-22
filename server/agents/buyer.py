from schemas.negotiation import NegotiationRequest


class BuyerAgent:
    def __init__(self, personality: str = "balanced") -> None:
        self.personality = personality.lower().strip()

    def next_offer(self, req: NegotiationRequest, seller_offer: float, round_index: int) -> float:
        spread = max(req.max_price - req.min_price, 1.0)

        if self.personality == "aggressive":
            concession_rate = 0.12
        elif self.personality == "conservative":
            concession_rate = 0.04
        else:
            concession_rate = 0.08

        target = req.min_price + spread * concession_rate * round_index
        offer = min(target, seller_offer, req.max_price)
        return round(max(offer, req.min_price), 2)
