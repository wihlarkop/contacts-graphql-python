from datetime import datetime

from sqlalchemy import String, Table, Column, TIMESTAMP, UUID

from app.database.client import metadata

user = Table(
    "user",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="email", type_=String(length=255), unique=True, nullable=False),
    Column(name="password", type_=String(length=255), nullable=False),
    Column(name="created_at", type_=TIMESTAMP(), default=datetime.now()),
    Column(name="updated_at", type_=TIMESTAMP(), onupdate=datetime.now()),
    Column(name="deleted_at", type_=TIMESTAMP(), nullable=True),
    Column(name="created_by", type_=String(length=255)),
    Column(name="updated_by", type_=String(length=255)),
    Column(name="deleted_by", type_=String(length=255)),
)
