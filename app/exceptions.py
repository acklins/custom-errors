#Define custom exception classes and the handler functions
# that convert them into consistent JSON responses.

from fastapi import Request
from fastapi.responses import JSONResponse

#Raised when a requested resource does not exist.
class NotFoundError(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

#Raised when creating a resource would violate a uniqueness constraint.
class DuplicateError(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

#Raised for domain-level validation failures (beyond Pydantic schema checks).
class AppValidationError(Exception):
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

#Handles NotFoundError → 404 response.
async def not_found_handler(
    request: Request,
    exc: NotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "NotFoundError",
            "message": exc.message,
            "status_code": 404
        }
    )
#Handles DuplicateError → 409 response.

async def duplicate_handler(
    request: Request,
    exc: DuplicateError
):
    return JSONResponse(
        status_code=409,
        content={
            "error": "DuplicateError",
            "message": exc.message,
            "status_code": 409
        }
    )
#Handles AppValidationError → 422 response.
async def app_validation_handler(
    request: Request,
    exc: AppValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "AppValidationError",
            "message": exc.message,
            "status_code": 422
        }
    )
