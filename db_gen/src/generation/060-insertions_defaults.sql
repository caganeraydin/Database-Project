INSERT INTO project_schema."user"
VALUES ('666', 'default_firstname', 'default_middlename', 'default_lastname', 'N/A',
        'default_company', 666666, 'default@mail.com', DATE '2022-05-01', '666-666-6666',
        0, 'default');

INSERT INTO project_schema.address
VALUES (DEFAULT, 66, 66, 'default_city', 'default_province',
        'default_postalcode'); --Default id will start at 1

INSERT INTO project_schema.user_address
VALUES ('666', 1); -- NEED TO FIND BETTER WAY OF GETTING
                 -- LATEST ID VALUE ADDED

INSERT INTO project_schema.clinic_enterprise
VALUES (default, date '1999-02-04');

