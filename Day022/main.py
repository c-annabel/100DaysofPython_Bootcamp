# Build Pong

# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another Paddle
# 4. Create the ball and make it move
# 5. Detect collision with wal and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)  # control the animation, tracer is off, 1 is on

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # update the screen after the animation is turned off
    ball.move()

    # Detect collision with wall of up/down.
    if ball.ycor() > 280 or \
            ball.ycor() < -280:
        ball.bounce_y()


    #Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
