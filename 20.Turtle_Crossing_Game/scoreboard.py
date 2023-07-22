FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Level = 1
        self.update_scoreboard()

    #align the level on the screen and update it
    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 250)
        self.write("Level: ", align="center", font= FONT)
        self.goto(-170, 250)
        self.write(self.Level, align="center", font=FONT)

    # increase the level by 1
    def Score(self):
        self.Level += 1
        self.update_scoreboard()


    def Game_Over(self):

        self.goto(0,0)
        self.write("Game Over!", align="center", font=  FONT )

