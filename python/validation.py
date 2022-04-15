import random
from getters import *


def generateUserId():
    n = random.randint(1,300000)
    user = get_user_with_id(str(n))
    while user:
        n = random.randint(1,300000)
        user = get_user_with_id(str(n))
    return n

def validateSSN(ssn):
    if (not (isinstance(ssn, int))) or (not 99999999 <ssn< 1000000000):
        return "SSN must be 9-digit integer"
    else:
        return "success"

def validateEmail(email):
    user = get_user_with_email(email)
    if user:
        return "This email address is registered under a different user, please enter another email"
    else:
        return "success"

def generateChartNo():
    n = random.randint(1,300000)
    chart = get_patient_chart(str(n))
    while chart:
        n = random.randint(1,300000)
        chart = get_patient_chart(str(n))
    return n

def generateInvoiceId():
    n = random.randint(1,300000)
    invoice = get_invoice(int(n))
    while invoice:
        n = random.randint(1,300000)
        invoice = get_invoice(int(n))
    return n

def checkTwoReceptionistsPerBranch(branch_id: int):
    receptionists = get_all_receptionist()
    counter = 0
    for receptionist in receptionists:
        if receptionist[1] == branch_id:
            counter += 1
            if counter >= 2:
                return False
    return True



