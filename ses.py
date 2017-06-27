from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email.mime.application import MIMEApplication

import settings
import smtplib

SMTP_USER = settings.SMTP_USER
SMTP_PASSWORD = settings.SMTP_PASSWORD
SMTP_SERVER = settings.SMTP_SERVER
SMTP_PORT = settings.SMTP_PORT
FROM_EMAIL = settings.FROM_EMAIL
SMTP_TIMEOUT = settings.SMTP_TIMEOUT


def send(recipients, subject, email_content, files=[]):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = COMMASPACE.join(recipients)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(email_content, _charset='utf-8'))

    for file in files:
        part = MIMEApplication(file.read(), Name=file.filename.encode('utf-8'))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(
            file.filename.encode('utf-8'),
        )

    smtp = smtplib.SMTP(
        host=SMTP_SERVER,
        port=SMTP_PORT,
        timeout=SMTP_TIMEOUT)
    smtp.set_debuglevel(SMTP_TIMEOUT)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    msg = msg.as_string()
    msg = msg.replace('text/plain', 'text/html')
    smtp.sendmail(FROM_EMAIL, recipients, msg)
    smtp.close()
