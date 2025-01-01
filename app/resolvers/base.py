import strawberry

from app.resolvers.contact import ContactMutations, ContactQuery


@strawberry.type
class Query:
    @strawberry.field()
    def contact(self) -> ContactQuery:
        return ContactQuery()


@strawberry.type
class Mutation:
    @strawberry.field()
    def contact(self) -> ContactMutations:
        return ContactMutations()


schema = strawberry.Schema(query=Query, mutation=Mutation)
