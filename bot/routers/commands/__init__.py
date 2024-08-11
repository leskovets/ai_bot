__all__ = ('router', )

from aiogram import Router

from .start import router as start_router
from .new_tread import router as new_tread_router

router = Router()

router.include_routers(
    start_router,
    new_tread_router,

)
