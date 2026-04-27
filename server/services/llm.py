import json

from openai import AsyncOpenAI
from pydantic import ValidationError

from config.settings import settings
from schemas.negotiation import AgentTurn

_FALLBACK_JSON = json.dumps({"message": "Unable to negotiate right now.", "offer_price": 0, "status": "cancel"})


def _coerce_json(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:].strip()

    try:
        json.loads(cleaned)
        return cleaned
    except (json.JSONDecodeError, TypeError):
        return _FALLBACK_JSON


def _validate_agent_turn_json(text: str) -> str:
    normalized = _coerce_json(text)
    try:
        parsed = AgentTurn.model_validate_json(normalized)
        return parsed.model_dump_json()
    except ValidationError:
        return _FALLBACK_JSON


class LLMService:
    def __init__(self, api_key: str | None = None) -> None:
        resolved_key = settings.api_key if api_key is None else api_key
        self.model_name = settings.model_name
        self.client = AsyncOpenAI(api_key=resolved_key, base_url=settings.base_url) if resolved_key else None

    def is_available(self) -> bool:
        return self.client is not None

    async def completion(self, prompt: str, system_prompt: str, model: str | None = None) -> str:
        if not self.client:
            return _FALLBACK_JSON

        chosen_model = model or self.model_name
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        try:
            response = await self.client.chat.completions.create(
                model=chosen_model,
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.4,
            )
        except Exception:
            response = await self.client.chat.completions.create(
                model=chosen_model,
                messages=messages,
                temperature=0.4,
            )

        content = response.choices[0].message.content or ""
        return _validate_agent_turn_json(content)


_service = LLMService()


async def call_llm(prompt: str, system_prompt: str) -> str:
    return await _service.completion(prompt, system_prompt)
