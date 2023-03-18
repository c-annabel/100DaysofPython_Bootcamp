print("Hello"[0])  #subscript

#----------EX01---------------------#
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = int(two_digit_number[0]) 
b = int(two_digit_number[1])

print(str(a) + ' + ' + str(b) + ' = ' + str(a+b))
print(a+b)

#----------EX02---------------------#
#Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight) / (float(height)**2)
print(int(BMI))

#----------EX03---------------------#
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left = 90 - int(age)
z = left * 12
y = left * 52
x = left * 365

print("You have " + str(x) + " days, " + str(y) + " weeks, " + \
       "and " + str(z) + " months left.")
#f-string
print(f"You have {x} days, {y} weeks, and {z} months left.")
      

# ------ Main Program: ---------- #
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# FAQ: How to round to 2 decimal places?
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")