import os
from openai import AsyncOpenAI


async def voice_to_text(path: str) -> str:
    client = AsyncOpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))

    audio_file = open(path, "rb")
    transcription = await client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )

    return transcription.text
