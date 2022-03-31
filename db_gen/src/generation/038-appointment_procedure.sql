create table project_schema.appointment_procedure
(
    procedure_no        int not null
        constraint appointment_procedure_pk
            primary key,
    appointment_id      int
        constraint appointment_id_fk
            references project_schema.appointment,
    procedure_code      varchar(10),
    procedure_type      varchar,
    description         varchar,
    tooth_involved      int,
    amount_of_procedure int
);

create unique index appointment_procedure_procedure_no_uindex
    on project_schema.appointment_procedure (procedure_no);

