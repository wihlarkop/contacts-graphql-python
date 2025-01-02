from datetime import datetime

from app.entities.base import AuditBaseModel


def test_audit_base_model_custom_value():
    model = AuditBaseModel(
        created_at=datetime(2023, 1, 1),
        updated_at=datetime(2023, 1, 2),
        deleted_at=datetime(2023, 1, 3),
        created_by="user1",
        updated_by="user2",
        deleted_by="user3"
    )
    assert model.created_at == datetime(2023, 1, 1)
    assert model.updated_at == datetime(2023, 1, 2)
    assert model.deleted_at == datetime(2023, 1, 3)
    assert model.created_by == "user1"
    assert model.updated_by == "user2"
    assert model.deleted_by == "user3"

def test_audit_base_model_default_value():
    model = AuditBaseModel()
    assert model.created_at is None
    assert model.updated_at is None
    assert model.deleted_at is None
    assert model.created_by is None
    assert model.updated_by is None
    assert model.deleted_by is None
