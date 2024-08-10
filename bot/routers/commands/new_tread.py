from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from amplitude import BaseEvent

from config import am_client, executor
from db.db_handler import del_user

router = Router()


@router.message(Command('new_tread'))
async def start(message: Message) -> None:
    executor.submit(am_client.track(BaseEvent(
        event_type='User started a new branch with an assistant', user_id=str(message.chat.id))))
    await del_user(message.chat.id)
    text = f'Начата новая тема, можешь задавать вопросы'
    await message.answer(text)
