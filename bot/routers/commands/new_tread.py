from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from amplitude import BaseEvent

from config import am_client, executor, client

router = Router()


@router.message(Command('new_tread'))
async def start(message: Message, state: FSMContext) -> None:

    thread = await client.beta.threads.create()
    await state.update_data({'tread_id': thread.id})

    text = f'Начата новая тема, можешь задавать вопросы'
    await message.answer(text)

    executor.submit(am_client.track(BaseEvent(
        event_type='User started a new branch with an assistant', user_id=str(message.chat.id))))
