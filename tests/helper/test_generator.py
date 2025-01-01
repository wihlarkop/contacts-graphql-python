from datetime import datetime
from uuid import UUID

from freezegun import freeze_time
from sqlalchemy import URL

from app.helper.generator import generate_time_now, generate_uuid, build_connection_url


def test_build_connection_url():
    result = build_connection_url(
        driver_name="postgresql",
        username="user",
        password="password",
        host="localhost",
        port="5432",
        database="test_db"
    )
    expected_url = URL.create(
        drivername="postgresql",
        username="user",
        password="password",
        host="localhost",
        port=5432,
        database="test_db"
    )
    assert result == expected_url

@freeze_time('2024-01-02 12:00:00')
def test_generate_time_now():
    result = generate_time_now()
    assert result == datetime(2024, 1, 2, 12, 0)


def test_generate_uuid():
    result = generate_uuid()
    assert isinstance(result, UUID)
