from sqlalchemy import UUID, String, TIMESTAMP
from datetime import datetime

from app.models.contact import contact


def test_contact_table_name():
    assert contact.name == 'contact'


def test_contact_columns():
    columns = contact.columns

    # Test column existence
    expected_columns = {
        'uuid', 'first_name', 'last_name', 'email', 'phone',
        'created_at', 'updated_at', 'deleted_at',
        'created_by', 'updated_by', 'deleted_by'
    }
    assert set(columns.keys()) == expected_columns


def test_column_types():
    # Test column types
    assert isinstance(contact.c.uuid.type, UUID)
    assert isinstance(contact.c.first_name.type, String)
    assert isinstance(contact.c.last_name.type, String)
    assert isinstance(contact.c.email.type, String)
    assert isinstance(contact.c.phone.type, String)
    assert isinstance(contact.c.created_at.type, TIMESTAMP)
    assert isinstance(contact.c.updated_at.type, TIMESTAMP)
    assert isinstance(contact.c.deleted_at.type, TIMESTAMP)


def test_column_properties():
    # Test primary key
    assert contact.c.uuid.primary_key

    # Test nullable properties
    assert not contact.c.phone.nullable  # phone is not nullable
    assert contact.c.deleted_at.nullable  # deleted_at is nullable

    # Test string lengths
    assert contact.c.first_name.type.length == 50
    assert contact.c.last_name.type.length == 50
    assert contact.c.email.type.length == 100
    assert contact.c.phone.type.length == 15
    assert contact.c.created_by.type.length == 255
    assert contact.c.updated_by.type.length == 255
    assert contact.c.deleted_by.type.length == 255


def test_timestamp_properties():
    # Test timestamp timezone settings
    assert contact.c.created_at.type.timezone
    assert contact.c.updated_at.type.timezone
    assert contact.c.deleted_at.type.timezone

    # Test default values
    assert contact.c.created_at.default is not None
    assert contact.c.updated_at.onupdate is not None
