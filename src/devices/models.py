from datetime import datetime

from sqlalchemy import Column, String, Integer, TIMESTAMP

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


