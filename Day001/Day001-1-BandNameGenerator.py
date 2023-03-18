# Write your code below this line 👇
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

#----------------------#
#Use of single and double quotes
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#----------------------#
#use of length function
name = input("What is your name?")
print(len(name))
# or print(len(input("What is your name?")))

# Thonny debugging tool

#-----------------------#
#Band-name-generator#
#1. Create a greeting for your program.
print("Hello! Welcome to the band name generator.")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grew up in? \n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of a pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end


