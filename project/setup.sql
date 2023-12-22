CREATE TABLE students
(
    id INTEGER NOT NULL AUTO_INCREMENT=100,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE teachers
(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE subjects
(

);

CREATE TABLE students_grades
(

);

