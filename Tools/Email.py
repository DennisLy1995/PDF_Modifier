import re
import smtplib
from Tools.Utils import ask
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def validate_single_email(email):
    """Validate the email account has the email format properly configured."""
    pattern = '[^@]+@[^@]+\.[^@]+'
    if not re.match(pattern, email):
        return False
    else:
        return True


def validate_multiple_emails(emails):
    """Validate the format of multiple emails delimiter by a ;"""
    list_emails = emails.split(';')
    new_emails = ''
    for email in list_emails:
        if validate_single_email(email):
            new_emails = new_emails + email + ';'
    return remove_character_first_last_position(';', new_emails)


def remove_character_first_last_position(c, st):
    """Check if the string has a special character at the end or beginning, in order to remove it."""
    if st.endswith(';'):
        st = "".join(st[:-1])
    if st.startswith(';'):
        st = "".join(st[1:])
    return st


def sendEmail(attachment, file_name):
    """Send email with attachment."""
    print('New PDF sent by email.')
    checker = ask("""
Send PDF by email:
    1: YES
    2: NO
        """)
    if checker:
        email_account = input('To:')
        if validate_multiple_emails(email_account) != '':
            try:
                server = open_connection_GMAIL()
                gmail_config = read_gmail_account('C:\\Users\\BT917DM\\Desktop\\Email.txt')
                server.login(gmail_config[0], gmail_config[1])
                text = define_email_content(attachment, gmail_config[0], email_account, file_name).as_string()
                server.sendmail(gmail_config[0], email_account, text)
                print('Your email has been sent.')
            except Exception as e:
                print(f'ERROR: {e}')
            finally:
                server.quit()
                print('INFO: Connection with GMAIL closed4.')
        else:
            print('WARN: email account is not valid.')
    else:
        """Email not sent"""


def open_connection_GMAIL():
    """Method created to open the SMTP connection to GMAIL using the port 587."""
    try:
        print('INFO: Opening the connection with Gmail...')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # ...send emails
        print('INFO: Connection opened.')
        return server
    except:
        print('WARN: Something went wrong connection with GMAIL...')
        return None


def read_gmail_account(path):
    file = open(path, 'r')
    return file.read().split(';')


def define_email_content(attachment_path, from_email, to_email, file_name):
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = """Thanks for using our tool, to manipulate your PDFs.

Best regards.

"""
    attach_file = open(attachment_path, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header(file_name, 'attachment')
    message.attach(payload)
    return message
