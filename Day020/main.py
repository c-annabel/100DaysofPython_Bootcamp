# Snake Game

# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #tracer is off, 1 is on

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)  # delay 1 second
    # for sq in all_squares:
    #     sq.forward(20)

    snake.move()


screen.exitonclick()