from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(
    url=settings.postgres_url,
    echo=settings.DB_ECHO,
)

session_factory = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class Treads(Base):
    __tablename__ = 'treads'

    chat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    tread_id: Mapped[str | None]
    key_value: Mapped[str | None]
