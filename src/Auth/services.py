from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from src.Auth.models import User
from src.Auth.schema import UserCreation
from .utils import password_hasher

class UserService():
    async def get_user(self, email:str , session:AsyncSession):
        statement = select(User).where(User.email == email)
        user = await session.execute(statement)
        return user.scalar_one_or_none()

    async def create_user(self, user_data : UserCreation, session :AsyncSession):
        user_dict = user_data.model_dump()
        user_email = user_dict["email"]
        user = await self.get_user(user_email ,session)
        if not user:
            new_user = User(
                **user_dict
            )
            new_user.password = password_hasher(user_dict["password"])
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
