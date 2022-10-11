from random import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import sys

game = [rock,paper,scissors]

userInput = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))

if userInput >=3 or userInput < 0:
    print("You typed an invalid number!")
    sys.exit(1)

userChoice = game[userInput]
machineChoice = random.choice(game)
#it also works with: machineChoice = game[random.randint(0,2)]

print("User Choice: " + userChoice)
print("Machine Choice: " + machineChoice)

if (machineChoice == rock and userChoice == scissors) or \
    (machineChoice == scissors and userChoice == paper) or \
        (machineChoice == paper and userChoice == rock):
      print("Machine wins.")
else: print("You win!")

