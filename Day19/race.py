from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(500, 400)  #set screen width and height
bet = screen.textinput(title='Make your bet', prompt='Choose your color')
color = ['red', 'orange', 'green', 'blue', 'pink', 'purple']
y_ind = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_ind[t_index])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f'You are the winner')
            else:
                print('loser')
        dist_rand = random.randint(0, 10)
        turtle.forward(dist_rand)


screen.exitonclick()

