import os

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from python.getters import get_all_users
from python.inserters import insert_user

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

    # insert_user(1439,'kut','K.','sad','mail','some company',489489489,'email@smtn.this','1965-08-09','987-876-7665',55,'Aeatclassic!')
    cur = conn.cursor()

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
    users = get_all_users()
    # print(users)
    #  conn.commit()
    cur.close()
    conn.close()

    return render_template('show_all.html', Users=users)

# me = user('123','abc',None,'def','male','sunlife','123456789','gmail@hotmail.com','2020-03-29','888-999-7766','2','pasword')
# db.session.add(me)
# db.session.commit()
# db.create_all()
app.run()
