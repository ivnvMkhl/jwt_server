from sqlalchemy import Table, Column, MetaData, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

metadata = MetaData()

users = Table(
  "users", metadata, 
  Column("id", Integer, primary_key=True),
  Column("email", String, nullable=False),
  Column("username", String, nullable=False),
  Column("password", String, nullable=False),
  Column("registered_at", TIMESTAMP, default=datetime.utcnow),
)