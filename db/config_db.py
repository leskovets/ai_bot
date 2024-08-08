import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

db_url = "postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USER=os.getenv('DB_USER'),
    DB_PASS=os.getenv('DB_PASS'),
    DB_HOST=os.getenv('DB_HOST'),
    DB_PORT=os.getenv('DB_PORT'),
    DB_NAME=os.getenv('DB_NAME'),
)
engine = create_async_engine(
    url=db_url,
    echo=True,
)
session_factory = async_sessionmaker(engine)
