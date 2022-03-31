create table project_schema.receptionist
(
    employee_id     varchar not null
        constraint receptionist_pk
            primary key
        constraint employee_id_fk
            references project_schema.employee,
    phone_extension varchar(4)
);

create unique index receptionist_employee_id_uindex
    on project_schema.receptionist (employee_id);
