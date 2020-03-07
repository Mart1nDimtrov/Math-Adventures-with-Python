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
    right(10)
    square(50)
    square(80)
    square()
