--MANAGER #1
INSERT INTO project_schema."user"
VALUES ('123', 'doga', NULL, 'Uras', 'woman',
        'LaCapitale', 122211, 'doga@mail.com', DATE '1989-05-01', '627-316-5466',
        33, 'doga123');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'toronto', 'ontario',
        'J8S 2L1'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES (123, 3); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.address
VALUES (DEFAULT, 1, 100, 'toronto', 'ontario',
        '3S2 D5F'); --Default id will start at 1

INSERT INTO project_schema.branch
VALUES (1, 1, NULL);

INSERT INTO project_schema.branch_address
VALUES (4,1);

INSERT INTO project_schema.employee
VALUES ('123', 1, 'Permanent', 'Manager', date '2000-10-12', 122000, 14);

UPDATE project_schema.branch
SET manager_id = 123
WHERE branch_id = 1;

----------------------------------
--MANAGER #2
INSERT INTO project_schema."user"
VALUES ('124', 'Cagan', NULL, 'Eraydin', 'man',
        'Intact_insurance', 123212, 'Cagan@mail.com', DATE '1989-05-01', '627-316-5466',
        35, 'Cagan#111');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'hawksbury', 'ontario',
        'J2S 2L4'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('124', 5); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.address
VALUES (DEFAULT, 1, 100, 'ottawa', 'ontario',
        '3S1 S5P'); --Default id will start at 1

INSERT INTO project_schema.branch
VALUES (2, 1, NULL);

INSERT INTO project_schema.branch_address
VALUES (6,2);

INSERT INTO project_schema.employee
VALUES ('124', 2, 'Permanent', 'Manager', date '2000-10-12', 90000, 8);

UPDATE project_schema.branch
SET manager_id = 124
WHERE branch_id = 2;

