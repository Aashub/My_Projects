import random
import turtle
from turtle import Turtle, Screen


turtles = Turtle()
screen = Screen()


should_continue = False
screen.setup(width= 500, height=400)
user_input = screen.textinput(title="make your bet", prompt= "decide the turtle color to bet the race. colors are 'red',"
                                                             "'blue','yellow'','voilet','green'")
turtle_color = ["red", "blue", "green", "yellow", "violet"]
y_axis = [-40,-10,20,50,80]
turtle_list = []


for index  in range(0,5):
    turtles = Turtle()
    turtles.penup()
    turtles.shape("turtle")
    turtles.color(turtle_color[index])
    turtles.goto(x=-240, y = y_axis[index])
    turtle_list.append(turtles)

if user_input:
    should_continue = True

while should_continue:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            wining_color = turtle.pencolor()
            if wining_color == user_input:
                print(f"The winner is {user_input}")
                should_continue = False

            elif wining_color != user_input:
                print(f"the winner is {wining_color} you lost the race!")
                should_continue = False


        random_speed = random.randint(0,10)
        turtle.forward(random_speed)





screen.exitonclick()
