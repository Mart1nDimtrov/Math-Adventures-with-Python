
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

angle = 5
length = 50
# move the turtle
for i in range(240):
    star(length)
    right(angle)
    length += 1

