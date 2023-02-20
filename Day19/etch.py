from turtle import Turtle, Screen

turtles = Turtle()

screen = Screen()

def move_forward():
    turtles.forward(10)

def move_backward():
    turtles.backward(10)

def move_clockwise():
    turtles.right(30)
    turtles.forward(10)

def move_anticlockwise():
    turtles.left(30)


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_clockwise)
screen.onkey(key='d', fun=move_anticlockwise)

screen.exitonclick()