from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.move_speed = 0.1
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.penup()
        self.forward(MOVE_DISTANCE)
        # it can also be written:
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

    def is_at_finish_lin(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)