UPDATE project_schema.user
SET first_name = %s, middle_name = %s, last_name = %s, gender = %s, insurance_company = %s, ssn = %s, email = %s, date_of_birth = %s, telephone = %s, age = %s, password = %s
WHERE user_id = %s;