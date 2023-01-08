from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP
from httpx import get

from database import Base


class Device(Base):
    def __init__(self, device_name: str, device_type: str, device_ip: str ):
        self.device_name = device_name
        self.device_type = device_type
        self.device_ip = device_ip

    __tablename__ = "device"
    id = Column(Integer, primary_key=True)
    device_name = Column(String(length=128), nullable=False)
    device_ip = Column(String(length=128), nullable=False)
    device_type = Column(String(length=128), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    def _device_request( URL: str ):
        try:
            result = get(URL)
            if (result.status_code >= 200 and result.status_code <= 300):
                return { "status": "success", "message": result.text }
            return { "status": f"fetch error {result.status_code}", "message": result.text }
        except Exception as error:
            return { "status": f"fetch error", "message": error.args }

    def on(self):
        device_on_url = f"{self.device_ip}/on"
        return self._device_request(device_on_url)

    def off(self):
        device_off_url = f"{self.device_ip}/off"
        return self._device_request(device_off_url)



