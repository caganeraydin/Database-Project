alter table project_schema.branch
    add manager_id varchar;

alter table project_schema.branch
    add constraint manager_id_fk
        foreign key (manager_id) references project_schema.employee ON DELETE CASCADE ON UPDATE CASCADE;

alter table project_schema."user"
	add password varchar not null;

