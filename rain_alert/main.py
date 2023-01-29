# API authentication: https://openweathermap.org/current#name
import requests

api_key = "23ba616de231f974cdd9[restkey]"

parameters = {
    "q": "Paris",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
#print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)

# http://jsonviewer.stack.hu = copy the result and paste to view
# {"coord":{"lon":2.3488,"lat":48.8534},
#  "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],
#  "base":"stations",
#  "main":{"temp":277.48,"feels_like":274.78,"temp_min":275.93,"temp_max":278.25,
#  "pressure":1028,"humidity":76},
#  "visibility":10000,"wind":{"speed":3.09,"deg":240},
#  "clouds":{"all":100},"dt":1675020015,"sys":{"type":2,
#  "id":2041230,"country":"FR","sunrise":1674977115,"sunset":1675010512},
#  "timezone":3600,"id":2988507,"name":"Paris","cod":200}


#https://openweathermap.org/api/one-call-api
#https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#https://www.latlong.net
#Subscription required

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": 48.58,
    "lon": 2,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response2 = requests.get(OWM_Endpoint, params=weather_params)
print(response2.status_code)
response2.raise_for_status()
data2 = response2.json()

#http://jsonviewer.stack.hu
#Doc of field content and codes
#https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
#ventusky.com: life weather
#slice function a[start:stop]

for x in range(0,12):
    if int(data2["hourly"][x]["weather"][0]["id"]) < 700:
        print("Bring an umbrella!")
        break

#Different way of data prepation:
will_rain = False
weather_slice = data2["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
#     print("Bring an umbrella")

#Twilio API for phone call and ordering and etc.

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = '[id]'
auth_token = '[token]'

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies={'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today, remember to bring an umbrella!",
        from_="+fromnumber",
        to='+desnumber'
    )
    print(message.status)
# print(message.sid)

#put online to schedule run.
#pythonanyway: https://www.pythonanywhere.com
#upload the file, open -> console -> run on python3 filename
#connection error: max retries exceeded with url = 443
#Set a task with command python3 main.py
#Daily 7am or current time
#convert UTC time to bst or local time

#when with environment variable
#on pythonanywhere, the command should be changed to:
#export Key=key; export Key2=key2; python3 main.py


#store secure info in the environment
#Terminal: env
#command: export OWM_API_KEY=[key] to store the value in environement variable.
#no space no quotes.
#in code: api_key = os.environ.get(OWM_API_KEY)


#apilist.fun