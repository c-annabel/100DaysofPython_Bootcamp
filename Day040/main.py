import requests


sheet_endpoint = "https://api.sheety.co/cf470ebc7fa12ee20ae8d9a36453c92c/flightDeals/users"
APP_KEY = "KEY"

class JoinTheClub:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, first_name, last_name, email, confirm_email):
        self.first_name = input("What is your first name?")
        self.last_name = input("What is your last name?")

        self.email = input("What is your email?")
        self.confirm_email = input("Type your email again.")

    def postSheetData(self):

        CLUB_PARAMS = {
            "query":
            "gender": 
        }

        response = requests.post(url=sheet_endpoint, json=CLUB_PARAMS)
        response.raise_for_status()
        result = response.json()
        print(result)


