INSERT INTO project_schema."user"
VALUES (2, 'eda', 'su', 'bicer', 'woman',
        'gov_of_canada', 666666, 'edaefault@mail.com', DATE '1980-05-01', '621-316-5466',
        15, 'eda123');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'ottawa', 'ontario',
        'J8R 3D1'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES (2, 2); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.admin
VALUES (2, 'Can shutdown the whole system'); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED