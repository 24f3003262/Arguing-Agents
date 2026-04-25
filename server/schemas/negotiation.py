from pydantic import BaseModel, Field
from typing import Literal

#  What the LLM returns for each agent turn (internal / parsed from LLM)      #

class AgentTurn(BaseModel):
    """One agent's response during a negotiation round."""
    message: str                                      # natural-language line shown in chat
    offer_price: float                                # the price the agent is proposing
    status: Literal["counter", "accept", "cancel"]   # what the agent decided


#  One full round (both sides spoke)                                           #

class NegotiationRound(BaseModel):
    """A single back-and-forth exchange between buyer and seller."""
    round_number: int
    buyer: AgentTurn
    seller: AgentTurn | None = None


#  API request / response shapes                                               #

class NegotiationRequest(BaseModel):
    item: str = Field(..., min_length=1, examples=["Logo Design"])
    starting_price: float = Field(..., gt=0, description="Seller's opening ask")
    buyer_max_price: float = Field(..., gt=0, description="Max the buyer will pay")
    seller_min_price: float = Field(..., gt=0, description="Floor the seller will accept")
    buyer_personality: Literal["conservative", "aggressive", "balanced"] = "balanced"
    seller_personality: Literal["conservative", "aggressive", "balanced"] = "balanced"


class NegotiationResponse(BaseModel):
    status: Literal["agreed", "cancelled"]
    item: str
    agreed_price: float | None = None          # set only when status == "agreed"
    total_rounds: int
    rounds: list[NegotiationRound] = Field(default_factory=list)
    history: list[dict] = Field(
        default_factory=list,
        description="Flat ordered list of every agent turn — good for chat UI rendering",
    )