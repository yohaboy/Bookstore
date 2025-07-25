from sqlmodel import SQLModel ,Field,Column
from sqlalchemy.dialects import postgresql as pg
from datetime import datetime
import uuid

class BookModel(SQLModel , table=True):
    __tablename__ = "books_table"
    
    id : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title : str
    author: str
    price : float
    created_at : datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
    updated_at : datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )
