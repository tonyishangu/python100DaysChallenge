from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

paddle = Turtle()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_pad.go_up, 'Up')
screen.onkey(r_pad.go_down, 'Down')
screen.onkey(l_pad.go_up, 'w')
screen.onkey(l_pad.go_down,'s')



game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

screen.exitonclick()