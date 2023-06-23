from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent food items."""

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color('red')
        self.shapesize(.5)
        self.speed('fastest')
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)

    # new location
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)