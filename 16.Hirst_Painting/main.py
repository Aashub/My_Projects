import turtle
from turtle import Screen
import colorgram
import random


tim = turtle

# providing range in tim.colormode
tim.colormode(255)
col = colorgram.extract('hirst_image.jpeg', 330)

rgb_color = []

"""creating tuple so we can use them in rgb format"""
for i in col:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    new_color = (r, g, b)
    rgb_color.append(new_color)

screen = Screen()

# removing to line by using tim.penup()
tim.penup()
tim.speed("fastest")
tim.hideturtle()


"""gererate random color and put dot in random color and move forward 20 pace"""
def create_dot(rgb_color):

    random_color = random.choice(rgb_color)
    for index in range(1):
        tim.dot(15, random_color)
        tim.forward(45)



"""start painting by taking two arguments"""
def start_painting(new_y, counter):
    tim.setheading(230)
    tim.forward(290)
    tim.setheading(0)


    # exit the code when it create 100 dots
    if counter >= 100:
        return

    for index, dot in  enumerate(range(10)):

        create_dot(rgb_color)
        counter += 1

    new_x = 0
    new_y += 40

    # tim.goto can change coordinate each time
    tim.goto(new_x, new_y)
    start_painting(new_y, counter)


counter = 0
new_y = 0
start_painting(new_y, counter)

screen.exitonclick()
