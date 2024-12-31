from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncConnection
from typing_extensions import Annotated

from app.dependencies.database import get_connection
from app.repositories.contact import ContactRepositories
from app.services.contact import ContactServices


async def context_getter(connection: Annotated[AsyncConnection, Depends(get_connection)]):
    contact_repo = ContactRepositories(connection=connection)
    contact_services = ContactServices(contact_repo=contact_repo)

    yield {
        "contact_services": contact_services
    }
