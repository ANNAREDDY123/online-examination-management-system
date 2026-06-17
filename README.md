# online-examination-management-system
Online Examination Management System built with FastAPI, SQLAlchemy, SQLite, JWT Authentication, Role-Based Access Control, Exam Attempts, Results, Rankings, Pagination, Background Tasks, Docker, and Clean Architecture.
# Online Examination Management System

## Overview

A FastAPI-based backend application for managing students, exams, questions, attempts, results, and rankings.

## Features

- JWT Authentication
- Student Management
- Exam Management
- Question Management
- Exam Attempts
- Results & Rankings
- Pagination
- Filtering
- SQLAlchemy ORM
- SQLite Database
- Swagger Documentation
- CORS Support

## APIs

### Authentication

- POST /auth/register
- POST /auth/login

### Students

- POST /students
- GET /students/{student_id}/exams

### Exams

- POST /exams
- GET /exams

### Questions

- POST /questions
- GET /questions/exam/{exam_id}

### Attempts

- POST /attempts/start
- POST /attempts/submit
- GET /attempts/{id}

### Results

- GET /results
- GET /results/leaderboard

## Run Project

pip install -r requirements.txt

uvicorn main:app --reload

## Swagger

http://127.0.0.1:8000/docs
