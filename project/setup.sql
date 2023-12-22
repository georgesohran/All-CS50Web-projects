CREATE TABLE students
(
    id INTEGER PRIMARY KEY  AUTOINCREMENT=200 NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,

);

CREATE TABLE teachers
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE subjects
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
);

CREATE TABLE students_grades
(
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

