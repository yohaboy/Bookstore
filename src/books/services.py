from sqlmodel import select,desc
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.models import BookModel
from .schemas import Book
import uuid

class BookService():
    async def get_all_books(self , session : AsyncSession):
        statment = select(BookModel).order_by(desc(BookModel.created_at))
        book = await session.exec(statment)
        return book.all()
    
    async def get_a_book(self ,id:uuid.UUID, session : AsyncSession):
        statment = select(BookModel).where(BookModel.id == id)
        result = await session.exec(statment)
        return result.first()
    
    async def add_book(self ,book_data:Book , session : AsyncSession):
        book_dict = book_data.model_dump()
        new_book = BookModel(
            **book_dict
        )
        session.add(new_book)
        await session.commit()
        return new_book
    
    async def update_a_book(self ,id:uuid.UUID, book_data:Book, session : AsyncSession):
        book_dict = book_data.model_dump()
        book = await self.get_a_book(id , session)
        for key,value in book_dict.items():
            setattr(book , key ,value)
        await session.commit()
        return book
    async def delete_a_book(self ,id:uuid.UUID, session : AsyncSession):
        book = await self.get_a_book(id , session)
        session.remove(book)
        await session.commit()