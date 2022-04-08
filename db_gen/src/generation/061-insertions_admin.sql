INSERT INTO project_schema."user"
VALUES ('admin', 'admin', null, 'admin', 'NA',
        'admin', 111111, 'admin@admin.com', DATE '1980-05-01', '621-316-5466',
        32, 'admin');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'ottawa', 'ontario',
        'J8R 3D1'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('admin', 2); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.admin
VALUES ('admin', 'Can shutdown the whole system'); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED