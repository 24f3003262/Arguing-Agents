from pydantic import BaseModel, Field


class NegotiationRequest(BaseModel):
    item: str = Field(..., min_length=1)
    start_price: float = Field(..., gt=0)
    min_price: float = Field(..., gt=0)
    max_price: float = Field(..., gt=0)
    personality: str = Field(default="balanced")


class NegotiationResult(BaseModel):
    round: int
    buyer_offer: float
    seller_offer: float


class NegotiationResponse(BaseModel):
    status: str
    item: str
    agreed_price: float | None = None
    rounds: list[NegotiationResult] = Field(default_factory=list)
