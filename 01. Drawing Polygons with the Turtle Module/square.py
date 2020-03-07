from turtle import *

# encapsulate with a function
def square():
    # use a for loop
    for i in range(4):
        forward(100)
        right(90)

# set speed and shape
shape('turtle')
speed(0)
# create a square
square()


