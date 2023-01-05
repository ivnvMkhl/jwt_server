from uvicorn import run
from fastapi import Depends, FastAPI

from config import PORT, HOST

from auth.router import router
from auth.models import User
from auth.auth import current_active_user

app = FastAPI()

app.include_router(router)

@router.get("/")
async def authenticated_route():
    return {"message": f"Hello!"}
    
@router.get("/auth")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

if __name__ == "__main__":
    run('main:app', port=PORT, reload=True, host=HOST)
