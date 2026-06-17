from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id"),
        unique=True
    )

    score = Column(Integer)

    rank = Column(Integer)
