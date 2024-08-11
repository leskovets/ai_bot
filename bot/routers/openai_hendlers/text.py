import logging

from aiogram import Router, F
from aiogram.types import Message

from openai_tool.assistant_tool import get_answer_from_assistant

router = Router()
logger = logging.getLogger('text_router')


@router.message(F.text)
async def text_message_handler(message: Message):

    answer = await get_answer_from_assistant(message.text, message.chat.id)
    logger.debug(f"response from the assistant: {answer}")

    await message.reply(text=answer)
