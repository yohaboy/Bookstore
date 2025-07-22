from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi import Request, status
from .utils import decode_token

class AuthBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        token = credentials.credentials
        if self.valid_token(token):
            return credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invlaid token")

    def valid_token(self,token:str):
        if decode_token(token) is not None:
            return True
        else:
            return False