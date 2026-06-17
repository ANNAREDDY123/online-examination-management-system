from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.student import Student
from models.attempt import Attempt

from schemas.student import StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student


@router.get("/{student_id}/exams")
def get_student_exams(
    student_id: int,
    db: Session = Depends(get_db)
):

    exams = db.query(Attempt).filter(
        Attempt.student_id == student_id
    ).all()

    return exams
