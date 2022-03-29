create table project_schema.address
(
    address_id    serial
        constraint address_pk
            primary key,
    house_number  integer not null,
    street_number integer not null,
    city          varchar,
    province      varchar,
    postal_code   varchar    not null
);

comment on table project_schema.address is 'Table containing the addresses of all users';

alter table project_schema.address
    owner to postgres;

