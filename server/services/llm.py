import os

from openai import OpenAI


class LLMService:
    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def is_available(self) -> bool:
        return self.client is not None

    def completion(self, system_prompt: str, user_prompt: str, model: str = "gpt-4o-mini") -> str:
        if not self.client:
            return "LLM unavailable: OPENAI_API_KEY not configured."

        response = self.client.responses.create(
            model=model,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.output_text
