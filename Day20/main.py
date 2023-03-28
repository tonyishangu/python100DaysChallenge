from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snakes')
screen.tracer(0)

starting_pos = [(0,0), (-20,0), (-40,0)]

snake =[]

for pos in starting_pos:
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.penup()   #stop drawing
    new_snake.goto(pos)
    snake.append(new_snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(snake) - 1, 0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg - 1].ycor()
        snake[seg].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()