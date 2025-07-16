from fastapi import APIRouter ,status
from src.books.book_list import Books
from src.books.schema import BookModel
from fastapi.exceptions import HTTPException

book_router = APIRouter()

@book_router.get('/')
async def get_all_books() -> dict:
    return {'books':Books}

@book_router.get('/{id}')
async def get_a_book(id:int) -> dict:
    for book in Books:
        if book['id'] == id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@book_router.post('/add' ,status_code=status.HTTP_201_CREATED)
async def add_book(book_data : BookModel):
    Books.append(book_data.model_dump())
    return {"message": "Book added successfully", "book": book_data}

@book_router.patch('/{id}')
async def update_a_book(id:int , book_data : BookModel) -> dict:
    for book in Books:
        if book['id'] == id:
            if book_data.title is not None:
                book['price'] = book_data.price
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@book_router.delete('/{id}')
async def delete_a_book(id:int) -> dict:
    for book in Books:
        if book['id'] == id:
            Books.remove(book)
            return {'books':Books}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')
