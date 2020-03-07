# exerCise 1-3: tri anD tri again
# Write a triangle()
# function that will draw a triangle of a given “side length.”

from turtle import *

# encapsulate with a function
def triangle(sidelength=100):
    # use a for loop
    for i in range(3):
        forward(sidelength)
        right(120)

# set speed and shape
shape('turtle')
speed(0)
# create a square
triangle()
