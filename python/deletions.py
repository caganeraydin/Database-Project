from psycopg2 import Error

from connection import get_db_connection
from utils import get_abs_filepath_from_module

conn = get_db_connection()


def delete_user(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_user.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting user with email') from error


def deleteTreatment(treatment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_treatment.sql'), 'r') as file:
            cur.execute(file.read(), (treatment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting treatment') from error


def deleteAppointment(appointment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_appointment.sql'), 'r') as file:
            cur.execute(file.read(), (appointment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting treatment') from error
