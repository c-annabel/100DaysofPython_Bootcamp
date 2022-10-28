from art import logo
from random import *

print(logo)

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

LEVEL_DICT = {'easy':5, 'hard':10}

target_num = randint(1,100)

guess_level = input("Choose the difficuly level: Type 'easy' or 'hard': ")
guess_turn = LEVEL_DICT[guess_level]
print(f"You have chosen the {guess_level} level, you have {guess_turn} times to guess. ")

guess_num = int(input("Guess a number between 1 and 100: "))
guess_turn -= 1

def compare(guess, target):
    end_of_guess = False
    if guess == target:
        print("You guess right!")
        print(f"The correct nubmer is {target}.")
        end_of_guess = True
    elif guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")

    return end_of_guess


def number_guess(guess_turn, guess_num):
    end_of_guess = False
    while end_of_guess == False:
        end_of_guess = compare(guess_num, target_num)

        if end_of_guess != True:
            if guess_turn != 0:
                print(f"You still have {guess_turn} times left to guess. ")
                guess_num = int(input("Make a guess again: "))
                guess_turn -= 1
            else:
                print(f"You have run out of guesses, you lose. ")
                end_of_guess = True
            
number_guess(guess_turn, guess_num)

