from psycopg2 import Error

from connection import get_db_connection
from utils import get_abs_filepath_from_module

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


def get_patient(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_patient.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching patient') from error


def get_patient_chart(chart_no: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_patient_chart.sql'), 'r') as file:
            cur.execute(file.read(), (chart_no,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching patient Chart ') from error


def get_admin(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_admin.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching admin') from error


def get_responsible_party(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_responsible_party.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching responsible party') from error


def get_employee(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_employee.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching employee') from error


def get_dentist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_dentist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching dentist') from error


def get_receptionist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_receptionist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching receptionist') from error


def get_hygienist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_hygienist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching hygienist') from error


def get_invoice(invoice_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_invoice.sql'), 'r') as file:
            cur.execute(file.read(), (invoice_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching invoice') from error


def get_payment(payment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_payment.sql'), 'r') as file:
            cur.execute(file.read(), (payment_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching payment') from error


def get_insurance_claim(insurance_claim_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_insurance_claim.sql'), 'r') as file:
            cur.execute(file.read(), (insurance_claim_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching payment') from error


def get_treatment(treatment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_treatment.sql'), 'r') as file:
            cur.execute(file.read(), (treatment_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching treatment') from error

def get_all_branches():
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_all_branches.sql'), 'r') as file:
            cur.execute(file.read())
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching all branches') from error

def get_branch(branch_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/get/get_branch.sql'), 'r') as file:
            cur.execute(file.read(), (branch_id,))
            conn.commit()
            return cur.fetchall()

    except Exception as error:
        raise Error('ERROR while fetching branch') from error
