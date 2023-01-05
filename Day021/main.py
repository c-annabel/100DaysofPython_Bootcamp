# Snake Game

# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food  v
# 5. Create a scoreboard  v
# 6. Detect collision with wall  v
# 7. Detect collision with tail v

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #tracer is off, 1 is on

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or \
        snake.head.xcor() < -280 or \
        snake.head.ycor() > 280 or \
        snake.head.ycor() < -280:

        game_in_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_in_on = False
            scoreboard.game_over()

screen.exitonclick()