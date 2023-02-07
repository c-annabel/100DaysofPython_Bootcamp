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
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "PAR"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()


# if sheet_data[0]["iataCode"] == "":
count = 0
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        count += 1
if count > 0:
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for row in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        row["iataCode"],
        from_time = today,
        to_time = six_month_from_today
    )

    if flight != None:
        if flight.price < row["lowestPrice"]:
            notification_manager.send_sms(
                msg=f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.desti_city}-{flight.desti_airport}, from{flight.out_date} to {flight.return_date}."
            )

        row["lowestPrice"] = flight.price

data_manager.destination_data = sheet_data
data_manager.update_destination_prices()
