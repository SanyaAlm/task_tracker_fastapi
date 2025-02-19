from typing import AsyncGenerator, Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core import settings

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL,  pool_size=30, max_overflow=20, pool_timeout=60)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def async_get_db() -> AsyncGenerator[AsyncSession, Any]:
    async with AsyncSessionLocal() as session:
        yield session