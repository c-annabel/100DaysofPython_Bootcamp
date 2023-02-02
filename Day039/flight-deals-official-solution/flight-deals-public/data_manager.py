import requests
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/cf470ebc7fa12ee20ae8d9a36453c92c/flightDeals/prices"
APP_KEY = "key"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def getSheetData(self):

        sheet_response = requests.get(url=sheet_endpoint, auth=("c-annabel", APP_KEY,))
        data = sheet_response.json()
        self.sheet_data = data["prices"]
        # pprint(self.sheet_data)
        return self.sheet_data

    def updateSheetData(self):

        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    "lowestPrice": city["lowestPrice"],
                }
            }

            response = requests.put(url=f"{sheet_endpoint}/{city['id']}", json=new_data, auth=("c-annabel", APP_KEY,))
            response.raise_for_status()
            # print(response.text)

# data_manager = DataManager()
# data_manager.getSheetData()