SELECT
    r.employee_id,
    e.branch_id
FROM
    project_schema."receptionist" r,
    project_schema."employee" e
WHERE r.employee_id = e.user_id;

