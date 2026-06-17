CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE exams(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    category VARCHAR(100),
    duration INTEGER,
    is_active BOOLEAN
);

CREATE TABLE questions(
    id INTEGER PRIMARY KEY,
    exam_id INTEGER,
    question_text TEXT,
    option_a VARCHAR(255),
    option_b VARCHAR(255),
    option_c VARCHAR(255),
    option_d VARCHAR(255),
    correct_answer VARCHAR(255)
);

CREATE TABLE attempts(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    exam_id INTEGER,
    score INTEGER,
    status VARCHAR(50)
);

CREATE TABLE results(
    id INTEGER PRIMARY KEY,
    attempt_id INTEGER UNIQUE,
    score INTEGER,
    rank INTEGER
);
