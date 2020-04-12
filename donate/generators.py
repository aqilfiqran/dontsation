from django.core.mail import send_mail
from .models import Donate
from django.urls import reverse
import string
import random


def generateCode(length=100):
    asciChar = string.ascii_letters + string.ascii_uppercase + \
        string.ascii_lowercase + string.digits
    return ''.join(random.choice(asciChar) for i in range(1, length))


def sendVerification(email, code):
    send_mail('Code Verifikasi Donasi Anda',
              f'Ini merupakan code verifikasi donasi anda : {code}',
              'donstation53@gmail.com',
              [email],
              )


def isCheck(code):
    try:
        donator = Donate.objects.get(barcode=code)
        donator.confirmation = 1
        donator.save()
        return True
    except Donate.DoesNotExist:
        pass
    return False
