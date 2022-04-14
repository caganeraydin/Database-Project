import os

import datetime
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
    get_all_appointments, get_appointment, get_all_payments, get_all_dentists, get_start_time, get_patient_charge, \
    get_user_invoice,get_all_Patients
from inserters import insert_user, insert_appointment_procedure, insert_address, insert_user_address_latest, \
    insert_patient, insert_patient_chart, insert_branch, insert_branch_address, insert_invoice, insert_payment, \
    insert_insurance_claim, insert_fee_charge, insert_receptionist, insert_dentist, \
    insert_hygienist, insert_review, insert_clinic_enterprise, insertTreatment, insertAppointment
from updaters import updateTreatment, updateAppointment, update_invoice
from validation import generateInvoiceId

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_database'

db = SQLAlchemy(app)

@app.route('/')
def show_all():
    users = get_all_users()
    return render_template('show_all.html', Users=users)

# Payment
@app.route('/get_invoices/<user_id>/')
def get_invoices(user_id):
    patient_invoice = get_user_invoice(user_id)
    return render_template("payment.html", PatientInvoice = patient_invoice)

@app.route('/insert_payment/<user_id>/<invoice_id>/', methods = ['POST'])
def insert_user_payment(user_id, invoice_id):

    print("LOL")
    payment_method = request.form['payment_method']
    print(payment_method)
    insurance_amount = request.form['insurance_amount']
    print(insurance_amount)
    patient_amount = get_invoice(invoice_id)[0][6]
    print(patient_amount)

    insert_payment(int(invoice_id), payment_method, int(patient_amount), int(insurance_amount))
    update_invoice(invoice_id, insurance_amount, True)

    flash("Payment is saved successfully!","success")
    return redirect(url_for('get_invoices',user_id = user_id))

#Appointments
@app.route('/')
def get_appointments():
    all_appointments = get_all_appointments()
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

        insert_invoice(invoice_id, patient_id, date_of_appointment,user[0][9], user[0][7], 0, procedure[3], None, None, False)
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




# me = user('123','abc',None,'def','male','sunlife','123456789','gmail@hotmail.com','2020-03-29','888-999-7766','2','pasword')
# db.session.add(me)
# db.session.commit()
# db.create_all()
app.run()
