"""
agents/negotiation.py
---------------------
Runs the negotiation loop between a buyer and seller agent.
History is kept as a list of turns and also fed back into context
as a readable string so agents remember what was said.
"""

from server.agents.base import Agent
from server.services.llm import call_llm
from server.schemas.negotiation import (
    AgentTurn,
    NegotiationRequest,
    NegotiationResponse,
    NegotiationRound,
)

MAX_ROUNDS = 5


def _build_context(item: str, starting_price: float, history: list[dict]) -> str:
    """
    Converts the running history into a readable string passed to each agent.
    Each agent sees the full conversation so far.
    """
    lines = [f"Item: {item}", f"Starting price: {starting_price}"]

    for turn in history:
        lines.append(
            f"{turn['role'].capitalize()}: \"{turn['message']}\" (offered {turn['offer_price']})"
        )

    return "\n".join(lines)


async def run_negotiation(req: NegotiationRequest) -> NegotiationResponse:
    buyer = Agent(
        role="buyer",
        personality=req.buyer_personality,
        max_price=req.buyer_max_price,
    )
    seller = Agent(
        role="seller",
        personality=req.seller_personality,
        min_price=req.seller_min_price,
    )

    history: list[dict] = []   # flat list of every turn: {role, message, offer_price, status}
    rounds: list[NegotiationRound] = []

    for round_number in range(1, MAX_ROUNDS + 1):
        context = _build_context(req.item, req.starting_price, history)

        # ── Buyer's turn ──────────────────────────────────────────────── #
        buyer_raw = await buyer.respond(context, call_llm)
        buyer_agent_turn = AgentTurn(**buyer_raw)
        history.append({"role": "buyer", **buyer_raw})

        if buyer_agent_turn.status in ("accept", "cancel"):
            rounds.append(NegotiationRound(
                round_number=round_number,
                buyer=buyer_agent_turn,
                seller=None,
            ))
            if buyer_agent_turn.status == "accept":
                return NegotiationResponse(
                    status="agreed",
                    item=req.item,
                    agreed_price=buyer_agent_turn.offer_price,
                    total_rounds=round_number,
                    rounds=rounds,
                    history=history,
                )
            break  # buyer cancelled

        # ── Seller's turn ─────────────────────────────────────────────── #
        context = _build_context(req.item, req.starting_price, history)

        seller_raw = await seller.respond(context, call_llm)
        seller_agent_turn = AgentTurn(**seller_raw)
        history.append({"role": "seller", **seller_raw})

        rounds.append(NegotiationRound(
            round_number=round_number,
            buyer=buyer_agent_turn,
            seller=seller_agent_turn,
        ))

        if seller_agent_turn.status == "accept":
            return NegotiationResponse(
                status="agreed",
                item=req.item,
                agreed_price=seller_agent_turn.offer_price,
                total_rounds=round_number,
                rounds=rounds,
                history=history,
            )

        if seller_agent_turn.status == "cancel":
            break

    # Ran out of rounds or someone cancelled
    return NegotiationResponse(
        status="cancelled",
        item=req.item,
        agreed_price=None,
        total_rounds=len(rounds),
        rounds=rounds,
        history=history,
    )