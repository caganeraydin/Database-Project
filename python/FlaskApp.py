import os

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from python.deletions import delete_user
from python.getters import get_all_users, get_last_address_id, get_all_addresses, get_user_with_id, get_user_with_email
from python.inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_appointment, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_treatment, insert_review, insert_clinic_enterprise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'

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


    def __init__(self, user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password):

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



@app.route('/')
def show_all():



    conn = get_db_connection()
    #insert_patient('2', None, 'CAA')
    #insert_patient_chart(20)
    #delete_user('edaefault@mail.com')
    #insert_branch(1234, 1, '123')
    #insert_branch_address(1, 1)
    #insert_appointment(123,1,'1','101','13:00','13:30','tooth_removal','tbd','C121','2020-10-10')
    #insert_fee_charge(3, 1, 1,'23', 50)
    #insert_receptionist('123', '12')
    #insert_dentist('123', '12')
    #insert_hygienist('123', '12')
    #insert_invoice(123, '1', '2002-10-10', '12', '12', 1,1,1,1)
    #insert_payment(13,123,'lol', 10, 10)
    #insert_insurance_claim(4,3,10)
    #insert_user_address_latest('1439')
    #insert_user('1439','kut','K.','sad','mail','some company',489489489,'email@smtn.this','1965-08-09','987-876-7665',55,'Aeatclassic!')
    #insert_appointment_procedure('Root Canal',1, 4, 6)
    #insert_address(2, 2,'gat','qc','adf')
    #insert_treatment('101',122,'test','test','test','test','test','test')
    #insert_review('1', 1, 1,1,1, 1)
    insert_clinic_enterprise('2020-12-12')



    #print(get_last_address_id())


    # try:
    #     cur = conn.cursor()
    #     with open(get_abs_filepath_from_module(__file__, 'queries/insert_user.sql'), 'r') as file:
    #         cur.execute(file.read(),
    #                        (145,'kut','K.','sad','mail','some company',489489489,'email@smtn.this','1965-08-09','987-876-7665',55,'Aeatclassic!'))
    #         conn.commit()
    #
    # except Exception as error:
    #     raise Error('ERROR') from error
    # print(conn)
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM project_schema."user";')
    # # cur.execute('INSERT INTO project_schema.user(user_id, first_name, middle_name, last_name, gender, insurance_company, ssn, email, date_of_birth, telephone, age, password)'
    # #         'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    # #         (145,'kut','K.','sad','mail','some company',489489489,'email@smtn.this','1965-08-09','987-876-7665',55,'Aeatclassic!'))
    # users = cur.fetchall()
    #delete_user('666', 'default@mail.com')

    cur = conn.cursor()
    users = get_all_users()

    # print(users)
    #  conn.commit()
    print(get_user_with_email('default@mail.com'))
    cur.close()
    conn.close()

    return render_template('show_all.html', Users=users)

# me = user('123','abc',None,'def','male','sunlife','123456789','gmail@hotmail.com','2020-03-29','888-999-7766','2','pasword')
# db.session.add(me)
# db.session.commit()
# db.create_all()
app.run()
