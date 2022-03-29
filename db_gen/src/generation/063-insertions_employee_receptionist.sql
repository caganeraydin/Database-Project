--RECEPTIONIST #1
INSERT INTO project_schema."user"
VALUES (100, 'Lequisha', 'Martey', 'Paul', 'Woman',
        'Intact_insurance', 123212, 'Lequisha@mail.com', DATE '1981-05-01', '681-316-5226',
        41, 'Lequisha1');

INSERT INTO project_schema.address
VALUES (DEFAULT, 2, 4, 'Vancouver', 'British Columbia',
        'D4G 44W'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES (100, 7); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.employee
VALUES (100, 1, 'Permanent', 'Receptionist', date '1999-12-10', 45000, 12);

INSERT INTO project_schema.receptionist
VALUES (100, '#199')