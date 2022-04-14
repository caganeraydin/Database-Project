UPDATE project_schema.invoice
SET insurance_charge = %s, paid=%s
WHERE invoice_id = %s;