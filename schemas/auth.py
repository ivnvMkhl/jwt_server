from pydantic import BaseModel
from core.config import AUTH_SECRET_KET

class User(BaseModel):
    username: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = AUTH_SECRET_KET