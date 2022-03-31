create table project_schema.dentist
(
    employee_id varchar not null
        constraint dentist_pk
            primary key
        constraint employee_id_fk
            references project_schema.employee,
    diploma     varchar
);

create unique index dentist_employee_id_uindex
    on project_schema.dentist (employee_id);