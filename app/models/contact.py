from datetime import datetime

from sqlalchemy import Column, String, Table, TIMESTAMP, UUID

from app.database.client import metadata

contact = Table(
    "contact",
    metadata,
    Column(name="uuid", type_=UUID, primary_key=True),
    Column(name="first_name", type_=String(50)),
    Column(name="last_name", type_=String(50)),
    Column(name="email", type_=String(100)),
    Column(name="phone", type_=String(15), nullable=False),
    Column(name="created_at", type_=TIMESTAMP(timezone=True), default=datetime.now()),
    Column(name="updated_at", type_=TIMESTAMP(timezone=True), onupdate=datetime.now()),
    Column(name="deleted_at", type_=TIMESTAMP(timezone=True), nullable=True),
    Column(name="created_by", type_=String(length=255)),
    Column(name="updated_by", type_=String(length=255)),
    Column(name="deleted_by", type_=String(length=255)),
)
