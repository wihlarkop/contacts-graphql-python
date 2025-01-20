import pytest
from sqlalchemy.ext.asyncio import AsyncConnection

from app.dependencies.context import context_getter
from app.services.contact import ContactServices


@pytest.mark.asyncio
async def test_context_getter_alternative(mocker):
    mock_connection = mocker.MagicMock(spec=AsyncConnection)

    context_generator = context_getter(connection=mock_connection)

    context = await anext(context_generator)

    assert "contact_services" in context
    assert isinstance(context["contact_services"], ContactServices)