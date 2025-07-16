from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.database.main import database_init

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server starting ....")
    await database_init()
    yield
    print("server stopped !! ")

version = "v1"

app = FastAPI(
    version= version,
    title="Book Store",
    lifespan= life_span
)

app.include_router(book_router, prefix=f"/api/{version}")