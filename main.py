from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import (
    Base,
    engine
)

from models.user import User
from models.student import Student
from models.exam import Exam
from models.question import Question
from models.attempt import Attempt
from models.result import Result

from routes.auth import router as auth_router
from routes.students import router as student_router
from routes.exams import router as exam_router
from routes.questions import router as question_router
from routes.attempts import router as attempt_router
from routes.results import router as result_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Online Examination Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(student_router)
app.include_router(exam_router)
app.include_router(question_router)
app.include_router(attempt_router)
app.include_router(result_router)


@app.get("/")
def home():

    return {
        "message":
        "Online Examination Management System"
    }
