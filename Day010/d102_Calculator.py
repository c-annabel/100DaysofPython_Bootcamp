#Calculator
from art import logo
#from replit import clear

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
#watch out the float numbers
def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    end_loop=False
        
    for symbol in operations:
        print(symbol)

    while not end_loop:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer1 = calculation_function(num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer1}")
        num1 = answer1

        cal_stopper = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to start a new calculation: ")

        if cal_stopper == "n":
            end_loop = True
            #clear()
            calculator() #call function within a function

calculator()