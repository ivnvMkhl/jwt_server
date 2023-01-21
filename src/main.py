from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import PORT, HOST

from auth.router import router as auth_router
from auth.models import User
from auth.auth import current_active_user

from devices.router import router as devices_router


app = FastAPI()

origins = ["http://localhost:3002"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(
    devices_router,     
    prefix="/device",
    tags=["Devices"],
    )

if __name__ == "__main__":
    run('main:app', port=PORT, reload=True, host=HOST)
