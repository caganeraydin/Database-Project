create table project_schema.treatment
(
    treatment_id     int not null
        constraint treatment_pk
            primary key,
    dentist_id       int not null
        constraint dentist_id_fk
            references project_schema.dentist,
    chart_no         int not null
        constraint chart_no_fk
            references project_schema.patient_chart,
    appointment_type char,
    treatment_type   char,
    medication       char(100),
    symptoms         varchar(100),
    comments         varchar(100)
);

create unique index treatment_treatment_id_uindex
    on project_schema.treatment (treatment_id);

