import os
import smtplib

EMAIL_ADDRESS = 'ENTEREMAILHERE'
EMAIL_PASSWORD = 'ENTERPASSWORDHERE'

def sendmail(reciver_address,subject,body):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        msg= f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS,reciver_address,msg)