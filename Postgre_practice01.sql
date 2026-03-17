CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    marks INT
);

INSERT INTO students (id, name, age, city, marks) VALUES
(1, 'Aman', 20, 'Lucknow', 85),
(2, 'Riya', 19, 'Delhi', 90),
(3, 'Karan', 21, 'Mumbai', 78),
(4, 'Sneha', 18, 'Lucknow', 88),
(5, 'Arjun', 22, 'Delhi', 67),
(6, 'Priya', 20, 'Mumbai', 92),
(7, 'Rahul', 23, 'Lucknow', 55),
(8, 'Neha', 19, 'Delhi', 73),
(9, 'Vikas', 21, 'Mumbai', 81),
(10, 'Anjali', 20, 'Lucknow', 95),
(11, 'Rohit', 22, 'Delhi', 60),
(12, 'Pooja', 18, 'Mumbai', 77),
(13, 'Deepak', 24, 'Lucknow', 69),
(14, 'Simran', 19, 'Delhi', 84),
(15, 'Yash', 21, 'Mumbai', 91);


-- 1.Select all columns from students
SELECT * FROM students

-- 2.Select only name and age
SELECT name ,age FROM students

-- 3. Select only city column
SELECT city FROM students

-- 4. Students with age > 18
SELECT * FROM students
WHERE age > 18

-- 5. Students from 'Lucknow'
SELECT * FROM students
WHERE city = 'Lucknow';

-- 6. Students with age != 21
SELECT * FROM students
WHERE age != 21;

-- 7. Age > 18 AND marks > 70
SELEct * from students
where age > 18 and marks > 70

-- 8. City = 'Delhi' AND age > 20
select * from students
where city = 'Delhi' and age > 20

-- 9. Sort by age descending 
select * from students
order by age DESC

-- 10. Sort by city descending 
select * from students
order by city DESC

-- 11. Show first 5 students
select * from students
Limit 5

-- 12. Unique age values 
SELECT DISTINCT(age) from students
ORDER by age ASC
