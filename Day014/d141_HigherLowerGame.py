from ast import keyword
from art import logo, vs
from game_data import data 
#from replit import clear
import random 

selected = {}
compare = {}
score = 0
print(logo)

def display_person(person_num, guess_al):
    selected[person_num] = random.choice(data)
    print (f"Compare {guess_al}: {selected[person_num]['name']}, a {selected[person_num]['description']}, from {selected[person_num]['country']}. ")
    compare[guess_al] = int(selected[person_num]['follower_count'])
    # print(compare) #test


def higher_lower():
    global compare
    global score

    print(vs)
    person = 2
    guess = 'B'
    display_person(person, guess)

    guess_option = input("Who has more followers? Type 'A' or 'B': ")

    #clear()
    print(logo)

    if (guess_option == 'A' and (compare[guess_option] > compare['B'])) or \
        (guess_option == 'B' and (compare[guess_option] > compare['A'])):
        score += 1
        print(f"You're right! Current score: {score}")
        # if guess_option == 'A' and (compare[guess_option] > compare['B']):
        #     person_num = 1
        #     print (f"Compare {guess_option}: {selected[person_num]['name']}, a {selected[person_num]['description']}, from {selected[person_num]['country']}. ")
        if guess_option == 'B' and (compare[guess_option] > compare['A']):
            selected[1] = selected[2]
            compare['A'] = compare['B']
            selected.popitem()
            print(selected)
        person_num = 1
        print (f"Compare {guess_option}: {selected[person_num]['name']}, a {selected[person_num]['description']}, from {selected[person_num]['country']}. ")
    else: 
        global final_game
        final_game = True
        print(f"Sorry, that's wrong. Final score: {score}.")
    
    return final_game

person = 1
guess = 'A'
display_person(person, guess)

final_game = False
while not final_game:
    higher_lower()




