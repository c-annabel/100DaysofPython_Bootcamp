import requests
from datetime import datetime, timedelta
from flight_data import FlightData

kiwi_endpoint = "https://api.tequila.kiwi.com"
# kiwi_endpoint = "https://tequila-api.kiwi.com"
HEADER_PARAMS = {
    "apikey": "key",
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    # DATE_FROM = input("Type the departure date (dd/mm/yyyy): ")
    # DATE_TO = input("Type the return date (dd/mm/yyyy): ")

    def get_destination_code(self, city_name):
        # code = "TESTING"
        # return code

        kiwi_params = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(url=f"{kiwi_endpoint}/locations/query", params=kiwi_params, headers=HEADER_PARAMS)
        response.raise_for_status()
        results = response.json()['locations']
        code = results[0]["code"]
        return code

    def get_search_data(self, city_code):
        today = datetime.now().strftime("%d/%m/%Y")
        six_month = datetime.now() + timedelta(days=(6*30))  # 6*30days
        six_month = six_month.strftime("%d/%m/%Y")

        search_params = {
            "fly_from": "PAR",
            "fry_to": city_code,
            "date_from": today,
            "date_to": six_month,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(url=f"{kiwi_endpoint}/v2/search", headers=HEADER_PARAMS, params=search_params)
        # response.raise_for_status()
        try:
            results = response.json()["data"]
        except IndexError:
            print(f"No flights found for {city_code}.")
            return None

        for city in results:
            if city['route'][0]['cityCodeTo'] == city_code:
                flight_data = FlightData(
                    price=city["price"],
                    origin_city = city["route"][0]["cityFrom"],
                    origin_airport = city["route"][0]["flyFrom"],
                    desti_city = city["route"][0]["cityTo"],
                    desti_airport = city["route"][0]["flyTo"],
                    out_date = city["route"][0]["local_departure"].split("T")[0],
                    return_date = city["route"][1]["local_departure"].split("T")[0]
                )
                min_price = city["price"]
                print(f"{city['route'][0]['cityTo']}: EUR{min_price}")
                return flight_data

