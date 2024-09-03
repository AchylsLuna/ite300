CREATE DATABASE school;

USE school;

CREATE TABLE course (
id INT PRIMARY KEY AUTO_INCREMENT,
CourseID INT,
CourseName VARCHAR(50),
Instructor VARCHAR(50),
Credits INT,
);

INSERT INTO course = (CourseID, CourseName, Instructor, Credits) VALUES (1, 'Math', 'Jose', 4);