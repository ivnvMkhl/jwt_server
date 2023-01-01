from typing import AsyncGenerator
from datetime import datetime

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

from database import DATABASE_URL


Base: DeclarativeMeta = declarative_base()

class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
    username = Column(String(length=320), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)