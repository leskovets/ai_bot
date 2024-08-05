import os
from datetime import datetime

import whisper
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


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
    file_name = f"{message.chat.id}_{datetime.now()}.mp3"
    await message.bot.download_file(file_path, file_name)

    model = whisper.load_model("base")
    result = model.transcribe(file_name)
    text = result["text"]

    os.remove(file_name)

    await message.answer(text)
