create table project_schema.employee
(
    user_id             int not null
        constraint employee_pk
            primary key
        constraint user_id_fk
            references project_schema."user",
    branch_id           int not null
        constraint branch_id_fk
            references project_schema.branch,
    employee_type       varchar(20),
    role                varchar(50),
    start_date          date,
    salary              int,
    years_of_experience int
);

create unique index employee_user_id_uindex
    on project_schema.employee (user_id);

