from pydantic import (
    BaseModel
)


class AttemptStart(BaseModel):

    student_id: int

    exam_id: int


class AttemptSubmit(BaseModel):

    attempt_id: int

    score: int
