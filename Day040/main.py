import requests

sheet_endpoint = "https://api.sheety.co/cf470ebc7fa12ee20ae8d9a36453c92c/flightDeals/users"
APP_KEY = "89396f0f4a72b374d7e58613cf7f54a9"
HEADER = "Yy1hbm5hYmVsOjg5Mzk2ZjBmNGE3MmIzNzRkN2U1ODYxM2NmN2Y1NGE5"


class Users:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def postSheetData(self):

        user_params = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
            }
        }

        print(user_params)
        response = requests.post(url=sheet_endpoint, json=user_params, auth=("c-annabel", APP_KEY,))
        print(response.text)

first_name = input("What is your first name?")
last_name = input("What is your last name?")

email = ""
email_check = False
while not email_check:
    email = input("What is your email: ")
    confirm_email = input("Type your email again: ")
    if email == confirm_email:
        email_check = True
    else:
        print("Email confirmation failed, please confirm your email and enter again.")

users = Users(first_name, last_name, email)
users.postSheetData()
