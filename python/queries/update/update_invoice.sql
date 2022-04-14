UPDATE project_schema."invoice"
SET user_id = %s, date_of_issue = %s, telephone = %s, email = %s, insurance_charge = %s, patient_charge = %s, discount = %s, penalty_charge = %s
WHERE invoice_id = %s;
