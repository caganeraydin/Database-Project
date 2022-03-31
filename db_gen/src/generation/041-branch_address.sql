create table project_schema.branch_address
(
    address_id int not null
        constraint branch_address_pk
            primary key,
    branch_id  int not null
        constraint branch_id_fk
            references project_schema.branch ON DELETE CASCADE ON UPDATE CASCADE
);

create unique index branch_address_address_id_uindex
    on project_schema.branch_address (address_id);

