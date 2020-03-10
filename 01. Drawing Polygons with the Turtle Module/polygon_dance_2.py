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
for i in range(1,181):
	polygon(7,i)
	right(i)
