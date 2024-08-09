import os
import logging

from aiogram import Router, F
from aiogram.types import Message

from openAI.vision import photo_to_emotions

router = Router()
logger = logging.getLogger('photo_router')


@router.message(F.photo)
async def photo_handler(message: Message):
    photo_id = message.photo[-1].file_id
    path = 'test.jpg'
    await message.bot.download(photo_id, destination=path)
    logger.debug('photo download to server')
    emotion = photo_to_emotions(path)
    logger.debug(f'emotion is received: {emotion}')
    await message.reply(emotion)
    os.remove(path)
