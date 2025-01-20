import strawberry
from app.resolvers.base import schema, Query, Mutation
from app.resolvers.contact import ContactMutations, ContactQuery


def test_query_contact():
    query = Query()
    assert isinstance(query.contact(), ContactQuery)

def test_mutation_contact():
    mutation = Mutation()
    assert isinstance(mutation.contact(), ContactMutations)

def test_schema():
    assert isinstance(schema, strawberry.Schema)
    assert schema.query == Query
    assert schema.mutation == Mutation