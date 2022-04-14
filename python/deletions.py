from psycopg2 import Error

from python.connection import get_db_connection
from python.utils import get_abs_filepath_from_module

conn = get_db_connection()


def delete_user(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_user.sql'), 'r') as file:
            cur.execute(file.read(), (user_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting user with email') from error


def delete_address(address_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_address.sql'), 'r') as file:
            cur.execute(file.read(), (address_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting address') from error


def delete_patient(patient_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_patient.sql'), 'r') as file:
            cur.execute(file.read(), (patient_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting patient') from error


def delete_employee(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_employee.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting patient') from error


def delete_responsible_party(responsible_party_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_responsible_party.sql'), 'r') as file:
            cur.execute(file.read(), (responsible_party_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting responsible party') from error


def delete_admin(admin_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_admin.sql'), 'r') as file:
            cur.execute(file.read(), (admin_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting admin') from error


def delete_patient_chart(chart_no: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_patient_chart.sql'), 'r') as file:
            cur.execute(file.read(), (chart_no,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting patient chart') from error


def delete_invoice(invoice_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_invoice.sql'), 'r') as file:
            cur.execute(file.read(), (invoice_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting invoice') from error


def delete_payment(payment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_payment.sql'), 'r') as file:
            cur.execute(file.read(), (payment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting payment') from error


def delete_insurance_claim(insurance_claim_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_insurance_claim.sql'), 'r') as file:
            cur.execute(file.read(), (insurance_claim_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting insurance claim') from error


def delete_appointment(appointment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_appointment.sql'), 'r') as file:
            cur.execute(file.read(), (appointment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting appointment') from error


def delete_appointment(appointment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_appointment.sql'), 'r') as file:
            cur.execute(file.read(), (appointment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting appointment id') from error


def delete_appointment_procedure(procedure_no: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_appointment_procedure.sql'),
                  'r') as file:
            cur.execute(file.read(), (procedure_no,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting appointment procedure') from error


def delete_fee_charge(fee_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_fee_charge.sql'), 'r') as file:
            cur.execute(file.read(), (fee_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting fee charge') from error


def delete_receptionist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_receptionist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting receptionist') from error


def delete_dentist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_dentist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting dentist') from error


def delete_hygienist(employee_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_hygienist.sql'), 'r') as file:
            cur.execute(file.read(), (employee_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting hygienist') from error


def delete_treatment(treatment_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_treatment.sql'), 'r') as file:
            cur.execute(file.read(), (treatment_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting treatment') from error


def delete_review(review_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_review.sql'), 'r') as file:
            cur.execute(file.read(), (review_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting review') from error


def delete_branch(branch_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_branch.sql'), 'r') as file:
            cur.execute(file.read(), (branch_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting branch') from error


def delete_clinic_enterprise(clinic_enterprise_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/delete/delete_clinic_enterprise.sql'), 'r') as file:
            cur.execute(file.read(), (clinic_enterprise_id,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR while deleting clinic_enterprise') from error
