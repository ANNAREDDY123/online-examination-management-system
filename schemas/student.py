from pydantic import (
    BaseModel,
    EmailStr
)


class StudentCreate(BaseModel):

    name: str

    email: EmailStr


class StudentResponse(
    StudentCreate
):

    id: int

    class Config:
        from_attributes = True
