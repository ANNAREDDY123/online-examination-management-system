from pydantic import (
    BaseModel
)


class ResultResponse(
    BaseModel
):

    id: int

    attempt_id: int

    score: int

    rank: int

    class Config:
        from_attributes = True
