from sqlmodel import SQLModel, Field ,Column
from sqlalchemy.dialects import postgresql as pg

class User(SQLModel, table=True):
    email: str = Field(primary_key=True, nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)
    username: str = Field(nullable=False, unique=True, max_length=12)
    # role: str = Field(
    #     sa_column=Column(
    #         pg.VARCHAR,
    #         nullable=False,
    #         server_default="user"
    #     ))

