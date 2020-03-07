# exerCise 1-4: Polygon FunCtions Write a function called polygon
# that takes an integer as an argument and makes the turtle draw
# a polygon with that integer’s number of sides.


from turtle import *

# encapsulate with a function
def polygon(sides=3,sidelength=100):
    angle = 360 / sides
    # use a for loop
    for i in range(sides):
        forward(sidelength)
        right(angle)

# set speed and shape
shape('turtle')
speed(0)
# move the turtle
polygon(10)
