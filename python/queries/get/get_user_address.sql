SELECT
    ad.address_id,
    ad.house_number,
    ad.street_number,
    ad.city,
    ad.province,
    ad.postal_code
FROM
    project_schema."user_address" uad,
    project_schema."address" ad
WHERE uad.user_id = %s AND ad.address_id = uad.address_id;

