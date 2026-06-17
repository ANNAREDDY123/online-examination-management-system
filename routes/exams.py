from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.exam import Exam

from schemas.exam import ExamCreate

router = APIRouter(
    prefix="/exams",
    tags=["Exams"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_exam(
    exam: ExamCreate,
    db: Session = Depends(get_db)
):

    new_exam = Exam(
        title=exam.title,
        category=exam.category,
        duration=exam.duration,
        is_active=exam.is_active
    )

    db.add(new_exam)

    db.commit()

    db.refresh(new_exam)

    return new_exam


@router.get("/")
def get_exams(
    category: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Exam)

    if category:

        query = query.filter(
            Exam.category == category
        )

    total_records = query.count()

    exams = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total_records,
        "current_page": page,
        "data": exams
    }
