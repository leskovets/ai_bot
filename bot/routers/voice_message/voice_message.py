import os
import logging
from datetime import datetime

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from ai.openAI_TTS import text_in_voice
from ai.openAI_assistant import get_answer_from_open_ai
from ai.whisper import voice_to_text

router = Router()
logger = logging.getLogger('voice.message')


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
    logger.info(f" download_audio complete, filename: {file_name}")

    text = voice_to_text(file_name)
    logger.info(f" converting from sound to text: {text}")

    answer = get_answer_from_open_ai(text)
    logger.info(f" response from the assistant: {answer}")

    text_in_voice(answer, file_name)
    logger.info(f" convert text to sound")

    image_from_pc = FSInputFile(file_name)
    await message.reply_voice(image_from_pc)

    logger.info(f" send voice to user")
    os.remove(file_name)
