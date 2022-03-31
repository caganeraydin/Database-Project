create table project_schema.patient
(
    user_id        varchar not null
        constraint party_pk
            primary key
        constraint user_id_fk
            references project_schema.user ON DELETE CASCADE ON UPDATE CASCADE,
    chart_no       integer unique not null,
    insurance_type varchar    not null
);

alter table project_schema.patient
    owner to postgres;

alter table project_schema.patient
    add constraint chart_no_fk
        foreign key (chart_no) references project_schema.patient_chart ON DELETE CASCADE ON UPDATE CASCADE;

