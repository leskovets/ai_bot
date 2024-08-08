from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.db_handler import del_user

router = Router()


@router.message(Command('new_tread'))
async def start(message: Message) -> None:
    await del_user(message.chat.id)
    text = f'Начата новая тема, можешь задавать вопросы'
    await message.answer(text)
