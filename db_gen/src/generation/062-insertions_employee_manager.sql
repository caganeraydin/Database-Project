INSERT INTO project_schema."user"
VALUES (123, 'doga', NULL, 'Uras', 'woman',
        'McDonalds', 666666, 'doga@mail.com', DATE '1989-05-01', '627-316-5466',
        15, 'doga123');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'toronto', 'ontario',
        'J8S 2L1'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES (123, 3); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.employee
VALUES (123, 1, 'Permanent', 'Manager', date '2000-10-12', 100000, 12);

INSERT INTO project_schema.branch
VALUES (1, 1, 123,);
