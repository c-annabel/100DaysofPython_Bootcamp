from tkinter import Y
from art import logo
#from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(list_cards, card_number):
    for i in range(card_number):
        list_cards.append(int(random.choice(cards)))

def calculate_score(list_cards):
    list_value = sum(list_cards)
    # if list_value == 21:
    #     list_value = 0
    
    if 11 in list_cards and list_value > 21:
        for i in range(len(list_cards)):
            if list_cards[i] == 11:
                list_cards[i] = 1
        #cards.remove(11)
        #cards.append(1)
        list_value = sum(list_cards)

    return list_value

def draw_cards(list_cards, computer_draw):
    draw_again = True
    while draw_again:
        draw_card = ''
        list_value = calculate_score(list_cards)
            
        if computer_draw == 'n':
            draw_card = input("If you want to draw another card? Type 'y' or 'n': \n")
        
        if draw_card == 'y' or \
            (computer_draw == 'y' and list_value < 17):
            deal_card(list_cards, 1)  
            list_value = calculate_score(list_cards)
            if list_value >= 21:
                draw_again = False
            print(f"===============================================================")
            print(f"Drawed cards are now: {list_cards}, score is {list_value}")
            print(f"===============================================================")
        else: draw_again = False
    return list_value

def compare(user_score, computer_score):
    
    if user_score > 21:
        print("Computer wins.")
    elif computer_score > 21:
        print("User wins.")
    elif computer_score == 21 and user_score == 21:
        print("Blackjack!")
    elif user_score == computer_score:
        print("It's a draw.")
    elif user_score == 21 or \
        (user_score > computer_score) :
        print("You win")
    elif computer_score == 21 or \
        (computer_score > user_score) :
        print("Computer wins")
      

def blackjack():  
    print(logo)

    computer_cards = []
    user_cards = []
    card_number = 2

    deal_card(computer_cards, card_number)
    deal_card(user_cards, card_number)
    computer_value = calculate_score(computer_cards)
    user_value = calculate_score(user_cards)    

    print(f"Computer's first card is: {computer_cards[0]}")
    print(f"User cards are: {user_cards}, score is {user_value}")
    print(f"===============================================================")

    if computer_value == 21 and user_value == 21:
        print("Blackjack!")
    elif computer_value == 21 or user_value > 21: print("Computer won!")
    elif user_value == 21 or computer_value > 21: print("You won!")
    else: 
        computer_draw = 'n'
        user_value = draw_cards(user_cards, computer_draw)
        if computer_value != 21 and computer_value < 17 and user_value <= 21: 
            computer_draw = 'y'
            computer_value = draw_cards(computer_cards, computer_draw)
        
        print(f"Computer cards are now: {computer_cards}, score is {computer_value}")
        print(f"User cards are now: {user_cards}, score is {user_value}")
        print(f"===============================================================")
        
        compare(user_value, computer_value)

play_again = True

while play_again:    
    blackjack() 
    end_of_game = input("Would you like to play again? Type 'y' or 'n': \n")

    if end_of_game == 'n':
        play_again = False
        print("End of the game. Goodbye!")
    else: 
        #clear()  #on replit
        print("Play again.")






