from psycopg2 import Error

from python.connection import get_db_connection
from python.utils import get_abs_filepath_from_module

conn = get_db_connection()


def get_all_users():
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_all_users.sql'), 'r') as file:
            cur.execute(file.read())
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching all users') from error


def get_user_with_id(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_user.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching user') from error


def get_user_with_email(email: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_user_with_email.sql'), 'r') as file:
            cur.execute(file.read(), (email,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching user with email') from error


def get_all_addresses():
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_all_addresses.sql'), 'r') as file:
            cur.execute(file.read())
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching all addresses') from error


def get_last_address_id():
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_latest_address_id.sql'), 'r') as file:
            cur.execute(file.read())
            conn.commit()
            return cur.fetchall()[0][0]
    except Exception as error:
        raise Error('ERROR while fetching last address id') from error
