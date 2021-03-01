from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

line = Turtle()
screen = Screen()
scoreboard = Scoreboard()
ball = Ball()

screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((560, 0))
left_paddle = Paddle((-560, 0))


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


line.hideturtle()
line.pensize(5)
line.pencolor("white")
line.penup()
line.goto(0, 285)
line.setheading(270)

for _ in range(20):
    line.speed("fastest")
    line.pendown()
    line.forward(9)
    line.penup()
    line.forward(20)



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 40 and ball.xcor() > 530 or ball.distance(left_paddle) < 40 and ball.xcor() < -530:
        ball.bounce_x()

    if ball.xcor() > 580:
        ball.reset_position()
        scoreboard.increase_left_score()

    if ball.xcor() < -580:
        ball.reset_position()
        scoreboard.increase_right_score()



# screen.listen()
# screen.onkey(right_up, "Up")
# screen.onkey(right_down, "Down")
# screen.onkey(left_up, "Up")
# screen.onkey(left_down, "Down")









screen.exitonclick()