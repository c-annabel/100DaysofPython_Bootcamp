import smtplib
from twilio.rest import Client

TWILIO_SID = 'ID'
TWILIO_AUTH_TOKEN = 'TOKEN'
TWILIO_VIRTUAL_NUMBER = "FROM"
TWILIO_VERIFIED_NUMBER = "TO"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_= TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode("utf-8")
                )