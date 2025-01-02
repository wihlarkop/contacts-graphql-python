import os
import signal

import uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import ResponseValidationError
from strawberry.fastapi import GraphQLRouter

from app.config import settings
from app.dependencies.context import context_getter
from app.resolvers.base import schema
from app.exceptions.base import create_exception_handler, InternalServerError
from app.exceptions.token import TokenExpired, TokenInvalid
from app.exceptions.user import UserAlreadyExists

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=None,
    redoc_url=None
)

graphql_app = GraphQLRouter(schema=schema, graphql_ide="apollo-sandbox", context_getter=context_getter)
app.include_router(graphql_app, prefix="/graphql")

# for add new custom exception handler
app.add_exception_handler(
    exc_class_or_status_code=ResponseValidationError,
    handler=create_exception_handler(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
)
app.add_exception_handler(
    exc_class_or_status_code=InternalServerError,
    handler=create_exception_handler(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="something went wrong")
)
app.add_exception_handler(
    exc_class_or_status_code=UserAlreadyExists,
    handler=create_exception_handler(status_code=status.HTTP_409_CONFLICT)
)
app.add_exception_handler(
    exc_class_or_status_code=TokenExpired,
    handler=create_exception_handler(status_code=status.HTTP_401_UNAUTHORIZED,
                                     message="Refresh token expired, login required.")
)
app.add_exception_handler(
    exc_class_or_status_code=TokenInvalid,
    handler=create_exception_handler(status_code=status.HTTP_403_FORBIDDEN, message="Invalid refresh token.")
)

if __name__ == "__main__":
    try:
        uvicorn.run(app="main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
    except KeyboardInterrupt:
        pass
    finally:
        os.kill(os.getpid(), signal.SIGINT)
