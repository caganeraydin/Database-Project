SELECT
    i.invoice_id,
    u.user_id,
    u.first_name,
    u.last_name,
    i.date_of_issue,
    i.telephone,
    i.email,
    i.insurance_charge,
    i.patient_charge,
    i.discount,
    i.penalty_charge

FROM
    project_schema."invoice" i,
    project_schema."user" u

WHERE i.user_id = u.user_id;
