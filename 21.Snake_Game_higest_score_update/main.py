from turtle import Screen
import time
from snake import  Snake
from food import Food
from score import  Score

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
score = Score()
screen.onkey(snake.up,"Up")
food  = Food()

screen.listen()
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on  = True

while is_game_on:

    time.sleep(0.1)
    screen.update()
    snake.Move()

    #when collide with the food
    if snake.head.distance(food) < 14:
        food.get_location()
        snake.extend()
        score.track_score()

    #detect collision when hit wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() < -240 or snake.head.ycor() > 235:
        is_game_on = False
        score.game_over()


    for segments in snake.snake_list[1:]:

        if snake.head.distance(segments) < 10:
            is_game_on = False
            score.game_over()
screen.exitonclick()