from psycopg2 import Error

from connection import get_db_connection
from utils import get_abs_filepath_from_module

conn = get_db_connection()


def insert_user(user_id: int, first_name: str, middle_name: str, last_name: str, gender: str, insurance_company: str,
                ssn: int, email: str, date_of_birth: str, telephone: str, age: int, password: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_user.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                        user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth,
                        telephone, age, password))
            conn.commit()

    except Exception as error:
        raise Error('ERROR') from error
