CREATE DATABASE student_analysis;

USE student_analysis;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    maths INT,
    science INT,
    english INT,
    interest VARCHAR(50),
    career VARCHAR(100)
);
ALTER TABLE students
ADD COLUMN name VARCHAR(100);

SELECT * FROM students;

ALTER TABLE students ADD computer INT;
ALTER TABLE students ADD economics INT;
ALTER TABLE students ADD creativity INT;
ALTER TABLE students ADD communication INT;