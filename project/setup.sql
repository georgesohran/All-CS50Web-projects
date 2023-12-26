CREATE TABLE teachers
(
    id PRIMARY KEY AUTOINCREMENT,
    name,
    subject_id
)

CREATE TABLE students
(
    id,
    name
)

CREATE TABLE subjects
(
    id,
    name
)

CREATE TABLE students_grades
(
    student_id,
    subject_id,
    time,
    grade
)
