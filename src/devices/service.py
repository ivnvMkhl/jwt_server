from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.result import  ChunkedIteratorResult

from devices.schemas import DeviceCreate
from devices.models import Device


async def add_devices(
    new_devices: List[DeviceCreate], 
    session: AsyncSession
    ):
    for new_device in new_devices:
        added_device = Device(**new_device.dict())
        session.add(added_device)
    await session.commit()

async def all_devices_info( session: AsyncSession ):
    query = select(Device)
    try:
        result: ChunkedIteratorResult = await session.execute(query)
        rows_list: List[Device] = result.scalars()
        return (i.__dict__ for i in rows_list)
    except Exception as error:
        return {"status": "error", "message": error.args}
        
async def device_by_id( id: int, session: AsyncSession ):
    query = select(Device).filter(Device.id == id)
    try:
        result: ChunkedIteratorResult = await session.execute(query)
        rows_list: List[Device] = result.one()
        return rows_list[0]
    except Exception as error:
        return {"status": "error", "message": error.args}
    

