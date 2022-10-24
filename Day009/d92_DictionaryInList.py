#Nesting Dictionary in a Dictionary
travel_log1 = {
    "France":{"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany":{"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
}

# Nesting Dictionary in a List
travel_log2 = [
    {"country":"France", "cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country":"Germany", "cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
]

# Exercise starts ================

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_input, visits_input, cities_list):
    new_country={}
    new_country["country"]=country_input
    new_country["visits"]=visits_input
    new_country["cities"]=cities_list
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)