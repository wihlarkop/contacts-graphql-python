import pytest
from sqlalchemy.ext.asyncio import AsyncEngine
from app.database.client import DatabaseClient
from app.helper.generator import build_connection_url
from app.config import settings

@pytest.fixture
def database_client():
    connection_url = build_connection_url(
        driver_name="postgresql+psycopg",
        username=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database=settings.POSTGRES_DB
    )
    return DatabaseClient(database_connection_url=connection_url)

def test_create_engine(database_client):
    engine = database_client.create_engine()
    assert isinstance(engine, AsyncEngine)
    assert str(engine.url) == str(database_client.connection_url)