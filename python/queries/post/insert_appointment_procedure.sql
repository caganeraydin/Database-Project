INSERT INTO project_schema.appointment_procedure
VALUES (DEFAULT, %s, %s, %s, %s, %s, %s) returning procedure_no;

