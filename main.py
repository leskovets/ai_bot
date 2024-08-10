import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from amplitude import Amplitude

from config import settings
from bot.routers import router as main_router


async def main() -> None:

    amplitude_client = Amplitude(settings.AMPLITUDE_API_KEY)

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger('main')
    logger.debug('Start main')

    bot = Bot(settings.API_TOKEN_telegram)
    await bot.set_my_commands([
        BotCommand(command='start', description='старт'),
        BotCommand(command='new_tread', description='сбросить историю сообщений'),
    ])
    dp = Dispatcher()

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except Exception as ex:
        logger.error(ex)


if __name__ == '__main__':
    asyncio.run(main())
