#Dictionary Comprehension

#syntax1: new_dict = {new_key:new_value for item in list}
#syntax2: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Catherine', 'Dave', 'Eleanor', 'Freddie']
import random

students_score = {student:random.randint(1,100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score > 60}
print(passed_students)

#Practice 01
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Write your code below:
list1 = list(sentence.split(" "))
result = {word:len(word) for word in list1}
print(result)

#Practice 02
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {
day:(temp_c * 9/5 + 32) for (day,temp_c) in weather_c.items()
}

print(weather_f)

