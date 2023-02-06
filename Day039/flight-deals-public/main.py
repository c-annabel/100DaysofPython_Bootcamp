#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#KAYAK flight ticket website
# Google Sheet Data Management - https://sheety.co/
# Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
# Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
# https://api.tequila.kiwi.com/v2
# Twilio SMS API - https://www.twilio.com/docs/sms

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.getSheetData()

flight_search = FlightSearch()
notification = NotificationManager()

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"Sheet Data: {sheet_data}")

    data_manager.sheet_data = sheet_data
    data_manager.updateSheetData()

for row in sheet_data:
    flight = flight_search.get_search_data(row["iataCode"])

    if flight != None and flight.price < row["lowestPrice"]:
        notification.send_sms(
            msg=f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.desti_city}-{flight.desti_airport}, from{flight.out_date} to {flight.return_date}."
        )

    if flight != None:
        row["lowestPrice"] = flight.price
        data_manager.sheet_data = sheet_data
        data_manager.updateSheetData()
