alter table project_schema.branch
    add manager_id int not null;

alter table project_schema.branch
    add constraint manager_id_fk
        foreign key (manager_id) references project_schema.employee;

alter table project_schema."user"
	add password varchar not null;

