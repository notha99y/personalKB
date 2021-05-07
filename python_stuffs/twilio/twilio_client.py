from twilio.rest import Client
from secrets import *

class TwilioClient(object):
    def __init__(self):
        self.account_sid = account_sid 
        self.auth_token = auth_token
        
        self.whatsapp_number = whatsapp_number
        self.twilio_number = twilio_number
        
        self.client = Client(account_sid, auth_token)
        
    def test(self):
        message = self.client.messages.create(
                                    body ='Hello there !',
                                    from_= f"whatsapp:{twilio_number}",
                                    to = f"whatsapp:{whatsapp_number}"
                                )
        print(message.sid)

if __name__ == '__main__':
    twilio_client = TwilioClient()
    twilio_client.test()