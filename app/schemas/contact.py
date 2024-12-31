import strawberry
from strawberry.schema.types.base_scalars import UUID

from app.entities.contact import ContactEntities
from app.helper.generator import generate_time_now, generate_uuid


@strawberry.type
class GetContactsType:
    uuid: UUID
    first_name: str | None
    last_name: str | None
    email: str
    phone: str


@strawberry.input
class CreateContactType:
    first_name: str | None
    last_name: str | None
    email: str
    phone: str

    def transform(self):
        return ContactEntities(
            uuid=generate_uuid(),
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            created_at=generate_time_now()
        )

@strawberry.input
class UpdateContactType:
    uuid: UUID
    first_name: str | None
    last_name: str | None
    email: str
    phone: str

    def transform(self):
        return ContactEntities(
            uuid=self.uuid,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            updated_at=generate_time_now()
        )