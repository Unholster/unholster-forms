'''
Created on Dec 22, 2016

@author: rtorres
'''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email.mime.application import MIMEApplication
from os.path import basename
import smtplib

AWS_USER = ''
AWS_PASSWORD = ''
SMTP_SERVER = 'email-smtp.us-west-2.amazonaws.com'
SMTP_PORT = '587'
FROM_EMAIL = ''
DEFAULT_TIMEOUT = 10
TO_EMAIL = []
ATTACH_FILE = 'unholster.jpg'


def sendMail(receipients, subject, email_content, files=[]):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = COMMASPACE.join(receipients)
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
        timeout=DEFAULT_TIMEOUT)
    smtp.set_debuglevel(DEFAULT_TIMEOUT)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(AWS_USER, AWS_PASSWORD)
    msg = msg.as_string()
    msg = msg.replace('text/plain', 'text/html')
    smtp.sendmail(FROM_EMAIL, receipients, msg)
    smtp.close()

if __name__ == "__main__":
    template_email = '<html><body>This is a text body. <strong>Foo bar.</strong></body></html>'
    sendMail(TO_EMAIL, 'Attached file email', template_email, [ATTACH_FILE])
