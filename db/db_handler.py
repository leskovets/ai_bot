
from sqlalchemy import select

from database import Treads
from db.config_db import session_factory


async def add_tread_from_chat_id(chat_id: int, tread_id: int) -> None:
    user = Treads(
        chat_id=chat_id,
        tread_id=tread_id
    )
    async with session_factory() as session:
        await session.add(user)
        await session.commit()


async def get_tread_id_or_none(chat_id: int) -> int | None:
    async with session_factory() as session:
        user = session.get(Treads, chat_id)

    return user.tread_id
