#POST/PUT(update)/DELETE
#Pixela: https://pixe.la
# Step1: Set up a user account
# curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}
# Step2: Create a graph
#$ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'
# {"message":"Success.","isSuccess":true}
# Step3: Get the graph
#Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API.
# Step4: Post value to the graph
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'
# {"message":"Success.","isSuccess":true}

import requests
from datetime import datetime

USERNAME = "USERNAME"
TOKEN = "TOKEN"
GRAPH_ID = "GRAPHID"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

# USER_PARAMS = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# Marked after the account created.
# response = requests.post(url=pixela_endpoint, json=USER_PARAMS)
# print(response.text) #issue/report
# response.raise_for_status()
# #https://pixe.la/@c-annabel

#================================================================================#

# #Create graph successfully: https://pixe.la/v1/users/c-annabel/graphs/GRAPH_ID.html
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "name",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora",
#     "timezone": "CET",
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_resp.text) #{"message":"Success.","isSuccess":true}

#================================================================================#

#https://www.w3schools.com/python/python_datetime.asp
# today = datetime.now()
#Also can specify a date: today = datetime(year=2020, month=7, day=23)
# today = datetime(year=2023, month=1, day=29)
#
# formatted_today= today.strftime("%Y%m%d")
#
# graph_pixel_config = {
#     "date": formatted_today,
#     "quantity": "0.5",
##can be written as:
##    "quantity": input("How many kilometers did you cycle today? "),
# }
#
# graph_id_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# graph_pixel = requests.post(url=graph_id_endpoint, json=graph_pixel_config, headers=headers)
# print(graph_pixel.text) #{"message":"Success.","isSuccess":true}

#================================================================================#

#Put: Update data
# today = datetime(year=2023, month=1, day=29)
# formatted_today= today.strftime("%Y%m%d")
#
# graph_pixel_config = {
#     "quantity": "1",
# }
#
# graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
# graph_pixel = requests.put(url=graph_put_endpoint, json=graph_pixel_config, headers=headers)
# print(graph_pixel.text) #{"message":"Success.","isSuccess":true}

#================================================================================#

#DETELE: delete data
# today = datetime(year=2023, month=1, day=29)
# formatted_today= today.strftime("%Y%m%d")
#
# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
# graph_pixel = requests.delete(url=graph_delete_endpoint, headers=headers)
# print(graph_pixel.text) #{"message":"Success.","isSuccess":true}