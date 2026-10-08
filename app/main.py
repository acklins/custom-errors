# Custom Error Handling
from fastapi import FastAPI
from app.database import Base, engine

from app.exceptions import( 
    NotFoundError, 
    DuplicateError, 
    AppValidationError,
    not_found_handler,
    duplicate_handler, 
    app_validation_handler,
)
from app.routers import students

app = FastAPI(title="Custom Errors API")

Base.metadata.create_all(bind=engine)

#Register the exception handlers on the app
app.add_exception_handler(
    NotFoundError, 
    not_found_handler
)
app.add_exception_handler(
    DuplicateError, 
    duplicate_handler
)
app.add_exception_handler(
    AppValidationError, 
    app_validation_handler
)
#Include the students router
app.include_router(
    students.router,
    prefix="/students",
    tags=["students"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
    )
