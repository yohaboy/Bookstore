from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlmodel import select
from src.Auth.models import User
from src.Auth.schema import UserCreation
from .utils import password_hasher

class UserService():
    async def get_user(self, email:str , session:AsyncSession):
        statement = select(User).where(User.email == email)
        user = await session.execute(statement)
        return user.scalar_one_or_none()

    async def create_user(self, user_data: UserCreation, session: AsyncSession):
            user = await self.get_user(user_data.email, session)
            if user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="User already exists"
                )

            # Hash password and create user
            new_user = User(
                **user_data.model_dump(exclude={"password"})
            )
            new_user.password = password_hasher(user_data.password)

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
