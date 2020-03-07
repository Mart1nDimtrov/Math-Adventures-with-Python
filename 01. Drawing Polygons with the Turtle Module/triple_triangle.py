
from turtle import *

# encapsulate with a function
def triangle(sidelength=100):
    # use a for loop
    for i in range(3):
        forward(sidelength)
        right(120)

def cross(sidelength=100):
    for i in range(3):
        triangle(sidelength)
        right(120)

# set speed and shape
shape('turtle')
speed(0)
# draw forms

length = 40
angle = 2.4
for i in range(242):
    cross(length)
    right(angle)
    length += 1.5
