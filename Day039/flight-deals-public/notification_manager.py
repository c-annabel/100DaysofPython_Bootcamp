from twilio.rest import Client

# Price/ Departure City Name/ Departure Airport IATA Code
# Arrival City Name/ Arrival Airport IATA Code
# Outbound Date/ Inbound Date

account_sid = 'id'
auth_token = 'token'

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_="fromTel",
            to='mobile'
        )
        print(message.status)