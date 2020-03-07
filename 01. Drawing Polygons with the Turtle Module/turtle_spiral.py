# exerCise 1-5: turtle sPiral
# Make a function to draw 60 squares,
# turning 5 degrees after each square and making each successive square bigger.
# Start at a length of 5 and increment 5 units every square.

from turtle import *

# encapsulate with a function
def triangle(sidelength=100):
    # use a for loop
    for i in range(1,6):
        forward(sidelength)
        if i % 2 == 0:
            right(120)
        else:
            left(120)

        
# set speed and shape
shape('turtle')
speed(0)

# set the length of the side
length = 5


# move the turtle
for i in range(360):
    triangle(length)
    right(1)
    length += 3

