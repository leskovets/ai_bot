import os

from openai import AsyncOpenAI
from openAI.openai_tools import tools
from db.db_handler import add_tread_from_chat_id, get_tread_id_or_none


async def get_answer_from_assistant(question: str, chat_id: int) -> str:
    client = AsyncOpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))

    assistant = await client.beta.assistants.create(
        name="assistant",
        instructions="your main task is to find out my hobbies, "
                     "find out my hobbies from the message history,"
                     "don't ask me questions about my hobbies, "
                     "use the save_value function to save my hobby",
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

    run = await client.beta.threads.runs.create_and_poll(
        thread_id=tread_id,
        assistant_id=assistant.id,
    )

    if run.status == 'requires_action':
        tool_outputs = []

        for tool in run.required_action.submit_tool_outputs.tool_calls:
            if tool.function.name == "save_value":
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": 'seve'
                })
            elif tool.function.name == "get_rain_probability":
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": "0.06"
                })
            print(tool.function)

        if tool_outputs:
            try:
                run = await client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=tread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                print("Tool outputs submitted successfully.")
            except Exception as e:
                print("Failed to submit tool outputs:", e)
        else:
            print("No tool outputs to submit.")

    response = await client.beta.threads.messages.list(thread_id=tread_id)
    response = response.data[0].content[0].text.value

    return response
