create table project_schema.appointment_procedure
(
    procedure_no        int not null
        constraint appointment_procedure_pk
            primary key,
    appointment_id      int not null
        constraint appointment_id_fk
            references project_schema.appointment,
    date                date,
    procedure_code      varchar(10),
    procedure_type      varchar(10),
    description         varchar(100),
    tooth_involved      bit,
    amount_of_procedure int
);

create unique index appointment_procedure_procedure_no_uindex
    on project_schema.appointment_procedure (procedure_no);

