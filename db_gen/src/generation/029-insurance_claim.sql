create table project_schema.insurance_claim
(
    insurance_claim_id integer not null
        constraint insurance_claim_pk
            primary key,
    payment_id         integer not null
        constraint payment_id_fk
            references project_schema.payment ON DELETE CASCADE ON UPDATE CASCADE,
    amount_accepted    integer not null
);

alter table project_schema.insurance_claim
    owner to postgres;

