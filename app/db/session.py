import os
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.logger import logger

load_dotenv()

DB_DSN = os.getenv("DB_DSN")
if DB_DSN is None:
    logger.error("Missing DB_DSN environment variable")
    raise ValueError("Missing DB_DSN environment variable")

engine = create_async_engine(url=DB_DSN)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)


class Base(DeclarativeBase):
    pass


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
