--HYGENIST #1
INSERT INTO project_schema."user"
VALUES ('102', 'Maria', NULL, 'McLloyd', 'women',
        'LaCapitale', 123212, 'Maria@mail.com', DATE '1980-10-05', '454-787-7897',
        42, 'Maria');

INSERT INTO project_schema.address
VALUES (DEFAULT, 10, 111, 'Gatineau', 'Quebec',
        'D9G S4W'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('102', 9); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.employee
VALUES ('102', 1, 'Partial', 'Hygienist', date '2012-12-10', 40000, 10);

INSERT INTO project_schema.hygienist
VALUES  ('102', 'Certification in Hygienistery - University of Ottawa');