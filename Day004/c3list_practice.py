# # ====== EX2 Banker Roulette===============#
# import random 

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# random_number = random.randint(0, len(names)-1)
# random_name = names[random_number]

# print(f"{random_name} is going to buy the meal today!")

# Nested Lists =========================
fruits = ['a','b','c','d','e','f','g']
vege = [1,2,3,4,5,6]

dirty_dozen = [fruits, vege]
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

#  ====== EX3 Treasure Map===============#
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal=int(position[0])-1
vertical=int(position[1])-1

map[vertical][horizonal] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")