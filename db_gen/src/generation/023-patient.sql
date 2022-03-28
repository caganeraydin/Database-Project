create table project_schema.patient
(
    user_id        integer not null
        constraint party_pk
            primary key
        constraint user_id_fk
            references project_schema.user,
    chart_no       integer unique not null,
    insurance_type char    not null
);

alter table project_schema.patient
    owner to postgres;

