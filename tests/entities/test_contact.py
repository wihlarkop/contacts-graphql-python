from uuid import UUID

from app.entities.contact import ContactEntities


def test_contact_entities_default_value():
    contact = ContactEntities(
        uuid=UUID("6afda23f-7527-45e7-831a-819cda0a0f69"),
        first_name=None,
        last_name=None,
        email="www@www.www",
        phone="628812812812"
    )

    assert isinstance(contact.uuid, UUID)
    assert contact.first_name is None
    assert contact.last_name is None
    assert contact.email == "www@www.www"
    assert contact.phone == "628812812812"


def test_contact_entities_custom_value():
    contact = ContactEntities(
        uuid=UUID("6afda23f-7527-45e7-831a-819cda0a0f69"),
        first_name="John",
        last_name="Doe",
        email="www@www.www",
        phone="628812812812"
    )

    assert isinstance(contact.uuid, UUID)
    assert contact.first_name == "John"
    assert contact.last_name == "Doe"
    assert contact.email == "www@www.www"
    assert contact.phone == "628812812812"