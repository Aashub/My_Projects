STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.setpos(STARTING_POSITION)

    # move turtle with distance of 10
    def Move(self):

        ycor = self.ycor()  + MOVE_DISTANCE
        self.goto(self.xcor(), ycor)





