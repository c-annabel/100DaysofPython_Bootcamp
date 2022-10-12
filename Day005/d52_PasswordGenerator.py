#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
codes1 = ""
for i in range(nr_letters):
    codes1 += random.choice(letters)
for i in range(nr_symbols):
    codes1 += random.choice(symbols)
for i in range(nr_numbers):
    codes1 += random.choice(numbers)
print(codes1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
codes2 = []
for i in range(nr_letters):
    codes2.append(random.choice(letters))
for i in range(nr_symbols):
    codes2.append(random.choice(symbols))
for i in range(nr_numbers):
    codes2.append(random.choice(numbers))

random.shuffle(codes2)

hardcode=""
for i in codes2:
    hardcode += i
print("Your password is: " + hardcode)