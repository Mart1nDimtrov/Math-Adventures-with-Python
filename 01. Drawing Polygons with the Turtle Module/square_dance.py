# exerCise 1-1: square DanCe
# Return to the myturtle.py program.
# Your first challenge is to modify
# the code in the program using only
# the forward and right functions so that the turtle draws a square.

from turtle import *

# encapsulate with a function
def square(sidelength=100):
    # use a for loop
    for i in range(4):
        forward(sidelength)
        right(90)


# set speed and shape
shape('turtle')
speed(0)

# move the turtle
for i in range(35):
    square()
    right(10)



