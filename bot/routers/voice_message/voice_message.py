from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
router = Router()


@router.message(Command('start'))
async def start(message: Message) -> None:
    text = f'Привет. Ты можешь задать мне вопрос головым сообщением и я отвечу тебе.'
    await message.answer(text)


@router.message(F.voice)
async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    file = await message.bot.get_file(file_id)
    file_path = file.file_path
    await message.bot.download_file(file_path, "123.mp3")
    await message.answer('голосовое получено')
