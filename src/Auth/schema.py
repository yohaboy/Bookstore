from pydantic import BaseModel

class UserCreation(BaseModel):
    email:str
    password:str
    username:str

class UserLogin(BaseModel):
    email:str
    password:str
    username:str

    