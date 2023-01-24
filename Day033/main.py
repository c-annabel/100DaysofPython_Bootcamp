#Application Programming Interfaces (APIs)
# APIs is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an
# external system. (an interface)
# https://en.wikipedia.org/wiki/API

# JSON viewer awesome APP will help to view JSON file more clearly.

import requests #needed to install
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json") #International Space Station Current Location"

# requests module https://docs.python-requests.org/en/latest/

# Status code: https://www.webfx.com/web-development/glossary/http-status-codes/
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("Unauthorized.")
# print(response)
# print(response.status_code)

#Second way!!! :
response.raise_for_status() #raise the status code and detailed error

# data= response.json()["iss_position"]["longitude"] #key or #actual further key
# print(data)

# 2nd way:
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(data)
print(longitude)
print(latitude)

iss_position = (longitude, latitude)
print(iss_position)
# Reverse Geocoding Convert: https://www.latlong.net/Show-Latitude-Longitude.html

#quick sort - 1XX: HOld On/ 2XX:Here you go/ 3XX: Go Away/ 4XX: You screwed Up/ 5XX: Server Screwed up

# ------------------------------------------------------------------------------------------
# Sunrise Sunset API: https://sunrise-sunset.org/api
# Find current Lat & Lon : https://www.latlong.net

MY_LAT = 48.856613
MY_LONG = 2.352222

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2 = response2.json()
#Latitude: 48.856613; Longitude: 2.352222
print(data2)

time_now = dt.datetime.now()
print(time_now.hour)

sunrise = data2["results"]["sunrise"]
sunset = data2["results"]["sunset"]

#split() # String split(): https://www.w3schools.com/python/ref_string_split.asp
print(sunrise.split("T")[1].split(":")[0]) #24 hour clock.
print(sunset)

#formatted function