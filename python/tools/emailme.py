"""
emailme.py - Provides a function that emails myself using Gmail.
"""

# Account information
username = 'atchieu'

import smtplib
import getpass

def emailme(subject, body):
    passwd = getpass.getpass()
    email_addr = username + '@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, passwd)
    message = 'From: {}\nSubject: (From emailme.py) {}\n\n{}'.format(email_addr, subject, body)
    server.sendmail(email_addr, email_addr, message)
    server.quit()

