from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from devices.schemas import DeviceCreate
from devices.service import add_devices, get_all_devices

from auth.models import User
from auth.auth import current_active_user

router = APIRouter()

@router.post('/create')
async def create_devices(
    new_devices: List[DeviceCreate], 
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
    ):
    await add_devices(new_devices, session)
    return { 
        "status": "success", 
        "user": user.username,
        "message": f"Created {len(new_devices)} devices" 
        }

@router.get('/list')
async def get_devices_list( 
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session) 
    ):
    device_list = await get_all_devices(session)
    return {
        "status": "success", 
        "user": user.username,
        "device_list": device_list
        }