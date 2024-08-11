from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from amplitude import BaseEvent

from config import am_client, executor, client
from openai_tool.assistant_tools import assistant_tools

router = Router()


@router.message(Command('start'))
async def start(message: Message,  state: FSMContext) -> None:

    assistant = await client.beta.assistants.create(
        name="assistant",
        instructions="your main task in communicating with me is to find out my key values, "
                     "then they will need to be saved using your save_value function. "
                     "if the answer is True, then the data is saved, "
                     "if False, then this value does not fit, you need to look further",
        model="gpt-4o",
        tools=assistant_tools
    )

    thread = await client.beta.threads.create()
    await state.update_data({'tread_id': thread.id})
    await state.update_data({'assistant_id': assistant.id})

    text = f'Привет. Ты можешь задать мне вопрос головым сообщением и я отвечу тебе.'
    await message.answer(text)

    executor.submit(am_client.track(BaseEvent(event_type='User click start', user_id=str(message.chat.id))))
