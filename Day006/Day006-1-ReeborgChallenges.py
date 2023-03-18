# LINK AS BELOW:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Hurdles race 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        hurdle()
    elif front_is_clear():
        move()  

#Hurdles race 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
       turn_left()
       while wall_on_right():
            move()
       turn_right()
       move()
       turn_right()
       while front_is_clear():
            move()
       turn_left()

while not at_goal():
    if wall_in_front():
       hurdle()
    else: move()

#Maze challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():   
    
    while wall_in_front():
          turn_left()
    while front_is_clear():
          move()
          while right_is_clear() and not at_goal():
                turn_right()
                move()

#answer for the Maze:
# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else: turn_left() 


