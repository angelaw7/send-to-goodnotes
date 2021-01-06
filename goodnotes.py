import smtplib
import os
import re

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    server.starttls()
    email_address = 'example@email.com'
    goodnotes_email = 'example@goodnotes.email'
    password = 'password'
    server.login(email_address, password)

    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = goodnotes_email
    message['Subject'] = "Goodnotes PDF"

    message.attach(MIMEText('Sent from Python', 'plain'))

    directory = 'directory path'  # e.g. 'D:/Downloads/Goodnotes'

    for file in [f for f in os.listdir(directory) if re.search('.pdf', f)]:

        with open(file, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), 'pdf')

        part.add_header('Content-Disposition', 'attachment', filename=file)

        message.attach(part)
        os.remove(file)

    server.sendmail(message['From'], message['To'], message.as_string())

    print("PDFs sent.")
    server.quit()


send_email()
