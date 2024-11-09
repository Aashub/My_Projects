from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(r_paddle.Go_up,"w")
screen.onkey(r_paddle.Go_down,"s")

screen.onkey(l_paddle.Go_up, "Up")
screen.onkey(l_paddle.Go_down, "Down")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.Ball_move()

    # when ball collide to the wall bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # when ball hit the paddle then it bounce back
    if ball.distance(r_paddle)  < 50  and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.x_bounce()

    #when right side misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.L_score()

    #when left side misses
    if ball.xcor() < -390:
        ball.reset_position()
        score.R_score()



screen.exitonclick()