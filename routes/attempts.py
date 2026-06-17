from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.exam import Exam
from models.attempt import Attempt
from models.result import Result
from models.question import Question

from schemas.attempt import (
    AttemptStart,
    AttemptSubmit
)

router = APIRouter(
    prefix="/attempts",
    tags=["Attempts"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/start")
def start_attempt(
    attempt: AttemptStart,
    db: Session = Depends(get_db)
):

    exam = db.query(Exam).filter(
        Exam.id == attempt.exam_id
    ).first()

    if not exam:

        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    if not exam.is_active:

        raise HTTPException(
            status_code=400,
            detail="Inactive exam cannot be attempted"
        )

    existing = db.query(Attempt).filter(
        Attempt.student_id == attempt.student_id,
        Attempt.exam_id == attempt.exam_id
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Student already attempted this exam"
        )

    new_attempt = Attempt(
        student_id=attempt.student_id,
        exam_id=attempt.exam_id,
        status="Started"
    )

    db.add(new_attempt)

    db.commit()

    db.refresh(new_attempt)

    return new_attempt


@router.post("/submit")
def submit_attempt(
    data: AttemptSubmit,
    db: Session = Depends(get_db)
):

    attempt = db.query(Attempt).filter(
        Attempt.id == data.attempt_id
    ).first()

    if not attempt:

        raise HTTPException(
            status_code=404,
            detail="Attempt not found"
        )

    if attempt.status == "Completed":

        raise HTTPException(
            status_code=400,
            detail="Attempt already submitted"
        )

    attempt.score = data.score

    attempt.status = "Completed"

    db.commit()

    existing_result = db.query(Result).filter(
        Result.attempt_id == attempt.id
    ).first()

    if existing_result:

        raise HTTPException(
            status_code=400,
            detail="Result already generated"
        )

    result = Result(
        attempt_id=attempt.id,
        score=data.score,
        rank=0
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return {
        "message": "Exam submitted successfully",
        "score": data.score
    }


@router.get("/{attempt_id}")
def get_attempt(
    attempt_id: int,
    db: Session = Depends(get_db)
):

    attempt = db.query(Attempt).filter(
        Attempt.id == attempt_id
    ).first()

    if not attempt:

        raise HTTPException(
            status_code=404,
            detail="Attempt not found"
        )

    return attempt


@router.get("/")
def get_attempts(
    status: str = None,
    db: Session = Depends(get_db)):

    query = db.query(Attempt)

    if status:

        query = query.filter(
            Attempt.status == status
        )

    return query.all()
