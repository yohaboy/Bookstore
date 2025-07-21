from datetime import timedelta ,datetime
from passlib.context import CryptContext
from src.config import settings
import jwt ,uuid

password_context = CryptContext(
    schemes=['bcrypt']
)

DEFAULT_EXPIRY_DATE = 3600 # 1 Hour 

def password_hasher(password: str):
    hashed = password_context.hash(password)
    return hashed

def verify_hash( password: str, hash: str):
    is_correct = password_context.verify(
        secret= password,
        hash= hash
    )
    return is_correct

def create_access_token(user_data: dict , expiry: timedelta = None ,refresh : bool = False):
    payload = {}

    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=DEFAULT_EXPIRY_DATE))
    payload['jti'] = str(uuid.uuid4)
    payload['refresh'] = refresh
    
    token = jwt.encode(
        payload = payload,
        key = settings.JWT_KEY,
        algorithm = settings.JWT_ALGORITHM
    )
    return token

def decode_token(token: str):
    try :
        token_data = jwt.decode(
            jwt=token,
            key=settings.JWT_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return token_data
    except jwt.PyJWTError:
        return None 