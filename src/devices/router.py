from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from devices.schemas import DeviceCreate
from database import get_async_session
from devices.models import Device

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_device(
  new_device: DeviceCreate, 
  session: AsyncSession = Depends(get_async_session)
  ):
  stmt = insert(Device).values(**new_device.dict())
  await session.execute(stmt)
  await session.commit()
  return { "status": "success" }