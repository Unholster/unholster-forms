# -*- coding: utf-8 -*
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.mime.application import MIMEApplication
from os.path import basename
import smtplib

import settings


def send_email(form, contents, attachments=[]):
    msg = MIMEMultipart()
    msg['From'] = settings.FROM_EMAIL
    msg['Subject'] = form.get('subject', '')
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(contents))
    for f in attachments:
        with open(f, 'rb') as arch:
            part = MIMEApplication(arch.read(), Name=basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    smtp = smtplib.SMTP(
        host=settings.SMTP_SERVER,
        port=settings.SMTP_PORT,
        timeout=settings.DEFAULT_TIMEOUT)
    smtp.set_debuglevel(settings.DEFAULT_TIMEOUT)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(settings.AWS_USER, settings.AWS_PASSWORD)
    msg = msg.as_string()
    msg = msg.replace('text/plain', 'text/html')
    response = smtp.sendmail(settings.FROM_EMAIL, form.get('to', []), msg)
    smtp.close()
    return response
