from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.result import Result
from models.attempt import Attempt

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/")
def get_results(
    student_id: int = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Result)

    if student_id:

        query = query.join(
            Attempt,
            Result.attempt_id == Attempt.id
        ).filter(
            Attempt.student_id == student_id
        )

    total_records = query.count()

    results = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total_records,
        "current_page": page,
        "data": results
    }


@router.get("/leaderboard")
def leaderboard(
    db: Session = Depends(get_db)
):

    results = db.query(Result).order_by(
        Result.score.desc()
    ).all()

    rank = 1

    leaderboard_data = []

    for result in results:

        result.rank = rank

        leaderboard_data.append(
            {
                "rank": rank,
                "attempt_id": result.attempt_id,
                "score": result.score
            }
        )

        rank += 1

    db.commit()

    return leaderboard_data
