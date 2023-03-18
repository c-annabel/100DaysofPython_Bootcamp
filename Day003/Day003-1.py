#==========EX01===========#
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#==========EX02==BMI 2.0=========#
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height)**2)

m=" "
if BMI < 18.5:
    m = "are underweight."
elif BMI < 25:
    m = "have a normal weight."
elif BMI < 30:
    m = "are slightly overweight."
elif BMI < 35:
    m = "are obese."
else:
    m = "are clinically obese."

print(f"Your BMI is {BMI}, you {m}")

#==========EX03==Leap year=========#
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
m = "Not leap year."
if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
           m = "Leap year."
        
print(m)

#==========EX04==Pizza order program=========#
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
amt = 0

if size == "S":
   amt += 15
elif size == "M":
    amt += 20 
else:
    amt += 25

if add_pepperoni == "Y":
    if size == "S":
         amt += 2
    else:
         amt += 3

if extra_cheese == "Y":
    amt += 1

print(f"Your final bill is: ${amt}.")

#==========EX05==Love Calculator=========#
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()

t1 = name.count("t") + \
     name.count("r") + \
     name.count("u") + \
     name.count("e")

o1 = name.count("l") + \
     name.count("o") + \
     name.count("v") + \
     name.count("e")     

d1 = int(str(t1) + str(o1))

if d1 < 10 or d1 > 90:
    print(f"Your score is {d1}, you go together like coke and mentos.")
elif d1 >= 40 and d1 <= 50:
    print(f"Your score is {d1}, you are alright together.")
else:
    print(f"Your score is {d1}.")
