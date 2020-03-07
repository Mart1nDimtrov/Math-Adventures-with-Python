# exerCise 1-2: a CirCle oF squares 
# Write and run a function that draws 60 squares,
# turning right 5 degrees after each square.
# Use a loop! Your result should end up looking like this:
from turtle import *

# first create the square
def square():
    for i in range(4):
        forward(100)
        right(90)

# use the square for the circle
def circle():
    for i in range(63):
        square()
        right(5)

shape("turtle")
speed(0)
circle()


        
    
