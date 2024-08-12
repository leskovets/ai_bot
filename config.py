from concurrent.futures import ThreadPoolExecutor

from amplitude import Amplitude
from openai import AsyncOpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PGHOST: str
    PGPORT: int
    PGUSER: str
    PGPASSWORD: str
    PGDATABASE: str
    API_TOKEN_OPENAI: str
    API_TOKEN_TELEGRAM: str
    AMPLITUDE_API_KEY: str
    DB_ECHO: bool = False
    REDIS_URL: str


    @property
    def postgres_url(self):
        return f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

executor = ThreadPoolExecutor()

am_client = Amplitude(settings.AMPLITUDE_API_KEY)

client = AsyncOpenAI(api_key=settings.API_TOKEN_OPENAI)
