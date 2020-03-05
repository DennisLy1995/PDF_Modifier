import re
import smtplib as smtp
from Tools.Utils import ask

def validate_single_email(email):
    pattern = '[^@]+@[^@]+\.[^@]+'
    if not re.match(pattern, email):
        return False
    else:
        return False


def sendEmail(attachment):
    print('New PDF sent by email.')
    checker = ask("""
Send PDF by email:
    1: YES
    2: NO
        """)
    if checker:
        email_account = input('To:')
        if validate_single_email(email_account):
            print('Email account is valid.')
        else:
            print('email account is not valid.')
    else:
        """Email not sent"""
