import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from aiogram.types import BotCommand

from bot.routers import router as main_router


async def main() -> None:

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger('main')
    logger.debug('Start main')

    load_dotenv('.env')

    token = os.getenv('API_TOKEN_telegram')
    bot = Bot(token)
    await bot.set_my_commands([
        BotCommand(command='start', description='старт'),
    ])
    dp = Dispatcher()

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    asyncio.run(main())
