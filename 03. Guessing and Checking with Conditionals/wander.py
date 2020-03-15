from turtle import *
from random import randint

speed(0)

def wander():
	while True:
		forward(3)
		if xcor() >= 250 or xcor() <= -250 or ycor() >= 250 or ycor() <= -250:
			left(randint(90,180))


shape("turtle")
wander()