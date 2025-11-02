import subprocess
import time
import smtplib
from email.mime.text import MIMEText
# import re


class DfMonitor:
    """Monitors running application"""

    def __init__(self, threshold, address):
        self.threshold = threshold
        self.email = address

    @staticmethod
    def _get_input():
        """run app, parses output"""
        value = 0
        df_output = subprocess.run(['df'], stdout=subprocess.PIPE)
        lst = df_output.stdout.decode().split('\n')
        for row in lst:
            try:
                if '/dev' in row.split()[-1]:
                    value = row.split()[-2].strip('%')
            except IndexError:
                continue
        return value

    def check_threshold(self):
        value = self._get_input()
        print(value)
        if int(value) > self.threshold:
            return value

    def send_notification(self):
        message = MIMEText("Threshold exceeded")
        message['Subject'] = 'Threshold exceeded'
        message['From'] = 'admin@localhost'
        message['To'] = self.email
        s = smtplib.SMTP('localhost')
        s.send(message)
        s.quit()


inst = DfMonitor(100, 'admin@example.com')
# inst.check_threshold()

while True:
    print('Checking...')
    if inst.check_threshold():
        inst.send_notification()
    print('Waiting 5 sec...')
    time.sleep(5)
