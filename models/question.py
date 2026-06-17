from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id")
    )

    question_text = Column(String)

    option_a = Column(String)

    option_b = Column(String)

    option_c = Column(String)

    option_d = Column(String)

    correct_answer = Column(String)
