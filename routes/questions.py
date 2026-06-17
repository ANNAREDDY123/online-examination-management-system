from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.exam import Exam
from models.question import Question

from schemas.question import QuestionCreate

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):

    exam = db.query(Exam).filter(
        Exam.id == question.exam_id
    ).first()

    if not exam:

        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    new_question = Question(
        exam_id=question.exam_id,
        question_text=question.question_text,
        option_a=question.option_a,
        option_b=question.option_b,
        option_c=question.option_c,
        option_d=question.option_d,
        correct_answer=question.correct_answer
    )

    db.add(new_question)

    db.commit()

    db.refresh(new_question)

    return new_question


@router.get("/exam/{exam_id}")
def get_exam_questions(
    exam_id: int,
    db: Session = Depends(get_db)
):

    questions = db.query(Question).filter(
        Question.exam_id == exam_id
    ).all()

    return questions


@router.get("/exam/{exam_id}/validate")
def validate_exam_questions(
    exam_id: int,
    db: Session = Depends(get_db)
):

    count = db.query(Question).filter(
        Question.exam_id == exam_id
    ).count()

    return {
        "exam_id": exam_id,
        "question_count": count,
        "minimum_required": 5,
        "valid_exam": count >= 5
    }
