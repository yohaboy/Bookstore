from sqlmodel import create_engine,text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import settings

engine = AsyncEngine(
    create_engine(
        url = settings.DATABASE_URL,
        echo = True
    )
)

async def database_init():
    async with engine.begin() as conn:
        statment = text("SELECT 'It worked' ")
        result = await conn.execute(statment)
    print(result.all())