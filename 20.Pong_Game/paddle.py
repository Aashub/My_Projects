from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(position)


    def Go_up(self):

        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def Go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)


