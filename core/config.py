from starlette.config import Config

config = Config(".env_dev")

DATABASE_URL = config("JWTS_DATABASE_URL", cast=str, default="")
AUTH_SECRET_KET = config("JWTS_AUTH_SECRET_KET", cast=str, default="")
HOST = config("JWTS_HOST", cast=str, default="127.0.0.1")
PORT = config("JWTS_PORT", cast=int, default=8000)
DB_USER = config("JWTS_DB_USER", cast=str, default="")
DB_HOST = config("JWTS_DB_HOST", cast=str, default="")
DB_PASS = config("JWTS_DB_PASS", cast=str, default="")
DB_PORT = config("JWTS_DB_PORT", cast=str, default="")
DB_NAME = config("JWTS_DB_NAME", cast=str, default="")