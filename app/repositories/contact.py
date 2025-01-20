from sqlalchemy import and_, insert, select, update
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.operators import eq
from strawberry.schema.types.base_scalars import UUID

from app.entities.contact import ContactEntities
from app.exceptions.base import InternalServerError
from app.helper.generator import generate_time_now
from app.models.contact import contact
from app.repositories.interface import ContactInterface


class ContactRepositories(ContactInterface):
    def __init__(self, connection: AsyncConnection):
        self.connection = connection

    async def get_contacts_by_user(self):
        stmt = select(
            contact.c.uuid,
            contact.c.first_name,
            contact.c.last_name,
            contact.c.email,
            contact.c.phone,
        ).where(
            # and_(
                contact.c.deleted_at.is_(None),
                # eq(contact.c.created_by,)
            # )
        )

        result = await self.connection.execute(stmt)
        return result.mappings().fetchall()

    async def create_contact(self, payload: ContactEntities):
        stmt = insert(contact).values(
            payload.model_dump()
        )
        try:
            await self.connection.execute(statement=stmt)
            await self.connection.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def update_contact(self, payload: ContactEntities):
        stmt = update(contact).where(
            eq(contact.c.uuid, payload.uuid)
        ).values(
            payload.model_dump(exclude_none=True)
        )

        try:
            await self.connection.execute(statement=stmt)
            await self.connection.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))

    async def delete_contact(self, contact_uuid: UUID):
        stmt = update(contact).where(
            eq(contact.c.uuid, contact_uuid)
        ).values(
            deleted_at=generate_time_now()
        )

        try:
            await self.connection.execute(statement=stmt)
            await self.connection.commit()
        except Exception as e:
            raise InternalServerError(message=str(e))
