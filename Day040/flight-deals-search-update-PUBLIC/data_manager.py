import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "PRICES SHEET"
SHEETY_USERS_ENDPOINT = "USERS SHEET"
APP_ID = "ID"
APP_KEY = "KEY"

class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(APP_ID, APP_KEY))
        data = sheet_response.json()
        self.destination_data = data["prices"]
        # pprint(self.sheet_data)
        return self.destination_data

    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(APP_ID, APP_KEY)
            )
            print(response.text)

    def update_destination_prices(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(APP_ID, APP_KEY)
            )
            response.raise_for_status()

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=(APP_ID, APP_KEY,))
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data