import os
import json

from openai import AsyncOpenAI

from openAI.completions import validate_key_value
from openAI.openai_tools import assistant_tools
from db.db_handler import add_tread_from_chat_id, get_tread_id_or_none, update_key_value_by_chat_id


async def get_answer_from_assistant(question: str, chat_id: int) -> str:
    client = AsyncOpenAI(api_key=os.getenv('API_TOKEN_OPENAI'))

    assistant = await client.beta.assistants.create(
        name="assistant",
        instructions="your main task in communicating with me is to find out my key values, "
                     "then they will need to be saved using your save_value function. "
                     "if the answer is True, then the data is saved, "
                     "if False, then this value does not fit, you need to look further",
        model="gpt-4o",
        tools=assistant_tools

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
                arguments = json.loads(tool.function.arguments)
                key_value = arguments.get('key_value')

                res = await validate_key_value(key_value)

                if res == 'True':
                    await update_key_value_by_chat_id(chat_id, key_value)
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": res
                })

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
