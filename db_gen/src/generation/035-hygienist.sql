create table project_schema.hygienist
(
    employee_id   int not null
        constraint hygienist_pk
            primary key
        constraint employee_id_fk
            references project_schema.employee,
    certification char
);

create unique index hygienist_employee_id_uindex
    on project_schema.hygienist (employee_id);
