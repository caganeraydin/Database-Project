import os
import random
import datetime

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from python.appointment_procedure_options import procedure_dict
from python.deletions import delete_user, delete_treatment, delete_patient
from python.getters import *
from python.inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insertAppointment, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_treatment, insert_review, insert_clinic_enterprise,insert_associate
from python.updaters import *
import python.updaters as up
import python.inserters as ins
import python.deletions as delt
from python.validation import generateInvoiceId

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'
app.secret_key = "Secret key"
db = SQLAlchemy(app)
current_employee = None


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='project_database',
                            user='postgres',
                            password='postgres')
    return conn


# Treatments
@app.route('/patient_home/<user_id>/')
def get_patient_home_page(user_id):


    first_name = (get_user_with_id(user_id)[0][1])
    middle_name = (get_user_with_id(user_id)[0][2])
    last_name = (get_user_with_id(user_id)[0][3])
    gender = (get_user_with_id(user_id)[0][4])
    insurance_company = (get_user_with_id(user_id)[0][5])
    ssn = (get_user_with_id(user_id)[0][6])
    email = (get_user_with_id(user_id)[0][7])
    birth_date = (get_user_with_id(user_id)[0][8])
    phone_number = (get_user_with_id(user_id)[0][9])
    age = (get_user_with_id(user_id)[0][10])
    password = (get_user_with_id(user_id)[0][11])
    invoices = get_invoice(user_id)
    responsible_party = get_responsible_party(user_id)


    appointments = get_all_appointments_patient(user_id)


    return render_template("patient_home.html", user_id=user_id, first_name=first_name, middle_name=middle_name, last_name=last_name,
                           gender=gender, insurance_company=insurance_company, ssn=ssn, birth_date=birth_date,
                           phone_number=phone_number, email=email, age=age, password=password, appointments=appointments, invoices=invoices,responsible_party=responsible_party)




@app.route('/get_appointmens_page/<user_id>')
def get_appointments_page(user_id):
    return render_template("appointments.html", user_id=user_id)


@app.route('/insert_appointment/<user_id>', methods=['POST'])
def insert_appointment(user_id):

    # if request.method == 'POST':

    invoice_id = generateInvoiceId()
    print(invoice_id)

    dentist_id = request.form['dentist_id']
    print(dentist_id)
    start_time = request.form['start_time']
    print(start_time)
    string_time = str(start_time)
    start_hour = string_time[0] + string_time[1]
    start_minutes = string_time[3] + string_time[4]
    date_start_time = datetime.timedelta(hours = int(start_hour), minutes = int(start_minutes))
    print('start' + str(date_start_time))
    appointment_type = request.form['appointment_type']

    time_complete = procedure_dict.get(appointment_type)[4]
    end_hour = time_complete[0] + time_complete[1]
    end_minute = time_complete[3] + time_complete[4]
    date_end_time = datetime.timedelta(hours = int(end_hour), minutes = int(end_minute))
    final_end_time = date_start_time + date_end_time
    print(appointment_type)

    # date_end_time = datetime.timedelta(hours = start_hour, seconds = start_minutes)
    status = request.form['status']
    print(status)

    date_of_appointment = request.form['date_of_appointment']
    print(date_of_appointment)

    if not (get_dentist(dentist_id)):
        print("here1")
        flash("Dentist Id you entered does not exist, please try again.", "danger")
        return redirect(url_for('get_appointments_page',user_id=user_id))
    if not (get_patient(user_id)):
        print("here3")
        flash("Patient Id you entered does not exist, please try again.", "danger")
        return redirect(url_for('get_appointments_page',user_id=user_id))
    if get_start_time(start_time):
        print("here4")
        flash("The time you entered is not available, please choose another time.", "danger")
        return redirect(url_for('get_appointments_page',user_id=user_id))
    else:
        print("here6")
        user = get_user_with_id(get_patient(user_id)[0][0])
        procedure = procedure_dict[str(appointment_type)]

        insert_invoice(invoice_id, user_id, date_of_appointment,user[0][9], user[0][7], 0, procedure[3], None, None)
        appointment = insertAppointment(invoice_id, user_id, dentist_id, start_time, str(final_end_time), appointment_type, status, "", date_of_appointment)
        procedure_no = insert_appointment_procedure(appointment_type, appointment[0][0], 1)

        insert_fee_charge(invoice_id, int(procedure_no[0][0]), procedure[0], procedure[3])


        flash("Appointment Inserted Successfully", "success")
        return redirect(url_for('get_patient_home_page',user_id=user_id))




@app.route('/update_patient/<user_id>', methods=['GET', 'POST'])
def update_patient(user_id, address_id, emp_id):
    print(current_employee)
    if request.method == 'POST':
        print(user_id + ", " + address_id)

        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        insurance_company = request.form['insurance_company']
        ssn = request.form['ssn']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        telephone = request.form['telephone']
        age = request.form['age']
        password = request.form['password']
        house_number = request.form['house_number']
        street_number = request.form['street_number']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']

        up.update_patient(user_id, first_name, middle_name, last_name, gender,
                          insurance_company, ssn, email, date_of_birth, telephone,
                          age, password, address_id, house_number, street_number,
                          city, province, postal_code)
        flash("Event Updated Successfully")
        return redirect(url_for('get_employee_home_page', user_id=emp_id))


@app.route('/insert_responsible_party/<user_id>', methods=['POST'])
def insert_responsible_party(user_id):
    # replace with generation method
    n = random.randint(1, 300000)
    resp_id = get_user_with_id(str(n))
    while resp_id:
        n = random.randint(1, 300000)
        resp_id = get_user_with_id(str(n))

    resp_id = n

    # if request.method == 'POST':

    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    insurance_company = request.form['insurance_company']
    ssn = request.form['ssn']
    date_of_birth = request.form['date_of_birth']
    telephone = request.form['telephone']
    email = request.form['email']
    age = request.form['age']
    password = request.form['password']

    print(first_name)
    print(middle_name)
    print(last_name)
    print(gender)
    print(insurance_company)
    print(ssn)
    print(date_of_birth)
    print(telephone)
    print(email)
    print(date_of_birth)
    print(telephone)
    print(age)
    print(password)

    insert_user(resp_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth,
                telephone, age, password)
    insert_associate(user_id, resp_id)

    flash("Reponsible Party Added Successfully")
    return redirect(url_for('get_patient_home_page', user_id=user_id))

# this route is for inserting a new treatment to postgres database via html
@app.route('/insert_patient/<emp_id>', methods=['POST'])
def insert_patient(emp_id):
    # replace with generation method
    n = random.randint(1, 300000)
    user_id = get_user_with_id(str(n))
    while user_id:
        n = random.randint(1, 300000)
        user_id = get_user_with_id(str(n))

    n1 = random.randint(1, 300000)
    chart_no = get_patient_chart(str(n1))
    while chart_no:
        n1 = random.randint(1, 300000)
        chart_no = get_patient_chart(str(n1))

    user_id = n
    chart_no = n1

    # if request.method == 'POST':

    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    insurance_type = request.form['insurance_type']
    gender = request.form['gender']
    insurance_company = request.form['insurance_company']
    ssn = request.form['ssn']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']
    telephone = request.form['telephone']
    age = request.form['age']
    password = request.form['password']
    house_number = request.form['house_number']
    street_number = request.form['street_number']
    city = request.form['city']
    province = request.form['province']
    postal_code = request.form['postal_code']

    if get_user_with_email(email):
        flash("account with the email address you entered already exists, please try again.")
        return redirect(url_for('get_employee_home_page'))
    else:
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth,
                    telephone, age, password)
        insert_address(house_number, street_number, city, province, postal_code)
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        address_ids = get_all_addresses()
        address_id = address_ids[len(address_ids) - 1][0]
        ins.insert_user_address(user_id, address_id)
        flash("Patient Added Successfully")
        return redirect(url_for('get_employee_home_page', user_id=emp_id))


# this is our update route to modify an already existing patient
@app.route('/update_p/<user_id>/', methods=['POST'])
def update_p(user_id):

    print(user_id)


    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    insurance_company = request.form['insurance_company']
    ssn = request.form['ssn']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']
    telephone = request.form['telephone']
    age = request.form['age']
    password = request.form['password']

    print(email)
    print(insurance_company)
    print(gender)
    print(telephone)

    update_patientt(user_id=user_id, first_name=first_name, middle_name=middle_name, last_name=last_name, gender=gender,
                          insurance_company=insurance_company, ssn=ssn, email=email, date_of_birth=date_of_birth, telephone=telephone,
                          age=age, password=password)



    flash("Event Updated Successfully")
    return redirect(url_for('get_patient_home_page', user_id=user_id))


#
#
# This route is for deleting a treatment
@app.route('/delete_patient/<user_id>/<emp_id>/', methods=['GET', 'POST'])
def delete_patient(user_id, emp_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_employee_home_page', user_id=emp_id))


# This route is for deleting a treatment
@app.route('/delete_invoice/<invoice_id>/<emp_id>/', methods=['GET', 'POST'])
def delete_invoice(invoice_id, emp_id):
    delt.delete_invoice(invoice_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_employee_home_page', user_id=emp_id))


@app.route('/')
def show_all():
    conn = get_db_connection()
    # insert_patient(10)
    # insert_patient_chart(30)
    # delete_user('edaefault@mail.com')
    # insert_branch(1234, 1, '123')
    # insert_branch_address(1, 1)
    # insert_appointment(123,1,'1','101','13:00','13:30','tooth_removal','tbd','C121','2020-10-10')
    # insert_fee_charge(3, 1, 1,'23', 50)
    # insert_receptionist('123', '12')
    # insert_dentist('123', '12')
    # insert_hygienist('123', '12')
    # insert_invoice(123, '1', '2002-10-10', '12', '12', 1,1,1,1)
    # insert_payment(13,123,'lol', 10, 10)
    # insert_insurance_claim(4,3,10)
    # insert_user_address_latest('1439')
    # insert_user('1439','kut','K.','sad','mail','some company',489489489,'email@smtn.this','1965-08-09','987-876-7665',55,'Aeatclassic!')
    # insert_appointment_procedure('Root Canal',1, 4, 6)
    # insert_address(2, 2,'gat','qc','adf')
    # insert_treatment('101',122,'test','test','test','test','test','test')
    # insert_review('1', 1, 1,1,1, 1)
    # insert_clinic_enterprise('2020-12-12')
    # print(get_treatment(1))
    # delete_treatment(1)
    # print(get_treatment(1))
    # update_treatment(1, '101', 122, 'test','test', 'test', 'test', 'test', 'test')
    # update_user('666', 'test', 'test', 'test', 'test', 'test',12, 'test', '2222-12-12', 'test',12, 'test')

    # print(get_last_address_id())

    # delete_user('666', 'default@mail.com')

    cur = conn.cursor()
    users = get_all_users()

    cur.close()
    conn.close()

    return render_template('show_all.html', Users=users)


# me = user('123','abc',None,'def','male','sunlife','123456789','gmail@hotmail.com','2020-03-29','888-999-7766','2','pasword')
# db.session.add(me)
# db.session.commit()
# db.create_all()


app.run()
