import smtplib
import os
import re

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from config import *

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    server.starttls()
    server.login(my_email, my_password)

    message = MIMEMultipart()
    message['From'] = my_email
    message['To'] = goodnotes_email
    message['Subject'] = "Goodnotes PDF"

    for file in [f for f in os.listdir(directory) if re.search('.pdf', f)]:

        with open(file, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), 'pdf')

        part.add_header('Content-Disposition', 'attachment', filename=file)

        message.attach(part)
        os.remove(file)

    server.sendmail(message['From'], message['To'], message.as_string())

    print("PDF(s) sent.")
    server.quit()

send_email()
