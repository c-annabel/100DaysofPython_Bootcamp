# coffee moji: https://emojipedia.org/hot-beverage/
from math import ceil
import json

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

moneyChange = {
    "quaters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}


nextCustomer = True
resources["money"] = 0

def prResources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    print()

while nextCustomer: 

    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "off":
        nextCustomer = False
        break
    elif coffee == "report":
        prResources()
    else:
        insufficient = False
        for i in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                insufficient = True
        print()
        if not insufficient:
            monetaryValue = 0
            for i in moneyChange:
                qty = int(input(f"Please insert the quantity of {i}: "))
                monetaryValue += moneyChange[i] * qty
            if monetaryValue < MENU[coffee]["cost"]:
                print("Sorry that's not enough money. Money refunded. ")
                break
            else:
                print(json.dumps(resources, indent=2))
                resources["money"] += MENU[coffee]["cost"]
                for i in MENU[coffee]["ingredients"]:
                    resources[i] -= MENU[coffee]["ingredients"][i]
                returnChange = monetaryValue - MENU[coffee]["cost"]
                print()
                print(f"Here is your {coffee}. Enjoy!")
                print(f"Here is ${returnChange:.2f} dollars in change")
                print()
                print(json.dumps(resources, indent=2))
