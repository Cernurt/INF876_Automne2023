'''
WARNING: this is Python 2.x version

Simple script to test sending email using SMTP server
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# smtp config
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'user@gmail.com'
SMTP_PASS = 'password'

# email content
to = "yohanes.gultom@gmail.com"
subject = "Just a test mail"
body = "This is just a test message from a new server. Kindly ignore it and proceed with what you are doing. Thank you!"

if __name__ == '__main__':
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(SMTP_USER, to, msg.as_string())
    server.quit()