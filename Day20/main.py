from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snakes')

starting_pos = [(0,0), (-20,0), (-40,0)]

for pos in starting_pos:
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.goto(pos)


screen.exitonclick()