# DOCUMENTATION

Last doc sync baseline: 1bebd2a (2026-04-23 01:53:59 +0530)

## API Endpoints

### GET /
Purpose: health/basic status check.

Response:
- message: string

Example response:
- { "message": "Backend running" }

### POST /start-negotiation
Purpose: run buyer and seller negotiation loop and return agreement outcome.

Request body:
- item: string
- start_price: number (> 0)
- min_price: number (> 0)
- max_price: number (> 0)
- personality: string (default: balanced)

Response body:
- status: string (currently agreed | no_agreement)
- item: string
- agreed_price: number | null
- rounds: array of round objects

Round object:
- round: number
- buyer_offer: number
- seller_offer: number

## Agent JSON Schema

### Target Per-turn Agent Message Contract
Use this schema for chat-style agent turns and frontend rendering:

- message: string
- offer_price: number
- status: counter | accept | cancel

Example:
- {
    "message": "I can do 0.008 ETH",
    "offer_price": 0.008,
    "status": "counter"
  }

### Current Backend Negotiation Response Contract
Current implementation returns aggregate negotiation result with round history rather than per-turn message payload.

## Negotiation Loop Behavior
- Entry point: start price is clamped within min/max boundaries.
- Turn order: buyer offer then seller offer each round.
- Max rounds default: 6.
- Agreement condition: buyer_offer >= seller_offer.
- Agreement price: midpoint of buyer and seller offers.
- No-agreement condition: loop exits after max rounds without crossing.

## Personality Behavior
- conservative: smaller concessions.
- aggressive: larger/faster concessions.
- balanced: moderate concession behavior.

## Smart Contract Interaction

### Contract
- File: solidity/Arguing.sol
- Contract: Deals

### Write Function
- createDeal(address buyer, address seller, uint256 price, string item)
- Validates non-zero buyer/seller and positive price.
- Stores deal with timestamp.
- Emits DealCreated event.

### Read Functions
- getDealsCount() -> uint256
- getDeal(index) -> buyer, seller, price, item, timestamp

### On-chain Storage
- buyer
- seller
- price
- item
- timestamp

### Not Stored On-chain
- Full chat transcript between agents

## New Functions And Classes

### Backend Entrypoint
- main.py
  - root()
  - start_negotiation(req)

### Agents
- agents/buyer.py
  - BuyerAgent
  - next_offer(...)
- agents/seller.py
  - SellerAgent
  - next_offer(...)
- agents/negotiation.py
  - run_negotiation(req, max_rounds=6)

### Schemas
- schemas/negotiation.py
  - NegotiationRequest
  - NegotiationResult
  - NegotiationResponse

### Services
- services/llm.py
  - LLMService
  - completion(...)

## Gaps And Next Documentation Updates
- Document finalize-deal backend endpoint once implemented.
- Add wallet flow details once wagmi/viem integration is added.
- Add request/response samples for on-chain execution route.
- Add explicit error response schema for validation and transaction failures.
