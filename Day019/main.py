from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html#turtle.listen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    # also can use below
    tim.left(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.right(new_heading)

def clear():
    tim.clear()  # clear the drawing
    tim.penup()
    tim.home() # move the turtle to the origin
    tim.pendown()

def key_listener(key_type, fun_name, event):
    event(key=key_type, fun=fun_name)

# Etch-A-Sketch App
# W=Forwards, S=Backwards, A=Counter-Clockwise, D=Clockwise, C=Clear

screen.listen()
key_listener("w", move_forwards, screen.onkey)
key_listener("s", move_backwards, screen.onkey)
key_listener("a", turn_left, screen.onkey)
key_listener("d", turn_right, screen.onkey)
key_listener("c", clear, screen.onkey)
screen.exitonclick()


#screen.onkey(key="space", fun=move_forwards)