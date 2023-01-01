from config import DB_USER, DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

