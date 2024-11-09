from turtle import Turtle
align = "center"
font = ("Arial",13, "bold")
movement = False

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=230)
        self.update_score_board()

    def update_score_board(self):
        self.write(arg=f"Score: {self.score}", align= align, font=font, move=movement)

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write(arg=f"Game Over", align="center", font=font)


    def track_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()



