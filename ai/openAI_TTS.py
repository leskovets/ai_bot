import os

from openai import OpenAI


def text_in_voice(text: str, file_name: str) -> None:

    client = OpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))

    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )

    response.stream_to_file(file_name)
