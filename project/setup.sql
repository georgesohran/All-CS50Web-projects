CREATE TABLE teachers
(
    id INTEGER AUTOINCREMENT PRIMARY KEY,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    subject_id INTEGER FOREIGN KEY REFERENCES subjects(id)
);

CREATE TABLE students
(
    id INTEGER AUTOINCREMENT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE subjects
(
    id INTEGER AUTOINCREMENT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE students_grades
(
    student_id INTEGER FOREIGN KEY REFERENCES students(id),
    subject_id INTEGER FOREIGN KEY REFERENCES subjects(id),
    time TEXT NOT NULL,
    grade INTEGER NOT NULL
);
