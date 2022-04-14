SELECT
    start_time,
    end_time,
    appointment_type,
    status,
    room_assigned,
    date_of_appointment

FROM
    project_schema."appointment" a,
    project_schema."user" u

WHERE a.patient_id = u.user_id ;




