import base64
import requests

from config import settings


def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def photo_to_emotions(path: str) -> str:

    base64_image = encode_image(path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.API_TOKEN_OPENAI}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "determine the mood from the photo. "
                                "please send the answer in Russian"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()['choices'][0]['message']['content']
