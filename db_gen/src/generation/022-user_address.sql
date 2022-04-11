create table project_schema.user_address
(
    user_id    varchar not null
        constraint user_id_pk
            references project_schema.user  ON DELETE CASCADE ON UPDATE CASCADE,
    address_id integer not null
        constraint address_id_fk
            references project_schema.address ON DELETE CASCADE ON UPDATE CASCADE

);

alter table project_schema.user_address
    owner to postgres;

ALTER TABLE project_schema.user_address
   ADD PRIMARY KEY (user_id, address_id);

