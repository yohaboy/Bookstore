from passlib.context import CryptContext

password_context = CryptContext(
    schemes=['bcrypt']
)

def password_hasher(password: str):
    hashed = password_context.hash(password)
    return hashed

def verify_hash( password: str, hash: str):
    is_correct = password_context.verify(
        secret= password,
        hash= hash
    )
    return is_correct