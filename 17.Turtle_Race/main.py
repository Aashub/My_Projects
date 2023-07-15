import random
import turtle
from turtle import Turtle, Screen


turtles = Turtle()
screen = Screen()

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_anticlock():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def move_clock():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear_screen():
#     screen.clearscreen()
#
#
# screen.listen()
#
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "a", fun = move_anticlock)
# screen.onkey(key = "d", fun = move_clock)
# screen.onkey(key = "c", fun = clear_screen)

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
