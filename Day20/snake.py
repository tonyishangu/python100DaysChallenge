from turtle import Turtle
starting_pos = [(0,0), (-20,0), (-40,0)]
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in starting_pos:
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()   #stop drawing
            new_snake.goto(pos)
            self.snake.append(new_snake)

    def move(self):
        for seg in range(len(self.snake) -1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
            self.snake[0].forward(move_distance)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() !=  Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)