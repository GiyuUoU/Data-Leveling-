SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT e.employee_id, e.department_id
FROM Employee e
JOIN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) = 1
) single_emp
ON e.employee_id = single_emp.employee_id;