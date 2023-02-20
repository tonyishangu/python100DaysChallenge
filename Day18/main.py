from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')    #changing the shape
timmy_the_turtle.color('green')

# draw a square
for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


for i in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()



































screen = Screen()
screen.exitonclick()