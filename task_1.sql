/* 1 */
SELECT name AS Course_Name
FROM courses;

/* 2 */
SELECT name as Teacher_Name
FROM teachers;

/* 3 */
SELECT  teachers.name, COUNT(courses.teacher_id) as number_of_courses
FROM courses INNER JOIN teachers ON courses.teacher_id = teachers.id
GROUP BY courses.teacher_id
ORDER BY  number_of_courses DESC;

/* 4 */
SELECT  teachers.name AS Teacher_with_no_course
FROM courses RIGHT OUTER JOIN teachers ON courses.teacher_id = teachers.id
WHERE courses.teacher_id IS NULL;