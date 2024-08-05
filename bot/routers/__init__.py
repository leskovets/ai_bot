__all__ = ('router', )

from aiogram import Router

from .commands import router as commands_router
from .voice_message import router as voice_message_router

router = Router()

router.include_routers(
    commands_router,
    voice_message_router,

)
