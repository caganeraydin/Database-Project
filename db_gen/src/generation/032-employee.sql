create table project_schema.employee
(
    user_id             varchar not null
        constraint employee_pk
            primary key
        constraint user_id_fk
            references project_schema."user" ON DELETE CASCADE ON UPDATE CASCADE,
    branch_id           int not null
        constraint branch_id_fk
            references project_schema.branch ON DELETE CASCADE ON UPDATE CASCADE,
    employee_type       varchar(20),
    role                varchar(50),
    start_date          date,
    salary              int,
    years_of_experience int
);

create unique index employee_user_id_uindex
    on project_schema.employee (user_id);

