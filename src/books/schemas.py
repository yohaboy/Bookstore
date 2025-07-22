from pydantic import BaseModel, Field
from src.books.models import BookModel

class Book(BaseModel):
    title: str
    author: str
    price: float

class BooksResponse(BaseModel):
    books: list[BookModel]