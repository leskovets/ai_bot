from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
router = Router()


@router.message(Command('start'))
async def start(message: Message) -> None:
    text = f'Привет. Ты можешь задать мне вопрос головым сообщением и я отвечу тебе.'
    await message.answer(text)

