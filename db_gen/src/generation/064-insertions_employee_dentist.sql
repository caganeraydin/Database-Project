--DENTIST #1
INSERT INTO project_schema."user"
VALUES ('101', 'Cem', NULL, 'Kiyik', 'man',
        'LaCapitale', 123212, 'Cem@mail.com', DATE '1990-10-05', '452-435-3453',
        32, 'Cem211');

INSERT INTO project_schema.address
VALUES (DEFAULT, 2, 'McConald', 'Gatineau', 'Quebec',
        'D9G S4W'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('101', 8); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.employee
VALUES ('101', 1, 'Permanent', 'Dentist', date '1999-12-10', 45000, 12);

INSERT INTO project_schema.dentist
VALUES  ('101', 'Doctorate of Dentistery - University of Toronto');