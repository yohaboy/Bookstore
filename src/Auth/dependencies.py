from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi import Request, status ,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from .utils import decode_token
from .services import UserService
from src.database.main import get_session

auth_service = UserService()

class AuthBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        token = credentials.credentials
        if self.valid_token(token):
            return credentials.credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invlaid token")

    def valid_token(self,token:str):
        if decode_token(token) is not None:
            return True
        else:
            return False
        
async def current_user(token_data:str = Depends(AuthBearer()) , session:AsyncSession = Depends(get_session)):
    decoded = decode_token(token_data)
    if decoded:
        email = decoded["user"]["email"]
        user = await auth_service.get_user(email ,session)
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or expired token")

class RoleBasedAccess:
    def __init__(self , allowed_roles:list):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user = Depends(current_user)):
        if current_user.role in self.allowed_roles:
            return True
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this"
        )