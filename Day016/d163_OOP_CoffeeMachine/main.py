from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

nextCustomer = True
while nextCustomer:
    options = menu.get_items()
    coffee = input(f"What would you like? ({options}): ")
    if coffee == "off":
        nextCustomer = False
        break
    elif coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
