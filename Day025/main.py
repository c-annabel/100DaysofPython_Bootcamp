# READ CSV FILES
#CSV Common Separated Value
#Pandas doc: https://pandas.pydata.org/docs/
#Pandas API: https://pandas.pydata.org/docs/reference/index.html

# SOLUTION 01
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# SOLUTION 02
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

#SOLUTION 03
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"]) #first row is the name of the column
# print(data)
# print(type(data)) #pandas.core.frame.DataFrame = whole table
# print(type(data["temp"])) #Series = Columns

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].tolist()
# print(temp_list)
# print(len(temp_list))
#
# # Conventional way
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean()) #AVERAGE
# print(data["temp"].max()) #MAX VALUE
#
# #get data in columns:
# print(data["condition"])
# print(data.condition) #Column name is seen as attribute. Same as using square brackets

#Get Data in Row, by specifying a condition
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
# Revert to F
monday_temp_F = monday_temp * 9/5 + 32
print(monday.condition)
print(monday_temp_F)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)


