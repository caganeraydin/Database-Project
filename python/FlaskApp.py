import os
import random

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from deletions import delete_user, delete_treatment, delete_patient
from getters import *
from inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_appointment, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_treatment, insert_review, insert_clinic_enterprise
from updaters import *
import updaters as up
import inserters as ins
import deletions as delt

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


class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    middle_name = db.Column(db.String())
    last_name = db.Column(db.String())
    gender = db.Column(db.String())
    insurance_company = db.Column(db.String())
    ssn = db.Column(db.Integer)
    email = db.Column(db.String())
    date_of_birth = db.Column(db.String())
    telephone = db.Column(db.String())
    age = db.Column(db.Integer)
    password = db.Column(db.String())

    def __init__(self, user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email,
                 date_of_birth, telephone, age, password):
        self.user_id = user_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.insurance_company = insurance_company
        self.ssn = ssn
        self.email = email
        self.date_of_birth = date_of_birth
        self.telephone = telephone
        self.age = age
        self.password = password


# Employee Home Page
@app.route('/employee_home/<user_id>/')
def get_employee_home_page(user_id):

    print(get_employee(user_id))
    all_patients = get_all_patients()
    all_appointments = get_all_appointments()
    all_invoices = get_all_invoices()
    cur_employee = get_employee(user_id)[0]
    cur_emp_user_info = get_user_with_id(user_id)[0]
    cur_employee_address = get_user_address(user_id)[0]
    current_employee = user_id
    print(current_employee)

    return render_template("employee_home.html", Patients = all_patients, Appointments = all_appointments, Invoices = all_invoices, employee = cur_employee, emp_profile = cur_emp_user_info, emp_address = cur_employee_address)


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_patient/<emp_id>', methods = ['POST'])
def insert_patient(emp_id):
    # replace with generation method
    n = random.randint(1,300000)
    user_id = get_user_with_id(str(n))
    while user_id:
        n = random.randint(1,300000)
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
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        insert_address(house_number, street_number, city, province, postal_code)
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        address_ids = get_all_addresses()
        address_id = address_ids[len(address_ids)- 1][0]
        ins.insert_user_address(user_id,address_id)
        flash("Patient Added Successfully")
        return redirect(url_for('get_employee_home_page', user_id = emp_id))


# this is our update route to modify an already existing patient
@app.route('/update_patient/<user_id>/<address_id>/<emp_id>/', methods = ['GET', 'POST'])
def update_patient(user_id,address_id, emp_id):
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

        up.update_patient(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_number,
                       city, province, postal_code)
        flash("Event Updated Successfully")
        return redirect(url_for('get_employee_home_page', user_id = emp_id))


# this is our update route to modify an already existing employee
@app.route('/update_employee/<user_id>/<address_id>/', methods = ['GET', 'POST'])
def update_employee(user_id,address_id):

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

        up.update_employee_profile(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_number,
                       city, province, postal_code)
        flash("Event Updated Successfully")

        return redirect(url_for('get_employee_home_page', user_id = user_id))


# this is our update route to modify an already existing invoice
@app.route('/update_invoice/<invoice_id>/<user_id>/<emp_id>/', methods = ['GET', 'POST'])
def update_invoice(invoice_id, user_id, emp_id):

    if request.method == 'POST':

        date_of_issue = request.form['date_of_issue']
        telephone = request.form['telephone']
        email = request.form['email']
        insurance_charge = request.form['insurance_charge']
        patient_charge = request.form['patient_charge']
        discount = request.form['discount']
        penalty_charge = request.form['penalty_charge']

        up.update_invoice(invoice_id, user_id, date_of_issue,
                          telephone, email, insurance_charge, patient_charge,
                          discount, penalty_charge)
        flash("Event Updated Successfully")

        return redirect(url_for('get_employee_home_page', user_id = emp_id))


# This route is for deleting a patient
@app.route('/delete_patient/<user_id>/<emp_id>/', methods = ['GET', 'POST'])
def delete_patient(user_id, emp_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_employee_home_page', user_id = emp_id))


# This route is for deleting a invoice
@app.route('/delete_invoice/<invoice_id>/<emp_id>/', methods = ['GET', 'POST'])
def delete_invoice(invoice_id, emp_id):
    delt.delete_invoice(invoice_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_employee_home_page', user_id = emp_id))


# Admin
@app.route('/admin_home/')
def get_admin_home_page():
    patients = get_all_patients()
    employees = get_all_employees()
    invoices = get_all_invoices()
    appointments = get_all_appointments()
    return render_template("admin_home.html",
                           Patients = patients,
                           Employees = employees,
                           Invoices = invoices,
                           Appointments = appointments)


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_patient_admin/', methods = ['POST'])
def insert_patient_admin():
    # replace with generation method

    n = random.randint(1,300000)
    user_id = get_user_with_id(str(n))
    while user_id:
        n = random.randint(1,300000)
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
    print(first_name)
    middle_name = request.form['middle_name']
    print(middle_name)
    last_name = request.form['last_name']
    print(last_name)
    insurance_type = request.form['insurance_type']
    print(insurance_type)
    gender = request.form['gender']
    print(gender)
    insurance_company = request.form['insurance_company']
    print(insurance_company)
    ssn = request.form['ssn']
    print(ssn)
    email = request.form['email']
    print(email)
    date_of_birth = request.form['date_of_birth']
    print(date_of_birth)
    telephone = request.form['telephone']
    print(telephone)
    age = request.form['age']
    print(age)
    password = request.form['password']
    print(password)
    house_number = request.form['house_number']
    print(house_number)
    street_number = request.form['street_number']
    print(street_number)
    city = request.form['city']
    print(city)
    province = request.form['province']
    print(province)
    postal_code = request.form['postal_code']
    print(postal_code)

    if get_user_with_email(email):
        flash("account with the email address you entered already exists, please try again.")
        return redirect(url_for('get_admin_home_page'))
    else:
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        address_id = insert_address(house_number, street_number, city, province, postal_code)[0]
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        ins.insert_user_address(user_id, address_id)
        flash("Patient Added Successfully")
        return redirect(url_for('get_admin_home_page'))


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_employee_admin/', methods = ['POST'])
def insert_employee_admin():
    # replace with generation method
    n = random.randint(1,300000)
    user_id = get_user_with_id(str(n))
    while user_id:
        n = random.randint(1,300000)
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
        return redirect(url_for('get_admin_home_page'))
    else:
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        insert_address(house_number, street_number, city, province, postal_code)
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        address_ids = get_all_addresses()
        address_id = address_ids[len(address_ids)- 1][0]
        ins.insert_user_address(user_id,address_id)
        flash("Patient Added Successfully")
        return redirect(url_for('get_admin_home_page'))


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_employee_admin/<user_id>', methods = ['POST'])
def insert_invoice_admin(user_id):
    # replace with generation method

    n = random.randint(1, 300000)
    invoice_id = get_invoice(n)
    while invoice_id:
        n = random.randint(1, 300000)
        invoice_id = get_patient_chart(n)

    invoice_id = n

    date_of_issue = request.form['date_of_issue']
    telephone = request.form['telephone']
    email = request.form['email']
    insurance_charge = request.form['insurance_charge']
    patient_charge = request.form['patient_charge']
    discount = request.form['discount']
    penalty_charge = request.form['penalty_charge']

    insert_invoice(invoice_id,
                   user_id,
                   date_of_issue,
                   telephone,
                   email,
                   insurance_charge,
                   patient_charge,
                   discount,
                   penalty_charge)
    flash("Invoice Added Successfully")
    return redirect(url_for('get_admin_home_page'))


# this is our update route to modify an already existing employee
@app.route('/update_employee_admin/<user_id>/<address_id>/', methods = ['GET', 'POST'])
def update_employee_admin(user_id,address_id):

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

        up.update_employee_profile(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_number,
                       city, province, postal_code)
        flash("Event Updated Successfully")

        return redirect(url_for('get_admin_home_page'))


# this is our update route to modify an already existing employee
@app.route('/update_patient_admin/<user_id>/<address_id>/', methods = ['GET', 'POST'])
def update_patient_admin(user_id,address_id):

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

        up.update_patient(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_number,
                       city, province, postal_code)
        flash("Event Updated Successfully")

        return redirect(url_for('get_admin_home_page'))


# this is our update route to modify an already existing employee
@app.route('/update_invoice_admin/<invoice_id>/<user_id>/', methods = ['GET', 'POST'])
def update_invoice_admin(invoice_id, user_id):

    if request.method == 'POST':

        date_of_issue = request.form['date_of_issue']
        telephone = request.form['telephone']
        email = request.form['email']
        insurance_charge = request.form['insurance_charge']
        patient_charge = request.form['patient_charge']
        discount = request.form['discount']
        penalty_charge = request.form['penalty_charge']

        up.update_invoice(invoice_id, user_id, date_of_issue,
                          telephone, email, insurance_charge, patient_charge,
                          discount, penalty_charge)
        flash("Event Updated Successfully")

        return redirect(url_for('get_admin_home_page'))


# This route is for deleting a patient
@app.route('/delete_patient_admin/<user_id>/', methods = ['GET', 'POST'])
def delete_patient_admin(user_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_admin_home_page'))


# This route is for deleting a patient
@app.route('/delete_employee_admin/<user_id>/', methods = ['GET', 'POST'])
def delete_employee_admin(user_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Employee Deleted Successfully")

    return redirect(url_for('get_admin_home_page'))


# This route is for deleting a invoice
@app.route('/delete_invoice_admin/<invoice_id>/', methods = ['GET', 'POST'])
def delete_invoice_admin(invoice_id):
    delt.delete_invoice(invoice_id)
    flash("Patient Deleted Successfully")

    return redirect(url_for('get_admin_home_page'))


@app.route('/')
def show_all():
    conn = get_db_connection()
    # insert_patient('2', None, 'CAA')
    # insert_patient_chart(20)
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
