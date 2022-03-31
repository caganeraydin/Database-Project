create table project_schema.hygienist
(
    employee_id   varchar not null
        constraint hygienist_pk
            primary key
        constraint employee_id_fk
            references project_schema.employee ON DELETE CASCADE ON UPDATE CASCADE,
    certification varchar
);

create unique index hygienist_employee_id_uindex
    on project_schema.hygienist (employee_id);
