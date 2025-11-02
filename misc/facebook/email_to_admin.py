import smtplib
from email.mime.text import MIMEText


def send_email():
    message = MIMEText('Email content')
    message['Subject'] = 'The subject'
    message['From'] = 'myemail@localhost'
    message['To'] = 'admin@example.com'

    s = smtplib.SMTP('localhost')
    s.send(message)
    s.quit()

