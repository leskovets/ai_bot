from concurrent.futures import ThreadPoolExecutor

from amplitude import Amplitude
from openai import AsyncOpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    API_TOKEN_OPENAI: str
    API_TOKEN_telegram: str
    AMPLITUDE_API_KEY: str
    DB_ECHO: bool = False
    REDIS_URL: str

    @property
    def postgres_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

executor = ThreadPoolExecutor()

am_client = Amplitude(settings.AMPLITUDE_API_KEY)

client = AsyncOpenAI(api_key=settings.API_TOKEN_OPENAI)
