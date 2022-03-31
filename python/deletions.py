from psycopg2 import Error

from python.connection import get_db_connection
from python.utils import get_abs_filepath_from_module

conn = get_db_connection()


def delete_user(user_id: str, email:str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_user.sql'), 'r') as file:
            cur.execute(file.read(), (user_id, email))
            conn.commit()

    except Exception as error:
        raise Error('ERROR') from error
