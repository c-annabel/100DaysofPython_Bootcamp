from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

# Generate random RGB colors
# Color RGB useful resource: https://www.w3schools.com/colors/colors_rgb.asp

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color


#documentation: https://docs.python.org/3/library/turtle.html
tim = Turtle()

#named color
colors = ["firebrick", "orange", "gold", "medium aquamarine", "dark green", "light blue", "medium blue", "blue violet"]
directions = [0, 90, 180, 270]
#tim.pensize(15) #set the size of the pen
tim.speed("fastest") #0-10, or fastest0 > fast10 > normal6 > slow3 > slowest1
tim.shape("turtle")
tim.color("red") #tkinterface, for GUI
#https://cs111.wellesley.edu/schedule#today



# Make a Spirograph
def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading((tim.heading() + size_of_gap))

draw_spirograph(5)

#---------------------------------------------------------#
def right100():
    tim.forward(100)
    tim.right(90)

def drawing():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Dashed square -----
# for i in range(4):
#     for _ in range(10):
#         drawing()
#     tim.right(90)

# Drawing different shapes:

# First try
# number_sides = 4
# for _ in range(6):
#     for i in range(x):
#         tim.forward(100)
#         tim.right(360/number_sides)
#     number_sides += 1'

# Second Try
# https://trinket.io/docs/colors


def drawShapes(number_sides):
   angle = 360/number_sides
   for _ in range(number_sides):
       tim.forward(100)
       tim.right(angle)


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     # or time.color(colors[shapes_side_n-3])
#     drawShapes(shape_side_n)




# Draw a Random Walk
# for _ in range(200):
#     #tim.color(random.choice(colors))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))







screen = Screen()
screen.exitonclick()