create table project_schema.clinic_enterprise
(
    clinic_enterprise_id  serial
        constraint clinic_enterprise_pk
            primary key,
    year_of_establishment date not null
);

alter table project_schema.clinic_enterprise
    owner to postgres;

