create table project_schema.responsible_party
(
    user_id               varchar not null
        constraint responsible_party_pk
            primary key
        constraint user_id_fk
            references project_schema.user,
    associated_patient_id varchar not null
        constraint associated_patient_id_fk
            references project_schema.patient
);

alter table project_schema.responsible_party
    owner to postgres;

