import os
import time

from openai import OpenAI


def submit_message(assistant_id, thread, user_message, client):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


def get_answer(messages):
    answer = ''
    for m in messages:
        answer = f"{m.content[0].text.value}"

    return answer


def wait_on_run(run, thread, client):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


def get_answer_from_open_ai(question: str) -> str:

    client = OpenAI(api_key=os.getenv('API_TOKEN_OpenAI'))

    assistant = client.beta.assistants.create(
        name="My AI",
        instructions="You are my assistant in the search for information."
                     " Answer questions briefly, in a sentence or less.",
        model="gpt-4-1106-preview",
    )

    thread = client.beta.threads.create()
    run = submit_message(assistant.id, thread, question, client)

    run = wait_on_run(run, thread, client)

    response = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    text = get_answer(response)

    return text
