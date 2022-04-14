SELECT
    start_time,
    end_time,
    appointment_type,
    status,
    room_assigned,
    date_of_appointment

FROM
    project_schema."appointment" a

WHERE a.patient_id = %s;

