import pytest
from sqlalchemy.ext.asyncio import AsyncEngine

from app.dependencies.database import get_connection


class MockAsyncConnection:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass


@pytest.mark.asyncio
async def test_get_connection(mocker):
    mock_connect = mocker.patch.object(AsyncEngine, "connect", return_value=MockAsyncConnection())

    connection_gen = get_connection()
    connection = await connection_gen.__anext__()

    mock_connect.assert_called_once()
    assert isinstance(connection, MockAsyncConnection)

    # Cleanup generator
    with pytest.raises(StopAsyncIteration):
        await connection_gen.__anext__()
