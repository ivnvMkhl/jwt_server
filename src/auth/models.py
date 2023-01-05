from datetime import datetime

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import Column, String, TIMESTAMP, Integer
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, get_async_session


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
    username = Column(String(length=320), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)