INSERT INTO project_schema."user"
VALUES ('1', 'Paul', NULL, 'O_Connor', 'Male', 'Intact-Insurance',
        123456, 'po@gmail.com', DATE '2009-05-01', '123-456-7890',
        13, 'patient');

INSERT INTO project_schema.address
VALUES (DEFAULT, 1, 'Saint-Jean', 'Gatineau', 'Quebec',
        'J3G 3S5'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('1', 10);

INSERT INTO project_schema.patient_chart
VALUES (122);

INSERT INTO project_schema.patient
VALUES ('1', 122, 'Intact_assurance_fullcoverage');

INSERT INTO project_schema.invoice
VALUES (1, '1', date '2021-09-11', '123-456-7890', 'po@gmail.com', 100, 165, 0, 0,FALSE);

INSERT INTO project_schema.payment
VALUES (DEFAULT , 1, 'VISA', 200, 100);

INSERT INTO project_schema.insurance_claim
VALUES (default , 1, 100);
