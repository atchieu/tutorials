"""
textme.py - Provides a function that texts myself using my Twilio credentials.
"""

# Account information
account_sid = 'ACdca1bf69192ecf86b677a83b99c145ec'
auth_token = '473704f1e8877a404c46c49ba1297213'
my_number = '+13109261956'
twilio_number = '+14242537789'

from twilio.rest import TwilioRestClient

def textme(message):
    twilio_cli = TwilioRestClient(account_sid, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)

