from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class Book(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    author: str
    price: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None