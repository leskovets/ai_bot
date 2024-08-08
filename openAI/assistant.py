import os
from openai import AsyncOpenAI

from openAI.openai_tools import tools
from db.db_handler import add_tread_from_chat_id, get_tread_id_or_none


async def get_answer_from_assistant(question: str, chat_id: int) -> str:

    client = AsyncOpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))
    
    assistant = await client.beta.assistants.create(
        name="assistant",
        model="gpt-4o",
        tools=tools

    )
    tread_id = await get_tread_id_or_none(chat_id)
    if tread_id is None:
        thread = await client.beta.threads.create()
        tread_id = thread.id
        await add_tread_from_chat_id(chat_id, tread_id)

    message = await client.beta.threads.messages.create(
        thread_id=tread_id,
        role="user",
        content=question,
    )

    await client.beta.threads.runs.create_and_poll(
        thread_id=tread_id,
        assistant_id=assistant.id,
    )

    response = await client.beta.threads.messages.list(thread_id=tread_id)
    response = response.data[0].content[0].text.value

    return response
