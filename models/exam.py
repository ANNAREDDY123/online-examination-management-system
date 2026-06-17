from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database import Base


class Exam(Base):
    __tablename__ = "exams"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    category = Column(String)

    duration = Column(Integer)

    is_active = Column(
        Boolean,
        default=True
    )
