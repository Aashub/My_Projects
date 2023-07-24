from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.get_location()

    def get_location(self):
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-230, 230)
        self.goto(x_coordinate, y_coordinate)

