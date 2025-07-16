from pydantic import BaseModel
from typing import Optional

class BookModel(BaseModel):
    title : Optional[str] = None
    author: Optional[str] = None
    price : Optional[float] = None
