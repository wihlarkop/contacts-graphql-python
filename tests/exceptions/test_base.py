import pytest
from app.exceptions.base import InternalServerError


def test_internal_server_error():
    with pytest.raises(InternalServerError) as exc_info:
        raise InternalServerError("Test error message")

    assert str(exc_info.value) == "Test error message"
