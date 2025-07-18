from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import settings

engine = create_async_engine(
        url = settings.DATABASE_URL,
        echo = True
    )

async def database_init():
    async with engine.begin() as conn:
        from src.books.models import BookModel
        from src.Auth.models import User
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession: # type: ignore
    Session = sessionmaker(
        bind=engine,
        class_= AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
