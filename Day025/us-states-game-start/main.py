import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()


    #If answer_state is one of the states in all the states of the 50_states.csv
        #If they got it right:
            #create a turtle to write the name of the state at the state's x and y coordinates
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))  #Ensure it's integer for coordinates
        t.write(answer_state)   #Also works with << t.write(state_data.state.item()) >> #run the element only

#Click to get coordinate
# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() #Keeping the screen open

# screen.exitonclick()