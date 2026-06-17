from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id")
    )

    score = Column(
        Integer,
        default=0
    )

    status = Column(String)
