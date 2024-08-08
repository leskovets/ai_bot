from database import session_factory, Treads


def add_tread_from_chat_id(chat_id: int, tread_id: int) -> None:
    user = Treads(
        chat_id=chat_id,
        tread_id=tread_id
    )
    async with session_factory() as session:
        await session.add(user)
        await session.commit()
