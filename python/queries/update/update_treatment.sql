UPDATE project_schema.treatment
SET dentist_id = %s, chart_no = %s, appointment_type = %s, treatment_type = %s, medication = %s, symptoms = %s, tooth = %s, comments = %s
WHERE treatment_id = %s;