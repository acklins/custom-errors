# Custom Errors

**Module:** 5 — FastAPI Development
**Estimated time:** 35 minutes

## Objective

Replace ad-hoc `HTTPException` usage with custom exception classes and centralized error handlers that return consistent JSON error responses.

## What You'll Do

1. In `app/exceptions.py`:
   - Implement three custom exception classes (`NotFoundError`, `DuplicateError`, `AppValidationError`), each storing a detail message.
   - Implement three async handler functions that convert each exception into a `JSONResponse` with a consistent format: `{"error": "...", "message": "...", "status_code": ...}`.
2. In `app/routers/students.py`, implement the student endpoints using the custom exceptions instead of `HTTPException`:
   - `POST /` — raise `DuplicateError` when email is already taken.
   - `GET /{student_id}` — raise `NotFoundError` when student is missing.
   - `DELETE /{student_id}` — raise `NotFoundError` when student is missing.
3. In `app/main.py`, register each exception handler with `app.add_exception_handler()` and include the students router.

## Starter Code

```
app/
  __init__.py
  main.py              — FastAPI app; needs handler registration and router inclusion
  database.py          — Database setup (pre-configured)
  exceptions.py        — Exception class and handler stubs
  models/
    __init__.py
    student.py         — Student ORM model (pre-configured)
  schemas/
    __init__.py
    student.py         — Pydantic schemas (pre-configured)
  routers/
    __init__.py
    students.py        — Endpoint stubs using custom exceptions
```

The database, model, and schemas are already complete. Focus on the exceptions and endpoint logic.

## Running

```bash
uvicorn app.main:app --reload
```

## Deliverable

An API where all error responses follow a uniform JSON structure, and domain errors like "not found" or "duplicate" are raised as plain Python exceptions rather than FastAPI-specific HTTPExceptions.
