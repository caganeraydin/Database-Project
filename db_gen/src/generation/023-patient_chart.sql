create table project_schema.patient_chart
(
    chart_no integer not null
        constraint patient_chart_pk
            primary key
);

alter table project_schema.patient_chart
    owner to postgres;


