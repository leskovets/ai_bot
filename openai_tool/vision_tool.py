import base64
import requests

from openai import AsyncOpenAI

from config import settings


def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


async def photo_to_emotions(path: str) -> str:

    base64_image = encode_image(path)

    client = AsyncOpenAI(api_key=settings.API_TOKEN_OPENAI)

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "determine the mood from the photo. "
                                             "please send the answer in Russian"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content
