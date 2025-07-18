from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from .models import User

class UserService():
    async def get_user(self, email:str , session:AsyncSession):
        statement = select(User).where(User.email == email)
        user = await session.execute(statement)
        return user.scalar_one_or_none()

    async def create_user(self, user_data : User, session :AsyncSession):
        user_dict = user_data.model_dump()
        user_email = user_dict["email"]
        user = await self.get_user(user_email ,session)
        if not user:
            new_user = User(
                **user_dict
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
