from psycopg2 import Error

from connection import get_db_connection
from python.appointment_procedure_options import procedure_dict
from python.getters import get_last_address_id
from utils import get_abs_filepath_from_module

conn = get_db_connection()


def insert_user(user_id: str, first_name: str, middle_name: str, last_name: str, gender: str, insurance_company: str,
                ssn: int, email: str, date_of_birth: str, telephone: str, age: int, password: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_user.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                            user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email,
                            date_of_birth,
                            telephone, age, password))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert user') from error


def insert_address(house_number: int, street_number: int, city: str, province: str, postal_code: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_address.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                            house_number, street_number, city, province, postal_code))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert user') from error


def insert_user_address_latest(user_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_user_address.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                            user_id, get_last_address_id()))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert user_address with most recent address') from error


def insert_patient(user_id: str, chart_no: int, insurance_type: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_patient.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                            user_id, chart_no, insurance_type))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert patient') from error

def insert_employee(user_id: str, branch_id: int, employee_type: str, role: str, start_date: str, salary: str, years_of_experience: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_employee.sql'), 'r') as file:
            cur.execute(file.read(),
                        (user_id, branch_id, employee_type, role, start_date, salary, years_of_experience))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert employee') from error

def insert_patient_chart(chart_no: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_patient_chart.sql'), 'r') as file:
            cur.execute(file.read(), (chart_no,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert patient chart') from error


def insert_user_address(user_id: str, address_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_user_address.sql'), 'r') as file:
            cur.execute(file.read(),
                        (
                            user_id, address_id))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert user_address with specific address') from error


def insert_branch(branch_id: int, clinic_enterprise_id: int, manager_id: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_branch.sql'), 'r') as file:
            cur.execute(file.read(),
                        (branch_id, clinic_enterprise_id, manager_id))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert branch') from error


def insert_branch_address(address_id: int, branch_id: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_branch_address.sql'), 'r') as file:
            cur.execute(file.read(),
                        (address_id, branch_id))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert branch_address') from error


def insert_invoice(invoice_id: int, patient_id: str, date: str, telephone: str, email: str, insurance_charge: int,
                   patient_charge: int, discount: int, penalty: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_invoice.sql'), 'r') as file:
            cur.execute(file.read(),
                        (invoice_id, patient_id, date, telephone, email, insurance_charge,
                         patient_charge, discount, penalty))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert invoice') from error


def insert_payment(payment_id: int, invoice_id: int, payment_type: str, patient_amount: int, insurance_amount: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_payment.sql'), 'r') as file:
            cur.execute(file.read(),
                        (payment_id, invoice_id, payment_type, patient_amount, insurance_amount))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert invoice') from error


def insert_insurance_claim(insurance_claim_id: int, payment_id: int, amount_accepted: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_insurance_claim.sql'), 'r') as file:
            cur.execute(file.read(),
                        (insurance_claim_id, payment_id, amount_accepted))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert insurance claim') from error


def insert_appointment(appointment_id: int, invoice_id: int, patient_id: str, dentist_id: str, start_time: str,
                       end_time: str,
                       appointment_type: str, status: str, room_assigned: str, date_of_appointment: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_appointment.sql'), 'r') as file:
            cur.execute(file.read(),
                        (appointment_id, invoice_id, patient_id, dentist_id, start_time, end_time, appointment_type,
                         status, room_assigned, date_of_appointment))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert appointment') from error


def insert_appointment_procedure(procedure_type: str, appointment_id: int, tooth_involved: int, procedure_no: int):
    if procedure_type in procedure_dict:
        try:
            current_procedure = procedure_dict.get(procedure_type)
            cur = conn.cursor()
            with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_appointment_procedure.sql'),
                      'r') as file:
                cur.execute(file.read(),
                            (procedure_no, appointment_id, current_procedure[0], current_procedure[1],
                             current_procedure[2], tooth_involved, current_procedure[3]
                             ))
                conn.commit()

        except Exception as error:
            raise Error('ERROR: Cant insert appointment procedure') from error
    else:
        raise Error('No Such Procedure Exists') from Exception


def insert_fee_charge(fee_id: int, invoice_id: int, procedure_no: int, fee_code: str, fee_amount: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_fee_charge.sql'), 'r') as file:
            cur.execute(file.read(),
                        (fee_id, invoice_id, procedure_no, fee_code, fee_amount))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert fee charge') from error


def insert_receptionist(receptionist_id: str, phone_extension: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_receptionist.sql'), 'r') as file:
            cur.execute(file.read(),
                        (receptionist_id, phone_extension))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert receptionist') from error


def insert_dentist(dentist_id: str, diploma: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_dentist.sql'), 'r') as file:
            cur.execute(file.read(),
                        (dentist_id, diploma))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert dentist') from error


def insert_hygienist(hygienist_id: str, certification: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_hygienist.sql'), 'r') as file:
            cur.execute(file.read(),
                        (hygienist_id, certification))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert hygienist') from error


def insert_treatment(dentist_id: str, chart_no: int, appointment_type: str, treatment_type: str, medication: str,
                     symptoms: str, tooth: str, comments: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_treatment.sql'), 'r') as file:
            cur.execute(file.read(),
                        (dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms,
                         tooth, comments))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert treatment') from error


def insert_review(patient_id: str, branch_id: int, professionalism: int, communication: int,
                  cleanliness: int, value: int):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_review.sql'), 'r') as file:
            cur.execute(file.read(),
                        (patient_id, branch_id, professionalism, communication, cleanliness, value))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert review') from error


def insert_clinic_enterprise(year_of_establishment: str):
    try:
        cur = conn.cursor()
        with open(get_abs_filepath_from_module(__file__, 'queries/post/insert_clinic_enterprise.sql'), 'r') as file:
            cur.execute(file.read(),
                        (year_of_establishment,))
            conn.commit()

    except Exception as error:
        raise Error('ERROR: cant insert clinic enterprise') from error
