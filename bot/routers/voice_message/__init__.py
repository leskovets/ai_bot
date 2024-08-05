__all__ = ('router', )

from aiogram import Router

from .voice_message import router as commands_router

router = Router()

router.include_routers(
    commands_router,
)
