from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings

engine = create_async_engine(
        url = settings.DATABASE_URL,
        echo = True
    )

async def database_init():
    async with engine.begin() as conn:
        from src.books.models import BookModel
        await conn.run_sync(SQLModel.metadata.create_all)