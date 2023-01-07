from pydantic import BaseModel

class DeviceCreate(BaseModel):
    device_name: str
    device_ip: str
    device_type: str
