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
# move the turtle
for i in range(60):
    triangle(250)
    triangle(200)
    triangle(150)
    triangle()
    triangle(50)
    right(10)
