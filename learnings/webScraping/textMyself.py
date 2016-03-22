accountSID = 'AC73aacf03c9c0230703dfef95324e3177'
authToken = '17266ee172823aecb906deabe8c46698'
twilioNumber = '+13864563322'
myNumber = str(input("Enter phone no. : "))
from twilio.rest import TwilioRestClient
def textmyself(message):
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)