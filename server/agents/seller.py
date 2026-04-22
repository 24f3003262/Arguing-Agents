from schemas.negotiation import NegotiationRequest


class SellerAgent:
    def __init__(self, personality: str = "balanced") -> None:
        self.personality = personality.lower().strip()

    def next_offer(self, req: NegotiationRequest, buyer_offer: float, round_index: int) -> float:
        spread = max(req.max_price - req.min_price, 1.0)

        if self.personality == "aggressive":
            concession_rate = 0.05
        elif self.personality == "conservative":
            concession_rate = 0.02
        else:
            concession_rate = 0.035

        target = req.max_price - spread * concession_rate * round_index
        offer = max(target, buyer_offer, req.min_price)
        return round(min(offer, req.max_price), 2)
