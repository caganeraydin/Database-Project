create table project_schema.invoice
(
    invoice_id       integer
        constraint invoice_pk
            primary key,
    user_id          varchar not null
        constraint user_id_fk
            references project_schema.patient ON DELETE CASCADE ON UPDATE CASCADE,
    date_of_issue    date    not null,
    telephone        varchar    not null,
    email            varchar    not null,
    insurance_charge integer not null,
    patient_charge   integer not null,
    discount         integer,
    penalty_charge   integer
);

alter table project_schema.invoice
    owner to postgres;

