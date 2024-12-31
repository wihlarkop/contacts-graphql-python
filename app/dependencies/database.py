from sqlalchemy.ext.asyncio import AsyncConnection

from app.database.client import engine


async def get_connection() -> AsyncConnection:
    async with engine.connect() as connection:
        yield connection
