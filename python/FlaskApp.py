import os
from datetime import date

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from python.deletions import delete_user, delete_treatment
from python.getters import get_all_users, get_last_address_id, get_all_addresses, get_user_with_id, get_user_with_email, \
    get_patient, get_employee, get_responsible_party, get_admin, get_insurance_claim, get_payment, get_invoice, \
    get_hygienist, get_receptionist, get_dentist, get_treatment
from python.inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_appointment, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_treatment, insert_review, insert_clinic_enterprise, insert_employee
from python.updaters import update_treatment, update_user
from python.validation import generateUserId, validateSSN, validateEmail, generateChartNo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'
app.secret_key = "Secret Key"

db = SQLAlchemy(app)


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

# @app.route('/')
# def getlogin():
#     return render_template('login.html')

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    user_id = request.form.get("userid")
    password = request.form.get("pwd")
    if request.method == 'POST':
        user = get_user_with_id(user_id)
        if not user: #user is empty list
            error = 'User id does not exist. Please try again.'
        elif password != user[0][11]:
            error = 'Password is wrong. Please try again.'
        else:
            #return redirect(url_for('home'))
            flash("Redirecting to home page.")

        # if (request.form['username'] != 'admin' or request.form['password'] != 'admin') or (request.form['username'] != 'admin' or request.form['password'] != 'admin'):
        #     error = 'Invalid Credentials. Please try again.'
        # else:
        #     return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=['POST'])
def signup():
    error = None
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

    print(first_name)
    print(middle_name)
    print(last_name)
    print(gender)
    print(insurance_company)
    print(ssn)
    print(email)
    print(dob)
    print(tel)
    print(age)
    print(password)
    retString = validateSSN(int(ssn))
    retVal = validateEmail(email)

    if(retString != "success"):
        error = retString
    if(retVal != "success"):
        error = retVal
    else:
        user_id = generateUserId()
        option = request.form['flexRadioDefault']
        insert_user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, dob, tel, age, password)
        if option == "patient":
            chart_no = generateChartNo()
            insert_patient_chart(chart_no)
            insert_patient(user_id, chart_no, insurance_company)
        if option == "dentist":
            insert_employee(user_id, None, "dentist", None, date.today().strftime("%Y-%m-%d"), None, 0)
            insert_dentist(user_id, None)
        if option == "hygienist":
            insert_employee(user_id, None, "hygienist", None, date.today().strftime("%Y-%m-%d"), None, 0)
            insert_hygienist(user_id, None)
        if option == "receptionist":
            insert_employee(user_id, None, "receptionist", None, date.today().strftime("%Y-%m-%d"), None, 0)
            insert_receptionist(user_id, None)

        flash("User Account Created Successfully")

    return render_template('login.html', error = error)

@app.route('/')
def show_all():
    conn = get_db_connection()

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
