from psycopg2 import Error

from connection import get_db_connection
from utils import get_abs_filepath_from_module

conn = get_db_connection()


def updateTreatment(treatment_id: int, dentist_id: str, chart_no: int, appointment_type: str,
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
