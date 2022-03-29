create table project_schema.payment
(
    payment_id       integer not null
        constraint payment_pk
            primary key,
    invoice_id       integer not null
        constraint invoice_id_fk
            references project_schema.invoice,
    payment_type     varchar    not null,
    patient_amount   integer not null,
    insurance_amount integer not null
);

alter table project_schema.payment
    owner to postgres;

