from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "PAR"

count=0
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        count += 1
if count > 0:
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]:{
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    }   for data in sheet_data
}

tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time = tomorrow,
        to_time = six_month_from_today
    )

    if flight != None:
        if flight.price < destinations[destination_code]["price"]:
            users = data_manager.get_customer_emails()
            emails = [row["email"] for row in users]
            names = [row["firstName"] for row in users]

            msg = f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.desti_city}-{flight.desti_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"

            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.desti_airport}.{flight.out_date}*{flight.desti_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_emails(emails, msg, link)

            # RESET WHEN NEW LOWEST PRICE EXISTS
            sheet_id = int(destinations[destination_code]["id"]) - 2
            sheet_data[sheet_id]["lowestPrice"] = flight.price


data_manager.destination_data = sheet_data
data_manager.update_destination_prices()
