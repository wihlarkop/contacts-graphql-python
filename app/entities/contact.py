from uuid import UUID

from app.entities.base import AuditBaseModel


class ContactEntities(AuditBaseModel):
    uuid: UUID
    first_name: str | None
    last_name: str | None
    email: str
    phone: str