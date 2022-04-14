import random

from python.getters import get_invoice


def generateInvoiceId():
    n = random.randint(1,300000)
    invoice = get_invoice(int(n))
    while invoice:
        n = random.randint(1,300000)
        invoice = get_invoice(int(n))
    return n

