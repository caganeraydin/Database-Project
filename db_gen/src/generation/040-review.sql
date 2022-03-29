create table project_schema.review
(
    review_id       int not null
        constraint review_pk
            primary key,
    patient_id      int not null
        constraint patient_id_fk
            references project_schema.patient,
    branch_id       int not null
        constraint branch_id_fk
            references project_schema.branch,
    professionalism int,
    communication   int,
    cleanliness     int,
    value           int
);

create unique index review_review_id_uindex
    on project_schema.review (review_id);

