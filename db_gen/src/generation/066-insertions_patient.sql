INSERT INTO project_schema."user"
VALUES ('1', 'Paul', NULL, 'O_Connor', 'man', 'Intact-Insurance',
        123456, 'PO@mail.com', DATE '2009-05-01', '123-456-7890',
        13, 'patient');

INSERT INTO project_schema.address
VALUES (DEFAULT, 1, 1000, 'Gatineau', 'Quebec',
        'J3G 3S5'); --Default id will start at 1


INSERT INTO project_schema.user_address
VALUES ('1', 10); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE DDED

INSERT INTO project_schema.patient_chart
VALUES (122);

INSERT INTO project_schema.patient
VALUES ('1', 122, 'Intact_assurance_fullcoverage');

INSERT INTO project_schema.invoice
VALUES (1, '1', date '2021-09-11', '123-456-7890', 'PO@mail.com', 100, 200, 20, 0);

INSERT INTO project_schema.payment
VALUES (1, 1, 'VISA', 200, 100);

INSERT INTO project_schema.insurance_claim
VALUES (default , 1, 100);
