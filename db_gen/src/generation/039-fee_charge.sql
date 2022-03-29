create table project_schema.fee_charge
(
    fee_id       int not null
        constraint fee_charge_pk
            primary key,
    invoice_id   int not null
        constraint invoice_id_fk
            references project_schema.invoice,
    procedure_no int not null
        constraint procedure_no_fk
            references project_schema.appointment_procedure,
    fee_code     varchar,
    fee_amount   int
);

create unique index fee_charge_fee_id_uindex
    on project_schema.fee_charge (fee_id);

