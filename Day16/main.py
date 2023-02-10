# OBJECT ORIENTED PROOGRAMMING
#       it's a method of structuring a program by bundling related 
#       properties and behacviours into individual objects
#       structure of a program

# OBJECTS
# car(object) = CarBlueprint()=>(class)
# Example using TURTLE CLASS

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('purple')
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

# ATTRIBUTES OF AN OBJECT
#       Data an object keeps track of
#       syntax
#       car(object).speed(attribute)
#       Example using TURTLE CLASS

my_screen = Screen()
print(my_screen.canvheight)

# METHODS OF AN OBJECT
#       Function tied to an object
#       syntax
#       car------->object.stop()------> mthod
#       Example using TURTLE CLASS

my_screen.exitonclick()
