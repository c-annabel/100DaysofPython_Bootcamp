# Unlimited (positional) args (*args)

def add(*args):
    for n in args:
        print(n)


def add2(*args):
    print(args[2])
    adding_sum = 0
    for n in args:
        adding_sum += n
    return adding_sum


print(add2(1, 3, 5, 6, 8))


# Unlimited Keyword arguments:
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["multiply"])
    for key, value in kwargs.items():
        print(key)
        print(value)
    print('\n')
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # ALso use the below method "get"
        # if the arg didn't offer, wont have error message.
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
