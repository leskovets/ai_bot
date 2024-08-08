__all__ = ('router', )

from aiogram import Router

from .start import router as start_router
from .test import router as test_router

router = Router()

router.include_routers(
    start_router,
    test_router,

)
