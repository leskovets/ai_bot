import os
import logging
from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from amplitude import BaseEvent

from config import executor, am_client
from openai.TTS import text_in_voice
from openai.assistant import get_answer_from_assistant
from openai.whisper import voice_to_text

router = Router()
logger = logging.getLogger('voice_router')


@router.message(F.voice)
async def voice_handler(message: Message):
    executor.submit(am_client.track(BaseEvent(
        event_type='User uploaded a voice', user_id=str(message.chat.id))))
    file_id = message.voice.file_id
    file = await message.bot.get_file(file_id)
    file_path = file.file_path
    file_name = f"{message.chat.id}_{datetime.now()}.mp3"

    await message.bot.download_file(file_path, file_name)
    logger.debug(f"download_audio complete, filename: '{file_name}'")

    text = await voice_to_text(file_name)
    logger.debug(f"converting from sound to text: {text}")

    answer = await get_answer_from_assistant(text, message.chat.id)
    logger.debug(f"response from the assistant: {answer}")

    await text_in_voice(answer, file_name)
    logger.debug(f"convert text to sound")

    image_from_pc = FSInputFile(file_name)
    await message.reply_voice(image_from_pc)

    logger.debug(f"send voice to user")
    os.remove(file_name)
