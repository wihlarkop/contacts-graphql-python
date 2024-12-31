import strawberry
from strawberry.schema.types.base_scalars import UUID

from app.schemas.contact import CreateContactType, GetContactsType, UpdateContactType
from app.services.contact import ContactServices


@strawberry.type
class ContactQuery:
    @strawberry.field()
    async def get_contacts_by_user(self, info: strawberry.Info) -> list[GetContactsType]:
        contact_services: ContactServices = info.context['contact_services']
        data = await contact_services.get_contacts_by_user()
        return data


@strawberry.type
class ContactMutations:
    @strawberry.mutation()
    async def create_contact(self, info: strawberry.Info, payload: CreateContactType) -> None:
        contact_services: ContactServices = info.context['contact_services']
        await contact_services.create_contact(payload=payload)
        return

    @strawberry.mutation()
    async def update_contact(self, info: strawberry.Info, payload: UpdateContactType) -> None:
        contact_services: ContactServices = info.context['contact_services']
        await contact_services.update_contact(payload=payload)
        return

    @strawberry.mutation()
    async def delete_contact(self, info: strawberry.Info, contact_uuid: UUID) -> None:
        contact_services: ContactServices = info.context['contact_services']
        await contact_services.delete_contact(contact_uuid=contact_uuid)
        return
