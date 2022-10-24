#helpers:
#Thonny
#pythontutor.com

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bid_dict = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  # {"Angela":123, "James":323}
  highest_bid = 0
  winner_bidder = ""
  for bidder in bid_dict:
    bid_amount = bid_dict[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner_bidder = bidder
  print(f"The winner is {winner_bidder} with a bid of ${highest_bid}")
      

while not bidding_finished:
  name = input("What is your name? \n")
  price = int(input("What is your bid? $\n"))
  
  bid_dict[name] = price
  
  should_continue = input("Are there any other users? Type 'yes' or 'no': \n")

  if should_continue == "no":
     bidding_finished = True
     find_highest_bidder(bid_dict)
  elif should_continue == "yes":
     clear()