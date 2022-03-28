create table project_schema.invoice
(
    invoice_id       serial
        constraint invoice_pk
            primary key,
    user_id          integer not null
        constraint user_id_fk
            references project_schema.patient,
    date_of_issue    date    not null,
    telephone        char    not null,
    email            char    not null,
    insurance_charge integer not null,
    patient_charge   integer not null,
    discount         integer,
    penalty_charge   integer
);

alter table project_schema.invoice
    owner to postgres;

