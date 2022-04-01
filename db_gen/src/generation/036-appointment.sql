create table project_schema.appointment
(
    appointment_id   int not null
        constraint appointment_pk
            primary key,
    invoice_id       int not null
        constraint invoice_id_fk
            references project_schema.invoice ON DELETE CASCADE ON UPDATE CASCADE,
    patient_id       varchar not null
        constraint patient_id_fk
            references project_schema.patient ON DELETE CASCADE ON UPDATE CASCADE,
    dentist_id       varchar not null
        constraint dentist_id_fk
            references project_schema.dentist ON DELETE CASCADE ON UPDATE CASCADE,
    start_time       time,
    end_time         time,
    appointment_type varchar,
    status           varchar,
    room_assigned    varchar(10),
    date_of_appointment date
);

create unique index appointment_appointment_id_uindex
    on project_schema.appointment (appointment_id);

