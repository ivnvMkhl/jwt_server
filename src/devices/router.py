from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import get

from database import get_async_session
from devices.schemas import DeviceCreate
from devices.models import Device
from devices.service import add_devices, all_devices_info, device_by_id

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
    device_list = await all_devices_info(session)
    return {
        "status": "success", 
        "user": user.username,
        "device_list": device_list
        }

@router.get('/on')
async def device_on(
    id: int,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session) 
    ):
    device = await device_by_id(id, session)
    if isinstance(device, Device): 
        return { "user": user.username, **device.on() }
    return { "user": user.username, **device }

@router.get('/off')
async def device_off(
    id: int,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session) 
    ):
    device = await device_by_id(id, session)
    if isinstance(device, Device): 
        return { "user": user.username, **device.off() }
    return { "user": user.username, **device }
    