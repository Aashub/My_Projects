import turtle
from turtle import Screen, Turtle


screen = Screen()
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE= 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0


# snake class that make use in main file
class Snake:

    def __init__(self):

        self.snake_list = []
        self.Create_Snake()
        self.head = self.snake_list[0]

    # this method create snake
    def Create_Snake(self):

        """create  square turtle object give them color provide them coordinate so they can align """
        for postion in STARTING_POSITION:
           self.add_segment(postion)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)

        """increase the size of of snake """
    def extend(self):
        self.add_segment(self.snake_list[-1].position())



    # provide move functionality to how to move it
    def Move(self):

        """run from last element to initial and so it can move in the form that it can change direction"""
        """3 come on 2 next time 2 goes to 1 and 1 goes to whereever direction decided this process continue and it can move forward"""

        for move in range(len(self.snake_list) - 1,0,-1):
            xcor = self.snake_list[move - 1].xcor()
            ycor = self.snake_list[move - 1].ycor()

            self.snake_list[move].goto(xcor,ycor)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
             self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



