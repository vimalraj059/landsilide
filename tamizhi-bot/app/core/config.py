import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "Tamizhi BOT")
    debug: bool = os.getenv("DEBUG", "false").lower() in {"1", "true", "yes"}
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./tamizhi.db")


settings = Settings()

