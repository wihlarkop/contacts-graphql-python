from strawberry.schema.types.base_scalars import UUID

from app.repositories.interface import ContactInterface
from app.schemas.contact import CreateContactType, GetContactsType, UpdateContactType


class ContactServices:
    def __init__(self, contact_repo: ContactInterface):
        self.__contact_repo = contact_repo

    async def create_contact(self, payload: CreateContactType) -> None:
        await self.__contact_repo.create_contact(payload=payload.transform())
        return

    async def get_contacts_by_user(self) -> list[GetContactsType]:
        contacts = await self.__contact_repo.get_contacts_by_user()
        return [GetContactsType(**contact) for contact in contacts]

    async def update_contact(self, payload: UpdateContactType) -> None:
        await self.__contact_repo.update_contact(payload=payload.transform())
        return

    async def delete_contact(self, contact_uuid: UUID) -> None:
        await self.__contact_repo.delete_contact(contact_uuid=contact_uuid)
        return