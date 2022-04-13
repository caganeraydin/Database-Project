import os

import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import Error
from sqlalchemy import false

from appointment_procedure_options import procedure_dict
from deletions import delete_user, deleteTreatment, deleteAppointment
from getters import get_all_users, get_last_address_id, get_all_addresses, get_user_with_id, get_user_with_email, \
    get_patient, get_employee, get_responsible_party, get_admin, get_insurance_claim, get_payment, get_invoice, \
    get_hygienist, get_receptionist, get_dentist, get_treatment, get_all_treatments, get_patient_chart, \
    get_all_appointments, get_appointment, get_all_payments, get_all_dentists, get_start_time, get_patient_charge
from inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_review, insert_clinic_enterprise, insertTreatment, insertAppointment
from updaters import updateTreatment, updateAppointment
from validation import generateInvoiceId

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'

db = SQLAlchemy(app)


#Appointments
@app.route('/')
def get_appointments():
    all_appointments = get_all_appointments()

    #Get dentists names on the dropdown menu on the appointment page
    list_of_dentists = get_all_dentists()
    return render_template("appointments.html", Appointments=all_appointments, List_of_all_dentists=list_of_dentists)

# Payment
@app.route('/')
def get_payment_amount():
    patient_amount = get_all_payments()
    return render_template("payment.html", PatientAmount=patient_amount)


# Treatments
@app.route('/')
def get_treatments():
    all_treatment = get_all_treatments()
    return render_template("treatment.html", Treatments=all_treatment)


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
    #end_time = request.form['end_time']
    appointment_type = request.form['appointment_type']
    print(appointment_type)
    status = request.form['status']
    print(status)
    room_assigned = request.form['room_assigned']
    print(room_assigned)
    date_of_appointment = request.form['date_of_appointment']
    print(date_of_appointment)

    if not (get_dentist(dentist_id)):
        print("here1")
        flash("Dentist Id you entered does not exist, please try again.")
        return redirect(url_for('get_appointments'))
    if not (get_patient(patient_id)):
        print("here3")
        flash("Patient Id you entered does not exist, please try again.")
        return redirect(url_for('get_appointments'))
    if get_start_time(start_time):
        print("here4")
        flash("The time you entered is not available, please choose another time.")
        return redirect(url_for('get_appointments'))
    else:
        print("here6")
        user = get_user_with_id(get_patient(patient_id)[0][0])
        procedure = procedure_dict[str(appointment_type)]
        print(procedure)
        insert_invoice(invoice_id, patient_id, date_of_appointment,user[0][9], user[0][7], 0, procedure[3], None, None)

        appointment = insertAppointment(invoice_id, patient_id, dentist_id, start_time, "15:00:00", appointment_type, status, room_assigned, date_of_appointment)
        print(appointment)
        print("here!!")
        procedure_no = insert_appointment_procedure(appointment_type, appointment[0][0], 1)
        print(procedure_no)
        print(procedure[0])
        print(procedure[3])
        print(procedure_no[0][0])
        insert_fee_charge(invoice_id, int(procedure_no[0][0]), procedure[0], procedure[3])
        flash("Appointment Inserted Successfully")
        return redirect(url_for('get_appointments'))


# this route is for inserting a new treatment to postgres database via html
@app.route('/insert_treatment', methods=['POST'])
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

    if not (get_patient_chart(chart_no)):
        print("here1")
        flash("Chart No you entered does not exist, please try again.")
        return redirect(url_for('get_treatments'))
    if not (get_dentist(dentist_id)):
        print("here2")
        flash("Dentist Id you entered does not exist, please try again.")
        return redirect(url_for('get_treatments'))
    else:
        print("here3")
        insertTreatment(dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms, tooth, comments)
        flash("Treatment Inserted Successfully")
        return redirect(url_for('get_treatments'))


# this is our update route to modify an already existing appointment
@app.route('/update_appointment/<appointment_id>/', methods=['GET', 'POST'])
def update_appointment(appointment_id):
    if request.method == 'POST':
        appointment_id = request.form['appointment_id']
        invoice_id = request.form['invoice_id']
        patient_id = request.form['patient_id']
        dentist_id = request.form['dentist_id']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        appointment_type = request.form['appointment_type']
        status = request.form['status']
        room_assigned = request.form['room_assigned']
        date_of_appointment = request.form['date_of_appointment']

        updateAppointment(appointment_id, invoice_id, patient_id, dentist_id, start_time, end_time, appointment_type,
                          status, room_assigned, date_of_appointment)
        flash("Event Updated Successfully")

        return redirect(url_for('get_appointments'))


# this is our update route to modify an already existing treatment
@app.route('/update_treatment/<treatment_id>/', methods=['GET', 'POST'])
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

        updateTreatment(dentist_id, chart_no, appointment_type, treatment_type, medication, symptoms,
                        tooth, comments, treatment_id)
        flash("Event Updated Successfully")

        return redirect(url_for('get_treatments'))


# This route is for deleting an appointment
@app.route('/delete_appointment/<appointment_id>/', methods=['GET', 'POST'])
def delete_appointment(appointment_id):
    print(appointment_id)
    deleteAppointment(appointment_id)
    flash("Appointment Deleted Successfully")

    return redirect(url_for('get_appointments'))


# This route is for deleting a treatment
@app.route('/delete_treatment/<treatment_id>/', methods=['GET', 'POST'])
def delete_treatment(treatment_id):
    print(treatment_id)
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
