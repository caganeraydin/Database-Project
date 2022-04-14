SELECT
    first_name,
    last_name,
    gender,
    insurance_company,
    email,
    telephone,
    age
FROM
    project_schema."appointment" a,
    project_schema."user" u

WHERE a.patient_id = u.user_id ;