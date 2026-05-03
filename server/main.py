from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.negotiation import run_negotiation
from schemas.negotiation import NegotiationRequest, NegotiationResponse

import json
import os
from fastapi import  HTTPException
app = FastAPI(title="Agent Negotiation API")

DB_FILE = "market_items.json"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # to be tightened before production
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_db():
    if not os.path.exists(DB_FILE):
        # Initial data if file doesn't exist
        initial_data = [
            {
                "id": 1, 
                "item": "Bored Ape #4211", 
                "starting_price": 0.5, 
                "seller_min_price": 0.4, 
                "seller_personality": "aggressive",
                "seller_wallet": "0x2AfA...85DB",
                "status": "available"
            }
        ]
        save_db(initial_data)
        return initial_data
    
    with open(DB_FILE, "r") as f:
        return json.load(f)
    

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


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
# market_items = [
#     {
#         "id": 1, 
#         "item": "Bored Ape #4211", 
#         "starting_price": 0.5, 
#         "seller_min_price": 0.4, # Add this for the AI
#         "seller_wallet": "0x...",
#         "status": "available"
#     },
# ]
@app.get("/items")
async def get_items():
    return load_db()

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    market_items = load_db()
    item = next((i for i in market_items if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items")
async def create_item(item_data: dict):
    market_items = load_db()
    
    # Generate ID based on the last item in the file
    new_id = market_items[-1]["id"] + 1 if market_items else 1
    
    new_item = {
        "id": new_id,
        "item": item_data.get("item"),
        "starting_price": item_data.get("starting_price"),
        "seller_min_price": item_data.get("seller_min_price"),
        "seller_personality": item_data.get("seller_personality", "balanced"),
        "seller_wallet": item_data.get("seller_wallet"),
        "status": "available"
    }
    
    market_items.append(new_item)
    save_db(market_items)  # Save to file!
    
    return {"status": "success", "item": new_item}