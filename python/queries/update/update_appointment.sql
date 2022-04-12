UPDATE project_schema.appointment
SET invoice_id = %s, patient_id = %s, dentist_id = %s, start_time = %s, end_time = %s, appointment_type = %s, status = %s, room_assigned = %s, date_of_appointment = %s
WHERE appointment_id = %s;
