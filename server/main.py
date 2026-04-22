from fastapi import FastAPI

from agents.negotiation import run_negotiation
from config.settings import settings
from schemas.negotiation import NegotiationRequest, NegotiationResponse

app = FastAPI(title=settings.app_name)

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/start-negotiation")
def start_negotiation(req: NegotiationRequest) -> NegotiationResponse:
    return run_negotiation(req)