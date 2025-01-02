from uuid import uuid4

import pytest

from app.resolvers.base import schema
from app.schemas.contact import GetContactsType
from app.services.contact import ContactServices


@pytest.fixture
def mock_contact_services(mocker):
    service = mocker.Mock(spec=ContactServices)
    service.get_contacts_by_user.return_value = [
        GetContactsType(
            uuid=uuid4(),
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="1234567890"
        )
    ]
    return service


@pytest.fixture
def mock_context(mock_contact_services):
    return {
        "contact_services": mock_contact_services
    }


async def execute_graphql_operation(operation, context):
    result = await schema.execute(
        operation,
        context_value=context
    )
    return result


@pytest.mark.asyncio
async def test_get_contacts_query(mock_context):
    query = """
        query {
            contact {
                getContactsByUser {
                    uuid
                    firstName
                    lastName
                    email
                    phone
                }
            }
        }
    """
    result = await execute_graphql_operation(query, mock_context)
    assert result.errors is None
    assert len(result.data["contact"]["getContactsByUser"]) == 1
    contact = result.data["contact"]["getContactsByUser"][0]
    assert contact["firstName"] == "John"
    assert contact["lastName"] == "Doe"
    assert contact["email"] == "john@example.com"
    assert contact["phone"] == "1234567890"


# @pytest.mark.asyncio
# async def test_create_contact_mutation(mock_context):
#     mutation = """
#         mutation {
#             createContact(input: {
#                 firstName: "Jane",
#                 lastName: "Doe",
#                 email: "jane@example.com",
#                 phone: "0987654321"
#             }) {
#                 uuid
#                 firstName
#                 lastName
#                 email
#                 phone
#             }
#         }
#     """
#     result = await execute_graphql_operation(mutation, mock_context)
#     assert result.errors is None
#     contact = result.data["createContact"]
#     assert contact["firstName"] == "Jane"
#     assert contact["lastName"] == "Doe"
#     assert contact["email"] == "jane@example.com"
#     assert contact["phone"] == "0987654321"