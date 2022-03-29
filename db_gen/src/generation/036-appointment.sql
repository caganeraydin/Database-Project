create table project_schema.appointment
(
    appointment_id   int not null
        constraint appointment_pk
            primary key,
    invoice_id       int not null
        constraint invoice_id_fk
            references project_schema.invoice,
    patient_id       int not null
        constraint patient_id_fk
            references project_schema.patient,
    dentist_id       int not null
        constraint dentist_id_fk
            references project_schema.dentist,
    start_time       time,
    end_time         time,
    appointment_type char,
    status           char,
    room_assigned    varchar(10)
);

create unique index appointment_appointment_id_uindex
    on project_schema.appointment (appointment_id);

