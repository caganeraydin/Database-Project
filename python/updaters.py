from psycopg2 import Error

from python.connection import get_db_connection
from python.utils import get_abs_filepath_from_module

conn = get_db_connection()


def update_treatment(treatment_id: int, dentist_id: str, chart_no: int, appointment_type: str,
                     treatment_type: str, medication: str, symptoms: str, tooth: str, comments: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/update/update_treatment.sql'), 'r') as file:
            cur.execute(file.read(),
                        (dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms,
                         tooth, comments, treatment_id))
            conn.commit()
    except Exception as error:
        raise Error('ERROR: cant update treatment') from error


def update_user(user_id: str, first_name: str, middle_name: str, last_name: str, gender: str, insurance_company: str,
                ssn: int, email: str, date_of_birth: str, telephone: str, age: int, password: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/update/update_user.sql'), 'r') as file:
            cur.execute(file.read(),
                        (first_name, middle_name, last_name, gender, insurance_company, ssn,
                         email, date_of_birth, telephone, age, password, user_id))
            conn.commit()
    except Exception as error:
        raise Error('ERROR: cant update user') from error
