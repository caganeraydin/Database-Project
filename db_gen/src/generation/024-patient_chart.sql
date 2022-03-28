create table project_schema.patient_chart
(
    chart_no integer not null
        constraint patient_chart_pk
            primary key
        constraint chart_no_fk
            references project_schema.patient (chart_no)
);

alter table project_schema.patient_chart
    owner to postgres;

