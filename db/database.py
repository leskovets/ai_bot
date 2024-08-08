from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Treads(Base):
    __tablename__ = 'treads'

    chat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    tread_id: Mapped[int | None]
    key_value: Mapped[str | None]
