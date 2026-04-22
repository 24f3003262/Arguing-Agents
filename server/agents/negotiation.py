from agents.buyer import BuyerAgent
from agents.seller import SellerAgent
from schemas.negotiation import NegotiationRequest, NegotiationResponse, NegotiationResult


def run_negotiation(req: NegotiationRequest, max_rounds: int = 6) -> NegotiationResponse:
    buyer = BuyerAgent(personality=req.personality)
    seller = SellerAgent(personality=req.personality)

    seller_offer = min(max(req.start_price, req.min_price), req.max_price)
    buyer_offer = req.min_price

    history: list[NegotiationResult] = []

    for round_index in range(1, max_rounds + 1):
        buyer_offer = buyer.next_offer(req, seller_offer=seller_offer, round_index=round_index)
        seller_offer = seller.next_offer(req, buyer_offer=buyer_offer, round_index=round_index)

        history.append(
            NegotiationResult(
                round=round_index,
                buyer_offer=buyer_offer,
                seller_offer=seller_offer,
            )
        )

        if buyer_offer >= seller_offer:
            agreed_price = round((buyer_offer + seller_offer) / 2, 2)
            return NegotiationResponse(
                status="agreed",
                item=req.item,
                agreed_price=agreed_price,
                rounds=history,
            )

    return NegotiationResponse(
        status="no_agreement",
        item=req.item,
        agreed_price=None,
        rounds=history,
    )
