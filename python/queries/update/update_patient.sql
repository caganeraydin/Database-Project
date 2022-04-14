BEGIN TRANSACTION;

UPDATE project_schema."user"
SET first_name = %s, middle_name = %s, last_name = %s, gender = %s, insurance_company = %s, ssn = %s, email = %s, date_of_birth = %s, telephone = %s, age = %s, password = %s
WHERE user_id = %s;

UPDATE project_schema."address"
SET house_number = %s, street_number = %s, city = %s, province = %s,  postal_code= %s
WHERE address_id = %s;

UPDATE project_schema."patient"
SET insurance_type = %s
WHERE user_id = %s;



COMMIT;
