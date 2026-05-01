from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

current_dir=Path(__file__).parent.parent

class Settings(BaseSettings):
    api_key: str
    model_name: str = "google/gemma-4-26b-a4b-it:free"
    base_url: str | None = "https://openrouter.ai/api/v1"
    max_negotiation_rounds: int = 6

    model_config = SettingsConfigDict(env_file=os.path.join(current_dir,".env"), extra="ignore")


settings = Settings()