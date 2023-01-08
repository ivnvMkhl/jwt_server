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

async def get_all_devices( session: AsyncSession ):
    query = select(Device)
    result: ChunkedIteratorResult = await session.execute(query)
    rows_list: List[Device] = result.scalars()
    return [i.__dict__ for i in rows_list]