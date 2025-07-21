from fastapi import APIRouter ,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UserService
from .schema import UserCreation
from src.database.main import get_session


auth_router = APIRouter()
auth_service = UserService()

@auth_router.post('/signup' ,response_model=UserCreation)
async def register(user_data:UserCreation , session:AsyncSession = Depends(get_session)):
    new_user = await auth_service.create_user(user_data ,session)
    return new_user

@auth_router.post('/login')
async def login(email: str , session):
    pass