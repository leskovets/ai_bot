import os

from openai import AsyncOpenAI

from config import settings


async def text_in_voice(text: str, path: str) -> None:

    client = AsyncOpenAI(api_key=settings.API_TOKEN_OPENAI)

    response = await client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text,
    )

    response.stream_to_file(path)
