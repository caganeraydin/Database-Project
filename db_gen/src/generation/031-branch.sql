create table project_schema.branch
(
    branch_id            int not null
        constraint branch_pk
            primary key,
    clinic_enterprise_id int
        constraint clinic_enterprise_id_fk
            references project_schema.clinic_enterprise
);

create unique index branch_branch_id_uindex
    on project_schema.branch (branch_id);
