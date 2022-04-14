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
    ad.street_name,
    ad.city,
    ad.province,
    ad.postal_code,
    p.chart_no,
    p.insurance_type
FROM
    project_schema."patient" p,
    project_schema."user" u,
    project_schema."user_address" uad,
    project_schema."address" ad
WHERE p.user_id = u.user_id AND uad.user_id = p.user_id AND ad.address_id = uad.address_id;
