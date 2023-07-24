import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LEVEL1 = 4
LEVEL2 = 8
LEVEL3 =  12

DISTANCE_BETWEEN_CAR = 35

from turtle import  Turtle


class CarManager():

    def __init__(self):
        self.car_list = []

    # Create the cars
    def Car(self):

        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)

        # create the random distance between each car
        xcor = 260 + len(self.car_list) * DISTANCE_BETWEEN_CAR
        car.setpos(xcor,random.randint(-250,250))
        self.car_list.append(car)

    #car speed increases when turtle crosses the road
    def Level_1(self):

        for index in self.car_list:
            xcor = index.xcor() - LEVEL1
            index.goto(xcor, index.ycor())

    def Level_2(self):

        for index in self.car_list:
            xcor = index.xcor() - LEVEL2
            index.goto(xcor, index.ycor())

    def Level_3(self):

        for index in self.car_list:
            xcor = index.xcor() - LEVEL3
            index.goto(xcor, index.ycor())
