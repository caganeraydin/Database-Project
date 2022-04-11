import random

from getters import get_user_with_id, get_user_with_email, get_patient_chart


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