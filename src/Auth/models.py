from sqlmodel import SQLModel ,Field ,column


class User(SQLModel):
    email:str = Field(nullable=False )
    password:str = Field(min_length=6, exclude=True)
    username:str = Field(max_length=12 ,unique=True)

