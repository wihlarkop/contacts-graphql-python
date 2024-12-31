"""generate table contact

Revision ID: eec05df79535
Revises:
Create Date: 2024-12-18 01:00:08.375520

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.database.client import metadata

# revision identifiers, used by Alembic.
revision: str = 'eec05df79535'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "contact",
    metadata,
    sa.Column(name="uuid", type_=sa.UUID, primary_key=True),
    sa.Column(name="first_name", type_=sa.String(50)),
    sa.Column(name="last_name", type_=sa.String(50)),
    sa.Column(name="email", type_=sa.String(100), ),
    sa.Column(name="phone", type_=sa.String(15), nullable=False),
    sa.Column(name="created_at", type_=sa.TIMESTAMP(timezone=True), default=datetime.now()),
    sa.Column(name="updated_at", type_=sa.TIMESTAMP(timezone=True), onupdate=datetime.now()),
    sa.Column(name="deleted_at", type_=sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column(name="created_by", type_=sa.String(length=255)),
    sa.Column(name="updated_by", type_=sa.String(length=255)),
    sa.Column(name="deleted_by", type_=sa.String(length=255)),
)


def downgrade() -> None:
    op.drop_table("contact")
