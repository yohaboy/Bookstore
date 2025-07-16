from fastapi import FastAPI ,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

Books = [
    {
     'id':1,
     'title' : 'The King',
     'author' :'john zee',
     'price':1200
    },

    {
     'id':2,
     'title' : 'Amongst US',
     'author' :'suiii',
     'price':90
    },

    {
     'id':3,
     'title' : 'Bright dawn',
     'author' :'rock',
     'price':870
    }
]

class BookModel(BaseModel):
    title : Optional[str] = None
    author: Optional[str] = None
    price : Optional[float] = None


@app.get('/')
async def get_all_books() -> dict:
    return {'books':Books}

@app.get('/{id}')
async def get_a_book(id:int) -> dict:
    for book in Books:
        if book['id'] == id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@app.patch('/{id}')
async def update_a_book(id:int , book_data : BookModel) -> dict:
    for book in Books:
        if book['id'] == id:
            if book_data.title is not None:
                book['price'] = book_data.price
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@app.delete('/{id}')
async def delete_a_book(id:int) -> dict:
    for book in Books:
        if book['id'] == id:
            Books.remove(book)
            return {'books':Books}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')
