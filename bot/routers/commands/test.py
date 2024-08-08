from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.db_handler import add_tread_from_chat_id, get_tread_id_or_none


router = Router()


@router.message(Command('add'))
async def add(message: Message) -> None:
    await add_tread_from_chat_id(message.chat.id, 12123)
    await message.answer('ok')


@router.message(Command('add'))
async def gat(message: Message) -> None:

    tread_id = await get_tread_id_or_none(message.chat.id)
    await message.answer(str(tread_id))
