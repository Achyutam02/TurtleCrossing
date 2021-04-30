from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("red")
        self.x_axis = 0
        self.goto(STARTING_POSITION)
        self.update = 20

    def up(self):

        new_y = self.ycor() + 20
        self.goto(self.x_axis, new_y)

    def restart(self):
        self.goto(STARTING_POSITION)

