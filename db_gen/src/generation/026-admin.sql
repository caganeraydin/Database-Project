create table project_schema.admin
(
    user_id    varchar not null
        constraint admin_pk
            primary key
        constraint user_id_fk
            references project_schema.user,
    privileges varchar
);

alter table project_schema.admin
    owner to postgres;

