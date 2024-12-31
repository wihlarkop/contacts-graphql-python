from typing import Protocol

from strawberry.schema.types.base_scalars import UUID

from app.entities.contact import ContactEntities


class ContactInterface(Protocol):

    async def create_contact(self, payload: ContactEntities): ...

    async def get_contacts_by_user(self): ...

    async def update_contact(self, payload: ContactEntities): ...

    async def delete_contact(self, contact_uuid: UUID): ...


class UserInterface(Protocol):
    pass
