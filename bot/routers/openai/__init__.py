__all__ = ('router', )

from aiogram import Router

from .voice import router as voice_router
from .text import router as text_router
from .photo import router as photo_router

router = Router()

router.include_routers(
    voice_router,
    text_router,
    photo_router,

)
