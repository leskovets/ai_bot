from db.database import Treads
from db.config_db import session_factory


async def add_tread_from_chat_id(chat_id: int, tread_id: str) -> None:
    user = Treads(
        chat_id=chat_id,
        tread_id=tread_id
    )
    async with session_factory() as session:
        session.add(user)
        await session.commit()


async def get_tread_id_or_none(chat_id: int) -> str | None:
    async with session_factory() as session:
        user = await session.get(Treads, chat_id)
    if user is not None:
        return user.tread_id
    return user


async def del_user(chat_id: int) -> None:
    async with session_factory() as session:
        user = await session.get(Treads, chat_id)
    if user is not None:
        await session.delete(user)
        await session.commit()


async def update_key_value_by_chat_id(chat_id: int, key_value: str) -> None:
    async with session_factory() as session:
        user = await session.get(Treads, chat_id)
        user.key_value = key_value
        await session.commit()
