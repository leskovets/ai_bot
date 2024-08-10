from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from amplitude import BaseEvent

from config import am_client, executor


router = Router()


@router.message(Command('start'))
async def start(message: Message) -> None:

    text = f'Привет. Ты можешь задать мне вопрос головым сообщением и я отвечу тебе.'
    await message.answer(text)

    executor.submit(am_client.track(BaseEvent(event_type='User click start', user_id=str(message.chat.id))))
