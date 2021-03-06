import os


from datetime import date
import random
import datetime

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from deletions import *
from getters import *
from inserters import *
from updaters import *
from validation import *

import updaters as up
import inserters as ins
import deletions as delt
from appointment_procedure_options import procedure_dict


app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'
app.secret_key = "Secret Key"


db = SQLAlchemy(app)
current_employee = None


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    user_id = request.form.get("userid")
    password = request.form.get("pwd")
    all_branches = get_all_branches()
    if request.method == 'POST':
        user = get_user_with_email(user_id)
        if not user: #user is empty list
            error = 'Email entered does not exist. Please try again.'
        elif password != user[0][11]:
            error = 'Password is wrong. Please try again.'
        else:
            if user_id == 'admin@admin.com':
                print("admin here")
                return redirect(url_for('get_admin_home_page'))
            elif get_employee(get_user_with_email(user_id)[0][0]):
                return redirect(url_for('get_employee_home_page', user_id = get_user_with_email(user_id)[0][0]))
            elif get_patient(get_user_with_email(user_id)[0][0]):
                return redirect(url_for('get_patient_home_page',user_id = get_user_with_email(user_id)[0][0]))
                #flash("Redirecting to patient page.")
            else:
                flash("User is neither a patient, employee or admin", "danger")

        # if (request.form['username'] != 'admin' or request.form['password'] != 'admin') or (request.form['username'] != 'admin' or request.form['password'] != 'admin'):
        #     error = 'Invalid Credentials. Please try again.'
        # else:
        #     return redirect(url_for('home'))
    return render_template('login.html', error=error, List_of_all_branches = all_branches)

@app.route('/signup', methods=['POST'])
def signup():
    error = None
    emp_type = ""
    first_name = request.form['fname']
    middle_name = request.form['mname']
    last_name = request.form['lname']
    gender = request.form['gender']
    insurance_company = request.form['insurance_company']
    ssn = request.form['ssn']
    email = request.form['email']
    dob = request.form['dob']
    tel = request.form['telephone']
    age = request.form['age']
    password = request.form['password']
    print(password)

    if request.form['flexRadioRole'] != "patient":
        branch_id = request.form['branch_id']
        emp_type = request.form['flexRadioType']

        print(branch_id)

    retString = validateSSN(int(ssn))
    retVal = validateEmail(email)

    if(retString != "success"):
        error = retString
    if(retVal != "success"):
        error = retVal
    else:
        user_id = generateUserId()
        role = request.form['flexRadioRole']
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, dob, tel, age, password)
        if role == "patient":
                chart_no = generateChartNo()
                insert_patient_chart(chart_no)
                ins.insert_patient(user_id, chart_no, insurance_company)
                a = insert_address(None,None,None,None,None)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
        if emp_type == "part-time":
            if role == "dentist":
                insert_employee(user_id, branch_id, 'part-time', 'Dentist', date.today().strftime("%Y-%m-%d"), None, 0)
                insert_dentist(user_id, None)
                a = insert_address(None,None,None,None,None)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "hygienist":
                insert_employee(user_id, branch_id, 'part-time', 'Hygienist', date.today().strftime("%Y-%m-%d"), None, 0)
                insert_hygienist(user_id, None)
                a = insert_address(None,None,None,None,None)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "receptionist":
                if checkTwoReceptionistsPerBranch(int(branch_id)):
                    insert_employee(user_id, branch_id, 'part-time', 'Receptionist', date.today().strftime("%Y-%m-%d"), None, 0)
                    insert_receptionist(user_id, None)
                    a = insert_address(None,None,None,None,None)
                    insert_user_address(user_id, a[0][0])
                    flash("User Account Created Successfully", "success")
                else:
                    flash("This branch already has two receptionists!", "danger")
        if emp_type == "full-time":
            if role == "dentist":
                insert_employee(user_id, branch_id, "full-time", 'Dentist', date.today().strftime("%Y-%m-%d"), None, 0)
                insert_dentist(user_id, None)
                a = insert_address(None,None,None,None,None)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "hygienist":
                insert_employee(user_id, branch_id, "full-time", 'Hygienist', date.today().strftime("%Y-%m-%d"), None, 0)
                insert_hygienist(user_id, None)
                a = insert_address(None,None,None,None,None)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "receptionist":
                if checkTwoReceptionistsPerBranch(int(branch_id)):
                    insert_employee(user_id, branch_id, "full-time", 'Receptionist', date.today().strftime("%Y-%m-%d"), None, 0)
                    insert_receptionist(user_id, None)
                    a = insert_address(None,None,None,None,None)
                    insert_user_address(user_id, a[0][0])
                    flash("User Account Created Successfully", "success")
                else:
                    flash("This branch already has two receptionists!", "danger")


    return render_template('login.html', error = error)


# Employee Home Page
@app.route('/employee_home/<user_id>/')
def get_employee_home_page(user_id):

    print(get_employee(user_id))
    all_patients = get_all_patients()
    all_appointments = get_all_appointments()
    all_invoices = get_all_invoices()
    cur_employee = get_employee(user_id)[0]
    cur_emp_user_info = get_user_with_id(user_id)[0]
    cur_employee_address = get_user_address(user_id)
    if not cur_employee_address:
        a = insert_address(None,None,None,None,None)
        insert_user_address(user_id, a[0][0])
        cur_employee_address = get_user_address(user_id)

    return render_template("employee_home.html", Patients = all_patients, Appointments = all_appointments, Invoices = all_invoices, employee = cur_employee, emp_profile = cur_emp_user_info, emp_address = cur_employee_address[0])



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

    all_branches = get_all_branches()
    appointments = get_all_appointments_patient(user_id)


    return render_template("patient_home.html", user_id=user_id, first_name=first_name, middle_name=middle_name, last_name=last_name,
                           gender=gender, insurance_company=insurance_company, ssn=ssn, birth_date=birth_date,
                           phone_number=phone_number, email=email, age=age, password=password, appointments=appointments, invoices=invoices,responsible_party=responsible_party,List_of_all_branches = all_branches)




@app.route('/get_appointmens_page/<user_id>')
def get_appointments_page(user_id):

    dentists = get_all_dentists()
    list_of_dentist_names = []
    for x in dentists:
        user = get_user_with_id(x[0])
        list_of_dentist_names.append(user[0]+(x[1],))

    return render_template("patient_appointment.html", user_id=user_id, List_of_all_dentists=list_of_dentist_names)


@app.route('/insert_appointment_patient/<user_id>', methods=['POST'])
def insert_appointment_patient(user_id):

    # if request.method == 'POST':

    invoice_id = generateInvoiceId()
    print(invoice_id)

    dentist_id = request.form['dentist_id']
    print(dentist_id)
    start_time = request.form['start_time']
    print(start_time)
    string_time = str(start_time)
    start_hour = string_time[0] + string_time[1]
    print(start_hour)
    start_minutes = string_time[3] + string_time[4]
    print(start_minutes)
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
    status = "New"

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

        insert_invoice(invoice_id, user_id, date_of_appointment,user[0][9], user[0][7], 0, procedure[3]*1.1, "0", "0", False)
        appointment = insertAppointment(invoice_id, user_id, dentist_id, start_time, str(final_end_time), appointment_type, status, "", date_of_appointment)
        procedure_no = insert_appointment_procedure(appointment_type, appointment[0][0], 1)

        insert_fee_charge(invoice_id, int(procedure_no[0][0]), procedure[0], procedure[3])
        flash("Appointment Inserted Successfully", "success")
        return redirect(url_for('get_patient_home_page',user_id=user_id))




@app.route('/update_patient/<user_id>/<address_id>/<emp_id>/', methods=['GET', 'POST'])
def update_patient(user_id, address_id, emp_id):
    print(current_employee)
    if request.method == 'POST':

        print(user_id + ", " + address_id)

        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        insurance_type = request.form['insurance_type']
        insurance_company = request.form['insurance_company']
        ssn = request.form['ssn']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        telephone = request.form['telephone']
        age = request.form['age']
        password = request.form['password']
        house_number = request.form['house_number']
        street_name = request.form['street_name']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']

        up.update_patient(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_name,
                       city, province, postal_code,insurance_type,user_id)
        flash("Event Updated Successfully", "success")
        return redirect(url_for('get_employee_home_page', user_id=emp_id))


@app.route('/insert_responsible_party/<user_id>', methods=['POST'])
def insert_responsible_party(user_id):

    resp_id = generateUserId()

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

    flash("Reponsible Party Added Successfully", "success")
    return redirect(url_for('get_patient_home_page', user_id=user_id))

# this route is for inserting a new treatment to postgres database via html
@app.route('/insert_patient/<emp_id>', methods=['POST'])
def insert_patient(emp_id):


    user_id = generateUserId()
    chart_no = generateChartNo()

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
    street_name = request.form['street_name']
    city = request.form['city']
    province = request.form['province']
    postal_code = request.form['postal_code']

    if get_user_with_email(email):
        flash("account with the email address you entered already exists, please try again.", "danger")
    else:
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        address_id = insert_address(house_number, street_name, city, province, postal_code)[0]
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        ins.insert_user_address(user_id, address_id)
        flash("Patient Added Successfully", "success")

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



    flash("Event Updated Successfully", "success")
    return redirect(url_for('get_patient_home_page', user_id=user_id))


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
        street_name = request.form['street_name']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']
        if house_number == "None":
            house_number = "0"
        up.update_employee_profile(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_name,
                       city, province, postal_code)
        flash("Event Updated Successfully", "success")

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
        flash("Event Updated Successfully", "success")

        return redirect(url_for('get_employee_home_page', user_id = emp_id))


# This route is for deleting a patient
@app.route('/delete_patient/<user_id>/<emp_id>/', methods=['GET', 'POST'])
def delete_patient(user_id, emp_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Patient Deleted Successfully", "success")

    return redirect(url_for('get_employee_home_page', user_id=emp_id))


# This route is for deleting a invoice
@app.route('/delete_invoice/<invoice_id>/<emp_id>/', methods=['GET', 'POST'])
def delete_invoice(invoice_id, emp_id):
    delt.delete_invoice(invoice_id)
    flash("Patient Deleted Successfully", "success")

    return redirect(url_for('get_employee_home_page', user_id=emp_id))

# Payment
@app.route('/get_invoices/<user_id>/')
def get_invoices(user_id):
    patient_invoice = get_user_invoice(user_id)
    return render_template("payment.html", PatientInvoice = patient_invoice)

@app.route('/insert_user_payment/<user_id>/<invoice_id>/', methods = ['POST'])
def insert_user_payment(user_id, invoice_id):
    print("LOL")
    print(user_id)
    print(invoice_id)
    payment_method = request.form['payment_method']
    print(payment_method)
    insurance_amount = request.form['insurance_amount']
    print(insurance_amount)
    patient_amount = get_invoice(invoice_id)[0][6]
    print(patient_amount)

    insert_payment(int(invoice_id), payment_method, int(patient_amount), int(insurance_amount))
    update_invoice_payment(invoice_id, insurance_amount, True)

    flash("Payment is saved successfully!", "success")
    return redirect(url_for('get_invoices',user_id = user_id))


@app.route('/leave_review/<patient_id>/', methods=['GET','POST'])
def leave_review(patient_id):
    print("hi")
    all_branches = get_all_branches()
    print(all_branches)
    branch_id = request.form['branch_id']
    print(branch_id)
    if not get_branch(branch_id):
        flash("Branch Id does not exist please select a value from dropdown.","danger")
        return render_template('login.html', List_of_all_branches = all_branches)

    professionalism = request.form['professionalism']
    print(professionalism)
    communication = request.form['communication']
    print(communication)
    cleanliness = request.form['cleanliness']
    print(cleanliness)
    value = request.form['value']
    print(value)
    insert_review(patient_id, branch_id, professionalism, communication, cleanliness, value)
    print("success")
    flash("Your Review Is Saved Successfully", "success")
    return render_template('login.html')


# Admin
@app.route('/admin_home/')
def get_admin_home_page():
    branches = get_all_branches()
    patients = get_all_patients()
    employees = get_all_employees()
    invoices = get_all_invoices()
    appointments = get_all_appointments()
    return render_template("admin_home.html",
                           Patients = patients,
                           Employees = employees,
                           Invoices = invoices,
                           Appointments = appointments,
                           Branches = branches)


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_patient_admin/', methods = ['POST'])
def insert_patient_admin():


    user_id = generateUserId()
    chart_no = generateChartNo()

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
    street_name = request.form['street_name']
    print(street_name)
    city = request.form['city']
    print(city)
    province = request.form['province']
    print(province)
    postal_code = request.form['postal_code']
    print(postal_code)

    if get_user_with_email(email):
        flash("account with the email address you entered already exists, please try again.", "danger")
        return redirect(url_for('get_admin_home_page'))
    else:
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        address_id = insert_address(house_number, street_name, city, province, postal_code)[0]
        insert_patient_chart(chart_no)
        ins.insert_patient(user_id, chart_no, insurance_type)
        ins.insert_user_address(user_id, address_id)
        flash("Patient Added Successfully", "success")
        return redirect(url_for('get_admin_home_page'))


# this route is for inserting a new patient to postgres database via html
@app.route('/insert_employee_admin/', methods = ['POST'])
def insert_employee_admin():

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
    street_name = request.form['street_name']
    city = request.form['city']
    province = request.form['province']
    postal_code = request.form['postal_code']
    branch_id = request.form['branch_id']
    salary = request.form['salary']
    years_of_experience = request.form['years_of_experience']

    if get_user_with_email(email):
        flash("account with the email address you entered already exists, please try again.", "danger")
        return redirect(url_for('get_admin_home_page'))
    else:
        user_id = generateUserId()
        role = request.form['flexRadioRole']
        emp_type = request.form['flexRadioType']
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)
        if emp_type == "part-time":
            if role == "dentist":
                insert_employee(user_id, branch_id, 'part-time', 'Dentist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                insert_dentist(user_id, None)
                a = insert_address(house_number,street_name,city,province,postal_code)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "hygienist":
                insert_employee(user_id, branch_id, 'part-time', 'Hygienist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                insert_hygienist(user_id, None)
                a = insert_address(house_number,street_name,city,province,postal_code)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "receptionist":
                if checkTwoReceptionistsPerBranch(int(branch_id)):
                    insert_employee(user_id, branch_id, 'part-time', 'Receptionist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                    insert_receptionist(user_id, None)
                    a = insert_address(house_number,street_name,city,province,postal_code)
                    insert_user_address(user_id, a[0][0])
                    flash("User Account Created Successfully", "success")
                else:
                    flash("This branch already has two receptionists!", "danger")
        if emp_type == "full-time":
            if role == "dentist":
                insert_employee(user_id, branch_id, "full-time", 'Dentist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                insert_dentist(user_id, None)
                a = insert_address(house_number,street_name,city,province,postal_code)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "hygienist":
                insert_employee(user_id, branch_id, "full-time", 'Hygienist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                insert_hygienist(user_id, None)
                a = insert_address(house_number,street_name,city,province,postal_code)
                insert_user_address(user_id, a[0][0])
                flash("User Account Created Successfully", "success")
            if role == "receptionist":
                if checkTwoReceptionistsPerBranch(int(branch_id)):
                    insert_employee(user_id, branch_id, "full-time", 'Receptionist', date.today().strftime("%Y-%m-%d"), salary, years_of_experience)
                    insert_receptionist(user_id, None)
                    a = insert_address(house_number,street_name,city,province,postal_code)
                    insert_user_address(user_id, a[0][0])
                    flash("User Account Created Successfully", "success")
                else:
                    flash("This branch already has two receptionists!", "danger")

        return redirect(url_for('get_admin_home_page'))



# this route is for inserting a new patient to postgres database via html
@app.route('/insert_employee_admin/<user_id>', methods = ['POST'])
def insert_invoice_admin(user_id):

    invoice_id = generateInvoiceId()

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
    flash("Invoice Added Successfully", "success")
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
        street_name = request.form['street_name']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']

        up.update_employee_profile(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_name,
                       city, province, postal_code)
        flash("Event Updated Successfully", "success")

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
        insurance_type = request.form['insurance_type']
        insurance_company = request.form['insurance_company']
        ssn = request.form['ssn']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        telephone = request.form['telephone']
        age = request.form['age']
        password = request.form['password']
        house_number = request.form['house_number']
        street_name = request.form['street_name']
        city = request.form['city']
        province = request.form['province']
        postal_code = request.form['postal_code']

        up.update_patient(user_id, first_name, middle_name, last_name,gender,
                       insurance_company, ssn, email, date_of_birth, telephone,
                       age, password, address_id, house_number, street_name,
                       city, province, postal_code,insurance_type,user_id)
        flash("Event Updated Successfully", "success")

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
        flash("Event Updated Successfully", "success")

        return redirect(url_for('get_admin_home_page'))


# This route is for deleting a patient
@app.route('/delete_patient_admin/<user_id>/', methods = ['GET', 'POST'])
def delete_patient_admin(user_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Patient Deleted Successfully", "success")

    return redirect(url_for('get_admin_home_page'))


# This route is for deleting a patient
@app.route('/delete_employee_admin/<user_id>/', methods = ['GET', 'POST'])
def delete_employee_admin(user_id):
    print(user_id)
    delt.delete_user(user_id)
    flash("Employee Deleted Successfully", "success")

    return redirect(url_for('get_admin_home_page'))


# This route is for deleting a invoice
@app.route('/delete_invoice_admin/<invoice_id>/', methods = ['GET', 'POST'])
def delete_invoice_admin(invoice_id):
    delt.delete_invoice(invoice_id)
    flash("Patient Deleted Successfully", "success")

    return redirect(url_for('get_admin_home_page'))
    print("LOL")
    payment_method = request.form['payment_method']
    print(payment_method)
    insurance_amount = request.form['insurance_amount']
    print(insurance_amount)
    patient_amount = get_invoice(invoice_id)[0][6]
    print(patient_amount)

    insert_payment(int(invoice_id), payment_method, int(patient_amount), int(insurance_amount))
    get_all_appointments(invoice_id, insurance_amount, True)

    flash("Payment is saved successfully!","success")
    return redirect(url_for('get_invoices',user_id = user_id))

#Appointments
@app.route('/get_appointments', methods=['GET'])
def get_appointments():
    all_appointments = get_all_appointments_allcolumns()
    #Get dentists names on the dropdown menu on the appointment page
    List_of_all_patients = get_all_Patients()
    print(List_of_all_patients)
    list_of_dentists = get_all_dentists()
    list_of_dentist_names = []
    for x in list_of_dentists:
        user = get_user_with_id(x[0])
        list_of_dentist_names.append(user[0]+(x[1],))


    return render_template("appointments.html", Appointments=all_appointments, List_of_all_dentists=list_of_dentist_names,
                           List_of_all_patients_names = List_of_all_patients)


# this route is for inserting a new appointment to postgres database via html
@app.route('/insert_appointment', methods=['POST'])
def insert_appointment():

    # if request.method == 'POST':

    invoice_id = generateInvoiceId()
    print(invoice_id)
    patient_id = request.form['patient_id']
    print(patient_id)
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
    room_assigned = request.form['room_assigned']
    print(room_assigned)
    date_of_appointment = request.form['date_of_appointment']
    print(date_of_appointment)

    if not (get_dentist(dentist_id)):
        print("here1")
        flash("Dentist Id you entered does not exist, please try again.", "danger")
        return redirect(url_for('get_appointments'))
    if not (get_patient(patient_id)):
        print("here3")
        flash("Patient Id you entered does not exist, please try again.", "danger")
        return redirect(url_for('get_appointments'))
    if get_start_time(start_time):
        print("here4")
        flash("The time you entered is not available, please choose another time.", "danger")
        return redirect(url_for('get_appointments'))
    else:
        print("here6")
        user = get_user_with_id(get_patient(patient_id)[0][0])
        procedure = procedure_dict[str(appointment_type)]

        insert_invoice(invoice_id, patient_id, date_of_appointment,user[0][9], user[0][7], 0, procedure[3]*1.1, "0", "0", False)
        appointment = insertAppointment(invoice_id, patient_id, dentist_id, start_time, str(final_end_time), appointment_type, status, room_assigned, date_of_appointment)
        procedure_no = insert_appointment_procedure(appointment_type, appointment[0][0], 1)
        insert_fee_charge(invoice_id, int(procedure_no[0][0]), procedure[0], procedure[3])

        flash("Appointment Inserted Successfully", "success")
        return redirect(url_for('get_appointments'))




# this is our update route to modify an already existing appointment
@app.route('/update_appointment/<appointment_id>/', methods=['GET', 'POST'])
def update_appointment(appointment_id):
    if request.method == 'POST':

        invoice_id = get_appointment(appointment_id)[0][1]
        print(invoice_id)
        patient_id = request.form['patient_id']
        print(patient_id)
        dentist_id = request.form['dentist_id']
        print(dentist_id)
        start_time = request.form['start_time']
        print(start_time)
        end_time = request.form['end_time']
        print(end_time)
        appointment_type = request.form['appointment_type']
        print(appointment_type)
        status = request.form['status']
        print(status)
        room_assigned = request.form['room_assigned']
        print(room_assigned)
        date_of_appointment = request.form['date_of_appointment']
        print(date_of_appointment)

        if not (get_patient(patient_id)):
            print("Patient id is not found in the db")
            flash("Patient Id you entered does not exist, please try again.", "danger")
            return redirect(url_for('get_appointments'))
        if not (get_dentist(dentist_id)):
            print("Dentist id is not found in the db")
            flash("Dentist Id you entered does not exist, please try again.", "danger")
            return redirect(url_for('get_appointments'))

        #validate start time then end time here
        ########
        ########

        if not (appointment_type in procedure_dict):
            flash("Please pick a procedure from the given list.", "danger")
            return redirect(url_for('get_appointments'))

        #validate date of appointment here
        ########
        ########

        updateAppointment(appointment_id, invoice_id, patient_id, dentist_id, start_time, end_time, appointment_type,
                          status, room_assigned, date_of_appointment)
        flash("Event Updated Successfully", "success")

        return redirect(url_for('get_appointments'))



# This route is for deleting an appointment
@app.route('/delete_appointment/<appointment_id>/', methods=['GET', 'POST'])
def delete_appointment(appointment_id):
    print(appointment_id)
    deleteAppointment(appointment_id)
    flash("Appointment Deleted Successfully", "success")

    return redirect(url_for('get_appointments'))

#Treatments
@app.route('/get_treatments')
def get_treatments():
    all_treatment = get_all_treatments()
    return render_template("treatment.html", Treatments = all_treatment)

#this route is for inserting a new treatment to postgres database via html
@app.route('/insert_treatment', methods = ['POST'])
def insert_treatment():

    # if request.method == 'POST':

    dentist_id = request.form['dentist_id']
    chart_no = request.form['chart_no']
    appointment_type = request.form['appointment_type']
    treatment_type = request.form['treatment_type']
    medication = request.form['medication']
    symptoms = request.form['symptoms']
    tooth = request.form['tooth']
    comments = request.form['comments']

    print(dentist_id)
    print(chart_no)
    print(appointment_type)
    print(treatment_type)
    print(medication)
    print(symptoms)
    print(tooth)
    print(comments)

    if(not (get_patient_chart(chart_no))):
        print("here1")
        flash("Chart No you entered does not exist, please try again.", "danger")
        return redirect(url_for('get_treatments'))
    if(not (get_dentist(dentist_id))):
        print("here2")
        flash("Dentist Id you entered does not exist, please try again.","danger")
        return redirect(url_for('get_treatments'))
    else:
        print("here3")
        insertTreatment(dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)
        flash("Treatment Inserted Successfully", "success")
        return redirect(url_for('get_treatments'))


#this is our update route to modify an already existing treatment
@app.route('/update_treatment/<treatment_id>/', methods = ['GET', 'POST'])
def update_treatment(treatment_id):

    if request.method == 'POST':

        dentist_id = request.form['dentist_id']
        chart_no = request.form['chart_no']
        appointment_type = request.form['appointment_type']
        treatment_type = request.form['treatment_type']
        medication = request.form['medication']
        symptoms = request.form['symptoms']
        tooth = request.form['tooth']
        comments = request.form['comments']

        if(not (get_dentist(dentist_id))):
            flash("Dentist Id you entered does not exist, please try again.","danger")
            return redirect(url_for('get_treatments'))
        if(not (get_patient_chart(chart_no))):
            flash("Chart No you entered does not exist, please try again.","danger")
            return redirect(url_for('get_treatments'))

        updateTreatment(treatment_id, dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)
        flash("Event Updated Successfully", "success")

        return redirect(url_for('get_treatments'))


#This route is for deleting a treatment
@app.route('/delete_treatment/<treatment_id>/', methods = ['GET', 'POST'])
def delete_treatment(treatment_id):
    print(treatment_id)
    deleteTreatment(treatment_id)
    flash("Treatment Deleted Successfully", "success")

    return redirect(url_for('get_treatments'))

@app.route('/')
def show_all():
    users = get_all_users()
    return render_template('show_all.html', Users=users)


# me = user('123','abc',None,'def','male','sunlife','123456789','gmail@hotmail.com','2020-03-29','888-999-7766','2','pasword')
# db.session.add(me)
# db.session.commit()
# db.create_all()


app.run()
