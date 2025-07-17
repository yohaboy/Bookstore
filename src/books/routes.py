from fastapi import APIRouter ,status ,Depends
from src.books.models import BookModel
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.services import BookService
from src.database.main import get_session

book_router = APIRouter()
book_service = BookService()

@book_router.get('/' , response_model=BookModel)
async def get_all_books(session:AsyncSession = Depends(get_session)) -> dict:
    books = await book_service.get_all_books(session)
    return {"books":books}

@book_router.get('/{id}' , response_model=BookModel)
async def get_a_book(id:str ,session:AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_a_book(id , session)
    if book:
        return {"books":book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@book_router.post('/add' ,status_code=status.HTTP_201_CREATED ,response_model=BookModel)
async def add_book(book_data : BookModel , session:AsyncSession = Depends(get_session)):
    book = await book_service.add_book(book_data,session)
    if book:
        return {"message": "Book added successfully", "book": book}
    return {"message": "error while adding the book !!"}

@book_router.patch('/{id}' , response_model=BookModel)
async def update_a_book(id:str , book_data : BookModel , session:AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.update_a_book(id , book_data , session)
    if book:
        return {"books":book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@book_router.delete('/{id}' ,response_model=BookModel)
async def delete_a_book(id:str , session:AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.delete_a_book(id ,session)
    if book:
        return {"books":book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')
