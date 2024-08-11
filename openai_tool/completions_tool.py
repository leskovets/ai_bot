import json
import os

from openai import AsyncOpenAI

from config import settings
from openai.openai_tools import completions_tool

client = AsyncOpenAI(api_key=settings.API_TOKEN_OPENAI)


async def validate_key_value(key_value: str) -> str:
    messages = [
        {"role": "system", "content": "you are a validator, you determine the correctness of the entered data"},
        {"role": "user", "content": f"can this be a human value: a '{key_value}'"}
    ]

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=completions_tool,
    )

    tool_call = response.choices[0].message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)

    is_valid = arguments.get('is_valid')
    return is_valid
