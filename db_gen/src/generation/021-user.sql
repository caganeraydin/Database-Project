create table project_schema."user"
(
    user_id           varchar not null
        constraint user_pk
            primary key,
    first_name        varchar    not null,
    middle_name       varchar,
    last_name         varchar    not null,
    gender            varchar    not null,
    insurance_company varchar    not null,
    ssn               integer not null,
    email             varchar    not null unique,
    date_of_birth     date    not null,
    telephone         varchar    not null,
    age               integer not null
);

comment on table project_schema."user" is 'Table containing the user information';

alter table project_schema."user"
    owner to postgres;

create unique index user_user_id_index
    on project_schema."user" (user_id);

