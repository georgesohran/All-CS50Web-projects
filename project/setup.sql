CREATE TABLE students
(
    id INTEGER AUTOINCREMENT=200 NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE teachers
(
    id INTEGER NOT AUTOINCREMENT  NULL,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE subjects
(
    id INTEGER NOT AUTOINCREMENT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
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

