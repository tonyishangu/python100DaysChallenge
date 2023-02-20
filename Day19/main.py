from turtle import Turtle, Screen

turtles = Turtle()

screen = Screen()

def move_forward():
    turtles.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.exitonclick()