SELECT
    u.user_id,
    u.first_name,
    u.middle_name,
    u.last_name,
    u.gender,
    u.insurance_company,
    u.ssn,
    u.email,
    u.date_of_birth,
    u.telephone,
    u.age,
    u.password,
    ad.address_id,
    ad.house_number,
    ad.street_number,
    ad.city,
    ad.province,
    ad.postal_code,
    e.branch_id,
    e.employee_type,
    e.role,
    e.start_date,
    e.salary,
    e.years_of_experience
FROM
    project_schema."employee" e,
    project_schema."user" u,
    project_schema."user_address" uad,
    project_schema."address" ad
WHERE e.user_id = u.user_id AND uad.user_id = e.user_id AND ad.address_id = uad.address_id;

