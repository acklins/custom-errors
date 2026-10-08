from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.schemas.student import StudentCreate, StudentResponse
from app.models.student import Student
from app.database import get_db

from app.exceptions import NotFoundError, DuplicateError

router = APIRouter()

#Creates a student. Raises DuplicateError (not HTTPException) if email taken.
@router.post(
    "/", 
    response_model=StudentResponse, status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate, 
    db: Session = Depends(get_db)
):
    existing_student = db.scalar(
        select(Student).where(
            Student.email == student.email
        )
    )
    if existing_student:
        raise DuplicateError(
            f"Email {student.email} already registered"
        )
    new_student = Student(
        name=student.name,
        email=student.email,
        major=student.major,
        gpa=student.gpa
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

#Gets a student. Raises NotFoundError if not found.
@router.get(
    "/{student_id}", response_model=StudentResponse
)
def get_student(
    student_id: int, 
    db: Session = Depends(get_db)
):
    student = db.get(Student, student_id)

    if student is None:
        raise NotFoundError(
            f"Student {student_id} not found"
        )
    return student

#Deletes a student. Raises NotFoundError if not found.
@router.delete("/{student_id}")
def delete_student(
    student_id: int, 
    db: Session = Depends(get_db)
):
    student = db.get(Student, student_id)

    if student is None:
        raise NotFoundError(
            f"Student {student_id} not found"
        )
    db.delete(student)
    db.commit()

    return {
        "message": f"Student {student_id} deleted"
    }