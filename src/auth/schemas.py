import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass
    username: str
    registered_at: str


class UserCreate(schemas.BaseUserCreate):
    pass
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
    username: str
