from fastapi import APIRouter ,Depends ,status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UserService
from .schema import UserCreation ,UserLogin
from src.database.main import get_session
from .utils import verify_hash ,create_access_token
from datetime import timedelta


auth_router = APIRouter()
auth_service = UserService()

@auth_router.post('/signup' ,response_model=UserCreation)
async def register(user_data:UserCreation , session:AsyncSession = Depends(get_session)):
    new_user = await auth_service.create_user(user_data ,session)
    return new_user

@auth_router.post('/login')
async def login(user_data: UserLogin , session:AsyncSession = Depends(get_session)):
    email = user_data.email
    user = await auth_service.get_user(email ,session)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    is_verified = verify_hash(
        password=user_data.password,
        hash=user.password
    )

    if is_verified:
        access_token = create_access_token(
            user_data={
                'email':user.email,
                'username':user.username
            }
        )

        refresh_token = create_access_token(
            user_data={
                'email':user.email,
                'username':user.username
            },
            refresh=True,
            expiry=timedelta(days=3)
        )

        return JSONResponse(
            content={
                "message": "login successful",
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        )

    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="wrong credentials"
        )