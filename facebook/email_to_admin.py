import smtplib
from email.mime.text import MIMEText


def send_email(file):
    with open(file) as f:
        msg = MIMEText(f.read())
        # Set message filename as a subject
        msg['Subject'] = locals()['message_file']
        msg['From'] = 'user@example.com'
        msg['To'] = 'user@example.com'

    # sending the message
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


message_file = 'message_file.txt'
send_email(message_file)