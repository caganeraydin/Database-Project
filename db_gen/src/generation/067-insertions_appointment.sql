INSERT INTO project_schema.appointment
VALUES (DEFAULT, 1, '1', '101', time '13:30', time '15:30', 'Tooth Removal', 'Completed', 'B02', date '2021-09-11');

INSERT INTO project_schema.appointment_procedure
VALUES (DEFAULT, 1, 'C1D1', 'Full anesthesia', 'Full anesthesia around the tooth to be removed', 1, 300);

INSERT INTO project_schema.fee_charge
VALUES (DEFAULT, 1, 1, 'B011', 200);

INSERT INTO project_schema.fee_charge
VALUES (DEFAULT, 1, 1, 'B012', 100);

