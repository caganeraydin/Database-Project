create table project_schema.admin
(
    user_id    integer not null
        constraint admin_pk
            primary key
        constraint user_id_fk
            references project_schema.user,
    privileges char
);

alter table project_schema.admin
    owner to postgres;

