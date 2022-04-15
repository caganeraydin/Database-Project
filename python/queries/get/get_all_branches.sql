SELECT
    b.branch_id,
    ad.house_number,
    ad.street_name,
    ad.city,
    ad.province,
    ad.postal_code
FROM
    project_schema."branch" b,
    project_schema."branch_address" bad,
    project_schema."address" ad
WHERE b.branch_id = bad.branch_id AND bad.address_id = ad.address_id;