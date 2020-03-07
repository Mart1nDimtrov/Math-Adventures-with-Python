# exerCise 1-6: a star is Born
# First, write a “star” function that will draw a five-pointed star.
# Next, write a function called starSpiral() that will draw a spiral of stars.

from turtle import *

# then rotate it
def star(sidelength=100):
    # use a for loop
    for i in range(1,6):
        forward(sidelength)
        right(144)


# set speed and shape
shape('turtle')
speed(0)

angle = 1
length = 1
# move the turtle
for i in range(120):
    star(length)
    right(angle)
    angle += 3
    length += 3

