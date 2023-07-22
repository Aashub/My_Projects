import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("gray")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# listen key is important to make work of onkey function
screen.listen()
screen.onkey(player.Move,"w")

#game continue until game_is_on = False
game_is_on = True
while game_is_on:
    car_manager.Car()
    time.sleep(0.1)

    # when car collided with turtle then game is over
    for car in car_manager.car_list:

        if player.distance(car) < 40:
            scoreboard.Game_Over()
            game_is_on = False

    car_manager.Level_1()
    # when turtle hit the edge increase the car speed
    if scoreboard.Level == 2:
        car_manager.Level_2()
    elif scoreboard.Level == 3:
        car_manager.Level_3()
    screen.update()

    #when turtle hit the top edge increase level by reseting coordinate
    if player.ycor() == 290:
        player.setpos(0,-280)
        scoreboard.Score()

screen.exitonclick()