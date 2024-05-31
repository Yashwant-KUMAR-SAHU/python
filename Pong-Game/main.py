from turtle import Turtle, Screen
from paddle import Paddle
from Ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.ycor() < 320:
        ball.bounce_x()

    # ball R goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # ball L goes out of bounds
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()