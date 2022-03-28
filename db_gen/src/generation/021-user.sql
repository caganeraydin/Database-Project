create table project_schema."user"
(
    user_id           integer not null
        constraint user_pk
            primary key,
    first_name        char    not null,
    middle_name       char,
    last_name         char    not null,
    gender            char    not null,
    insurance_company char    not null,
    ssn               integer not null,
    email             char    not null,
    date_of_birth     date    not null,
    telephone         char    not null,
    age               integer not null
);

comment on table project_schema."user" is 'Table containing the user information';

alter table project_schema."user"
    owner to postgres;

create unique index user_user_id_index
    on project_schema."user" (user_id);

