from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.negotiation import run_negotiation
from schemas.negotiation import NegotiationRequest, NegotiationResponse

app = FastAPI(title="Agent Negotiation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # to be tightened before production
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Main negotiation endpoint ──────────────────────────────────────────────── #


@app.post("/negotiate", response_model=NegotiationResponse)
async def negotiate(req: NegotiationRequest) -> NegotiationResponse:
    return await run_negotiation(req)


# ── Quick sample-run endpoint (no body needed) ─────────────────────────────── #


@app.get("/sample-run", response_model=NegotiationResponse)
async def sample_run() -> NegotiationResponse:
    """
    Fires a pre-baked negotiation so you can test the whole pipeline
    without needing a frontend or Postman.

    Hit: GET http://localhost:8000/sample-run
    """
    sample = NegotiationRequest(
        item="Logo Design",
        starting_price=0.015,  # seller opens at 0.015 ETH
        buyer_max_price=0.010,  # buyer won't pay more than 0.010 ETH
        seller_min_price=0.008,  # seller won't go below 0.008 ETH
        buyer_personality="conservative",
        seller_personality="balanced",
    )
    return await run_negotiation(sample)


# ── Health check ───────────────────────────────────────────────────────────── #


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


# A simple list to act as  database for now
market_items = [
    {
        "id": 1, 
        "item": "Bored Ape #4211", 
        "starting_price": 0.5, 
        "seller_min_price": 0.4, # Add this for the AI
        "seller_wallet": "0x...",
        "status": "available"
    },
]
@app.post("/items")
async def create_item(item: dict):
    # Assign a basic ID and save
    item["id"] = len(market_items) + 1
    item["status"] = "available"
    market_items.append(item)
    return {"status": "success", "item": item}

@app.get("/items")
async def get_items():
    return market_items



@app.get("/items/{item_id}")
async def get_item(item_id: int):
    # Search the list for the item with the matching ID
    item = next((i for i in market_items if i["id"] == item_id), None)
    if item:
        return item
    return {"error": "Item not found"}, 404