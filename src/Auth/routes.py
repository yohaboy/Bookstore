from fastapi import APIRouter, HTTPException ,status ,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UserService
from .models import User
from src.database.main import get_session

auth_route = APIRouter()
user_service = UserService()

@auth_route.post("/signin")
async def signin(user_data:User,session:AsyncSession = Depends(get_session)):
    email = user_data.email
    user = await user_service.get_user(email ,session)
    if user:
        if user.password == user_data.password:
            return user   
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT , detail="user not found ")

@auth_route.post("signup")
async def signup(user_data:User ,session:AsyncSession = Depends(get_session)):
    user = await user_service.create_user(user_data,session)
    if user:
        raise HTTPException(status_code=status.HTTP_201_CREATED)
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Error while creating user")