from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email.mime.application import MIMEApplication
from os.path import basename
import settings
import smtplib

AWS_USER = settings.AWS_USER
AWS_PASSWORD = settings.AWS_PASSWORD
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
    msg.attach(MIMEText(email_content))
    for f in files:
        with open(f, 'rb') as arch:
            part = MIMEApplication(arch.read(), Name=basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    smtp = smtplib.SMTP(
        host=SMTP_SERVER,
        port=SMTP_PORT,
        timeout=SMTP_TIMEOUT)
    smtp.set_debuglevel(SMTP_TIMEOUT)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(AWS_USER, AWS_PASSWORD)
    msg = msg.as_string()
    msg = msg.replace('text/plain', 'text/html')
    smtp.sendmail(FROM_EMAIL, recipients, msg)
    smtp.close()
