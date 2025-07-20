from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    email: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)
    username: str = Field(nullable=False, unique=True, max_length=12)


