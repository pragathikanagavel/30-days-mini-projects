-- Create students table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT,
    marks INTEGER CHECK(marks BETWEEN 0 AND 100)
);

-- Insert sample records
INSERT INTO students (id, name, department, marks) VALUES
(1, 'Pragathi', 'CSE', 87),
(2, 'Arun', 'ECE', 72),
(3, 'Divya', 'IT', 91),
(4, 'Karthik', 'EEE', 65),
(5, 'Meena', 'CSE', 48);

-- Query: show all students
SELECT * FROM students;

-- Query: students with marks >= 75
SELECT name, department, marks
FROM students
WHERE marks >= 75;

-- Query: students who failed
SELECT name, marks
FROM students
WHERE marks < 50;
