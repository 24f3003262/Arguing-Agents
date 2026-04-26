import json

from openai import AsyncOpenAI

from config.settings import settings

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


class LLMService:
    def __init__(self, api_key: str | None = None) -> None:
        resolved_key = settings.api_key if api_key is None else api_key
        self.model_name = settings.model_name
        self.client = AsyncOpenAI(api_key=resolved_key, base_url=settings.base_url) if resolved_key else None

    def is_available(self) -> bool:
        return self.client is not None

    async def completion(self, prompt: str, model: str | None = None) -> str:
        if not self.client:
            return _FALLBACK_JSON

        response = await self.client.responses.create(
            model=model or self.model_name, input=[{"role": "user", "content": prompt}]
        )
        return _coerce_json(response.output_text or "")


_service = LLMService()


async def call_llm(prompt: str) -> str:
    return await _service.completion(prompt)
