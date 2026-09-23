from datetime import datetime, time

from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="UTF-8", env_file=".env")
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: int
    GROQ_API_KEY: str
    DATABASE_URL: str
    DELIVERY_MODE: Literal["digest", "realtime"] = "digest"
    DIGEST_SCHEDULE: list[time]
    DIGEST_MAX_ARTICLES: int

    @field_validator("DIGEST_SCHEDULE", mode="before")
    @classmethod
    def parse_schedule(cls, v):
        time_one = time.fromisoformat("08:00")
        time_two = time.fromisoformat("18:00")
        return time


settings = Settings()


