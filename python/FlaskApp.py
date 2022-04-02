import os

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error

from python.deletions import delete_user,deleteTreatment
from python.getters import get_all_users, get_last_address_id, get_all_addresses, get_user_with_id, get_user_with_email, \
    get_patient, get_employee, get_responsible_party, get_admin, get_insurance_claim, get_payment, get_invoice, \
    get_hygienist, get_receptionist, get_dentist, get_treatment, get_all_treatments
from python.inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_appointment, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_review, insert_clinic_enterprise, insertTreatment
from python.updaters import updateTreatment

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'

db = SQLAlchemy(app)

#Treatments
@app.route('/')
def get_treatments():
    all_treatment = get_all_treatments()
    return render_template("treatment.html", Treatments = all_treatment)

#this route is for inserting a new treatment to postgres database via html
@app.route('/insert_treatment', methods = ['POST'])
def insert_treatment():

    # if request.method == 'POST':

    treatment_id = request.form['treatment_id']
    dentist_id = request.form['dentist_id']
    chart_no = request.form['chart_no']
    appointment_type = request.form['appointment_type']
    treatment_type = request.form['treatment_type']
    medication = request.form['medication']
    symptoms = request.form['symptoms']
    tooth = request.form['tooth']
    comments = request.form['comments']

    print(treatment_id)
    print(dentist_id)
    print(chart_no)
    print(appointment_type)
    print(treatment_type)
    print(medication)
    print(symptoms)
    print(tooth)
    print(comments)

    # treatment = Treatment(treatment_id, dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)
    #
    #
    # db.session.add(treatment)
    # db.session.commit()
    insertTreatment(dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)

    flash("Treatment Inserted Successfully")

    return redirect(url_for('get_treatments'))


#this is our update route to modify an already existing treatment
@app.route('/update_treatment', methods = ['GET', 'POST'])
def update_treatment():

    if request.method == 'POST':
        # treatment = Treatment.query.get(treatment_id)

        treatment_id = request.form['treatment_id']
        dentist_id =request.form['dentist_id']
        chart_no = request.form['chart_no']
        appointment_type = request.form['appointment_type']
        treatment_type = request.form['treatment_type']
        medication = request.form['medication']
        symptoms = request.form['symptoms']
        tooth = request.form['tooth']
        comments = request.form['comments']

        # db.session.commit()
        updateTreatment(treatment_id, dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)
        flash("Event Updated Successfully")

        return redirect(url_for('get_treatments'))


#This route is for deleting a treatment
@app.route('/delete_treatment/<treatment_id>/', methods = ['GET', 'POST'])
def delete_treatment(treatment_id):
    # treatment = Treatment.query.get(treatment_id)

    # db.session.delete(treatment)
    # db.session.commit()
    deleteTreatment(treatment_id)
    flash("Treatment Deleted Successfully")

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
