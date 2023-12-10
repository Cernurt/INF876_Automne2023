"""
Send email Python 3

Reference: https://realpython.com/python-send-email/#sending-your-plain-text-email
"""
import smtplib
import ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

config = configparser.ConfigParser()
config.read('config.ini')

smtp_server = config['smtp']['host']
port = 587  # For starttls
sender_email = config['smtp']['user']
password = config['smtp']['password']
receiver_email = config['buk']['recipient']

# Create the plain-text and HTML version of your message
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
text = """\
Hello world!
This is an HTML email test
"""
html = """\
<html>
  <body>
    <h1>Hello world!</h1>
    <p>This is an <strong>HTML</strong> email test</p>
  </body>
</html>
"""
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    print('authenticating..')
    server.login(sender_email, password)
    print('sending email...')
    server.sendmail(sender_email, receiver_email, message.as_string())
print('done')
