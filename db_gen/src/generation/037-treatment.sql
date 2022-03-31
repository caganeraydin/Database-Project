create table project_schema.treatment
(
    treatment_id     int not null
        constraint treatment_pk
            primary key,
    dentist_id       varchar not null
        constraint dentist_id_fk
            references project_schema.dentist ON DELETE CASCADE ON UPDATE CASCADE,
    chart_no         int not null
        constraint chart_no_fk
            references project_schema.patient_chart ON DELETE CASCADE ON UPDATE CASCADE,
    appointment_type varchar,
    treatment_type   varchar,
    medication       varchar,
    symptoms         varchar,
    tooth            varchar,
    comments         varchar
);

create unique index treatment_treatment_id_uindex
    on project_schema.treatment (treatment_id);

