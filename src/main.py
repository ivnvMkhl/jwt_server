from uvicorn import run
from fastapi import Depends, FastAPI

from config import PORT, HOST

from auth.router import router as auth_router
from auth.models import User
from auth.auth import current_active_user

from devices.router import router as devices_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(
    devices_router,     
    prefix="/device",
    tags=["Devices"],
    )

@auth_router.get("/")
async def authenticated_route():
    return {"message": f"Hello!"}
    
@auth_router.get("/auth")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

if __name__ == "__main__":
    run('main:app', port=PORT, reload=True, host=HOST)
