import asyncio
import logging
import os
from logging.config import dictConfig

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from aiogram.types import BotCommand

from bot.routers import router as main_router
from logger_setup import dict_config


async def main() -> None:
    logging.config.dictConfig(dict_config)

    logger = logging.getLogger('main')

    load_dotenv('.env')

    token = os.getenv('API_TOKEN_telegram')
    bot = Bot(token)
    await bot.set_my_commands([
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='reminder', description='Напоминания'),
        BotCommand(command='history', description='История молитв'),

    ])
    dp = Dispatcher()

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    asyncio.run(main())
