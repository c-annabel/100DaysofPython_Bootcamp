import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "KEY"



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # DATE_FROM = input("Type the departure date (dd/mm/yyyy): ")
    # DATE_TO = input("Type the return date (dd/mm/yyyy): ")

    def get_destination_code(self, city_name):
        # code = "TESTING"
        # return code
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        # response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            try:
                query["max_stopovers"] = 1
                response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
                data = response.json()["data"][0]
                print(data)
            except IndexError:
                print(f"No indirect flights found for {destination_city_code} too. ")
                return None


        flight_data = FlightData(
            price=data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport = data["route"][0]["flyFrom"],
            desti_city = data["route"][0]["cityTo"],
            desti_airport = data["route"][0]["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.desti_city}: EUR{flight_data.price}")
        return flight_data

