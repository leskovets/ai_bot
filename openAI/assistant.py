import os
from openai import AsyncOpenAI


async def get_answer_from_assistant(question: str) -> str:

    client = AsyncOpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))
    
    assistant = await client.beta.assistants.create(
        name="assistant",
        model="gpt-4o",
    )
    thread = await client.beta.threads.create()

    message = await client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question,
    )

    await client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    response = await client.beta.threads.messages.list(thread_id=thread.id)
    response = response.data[0].content[0].text.value

    return response
