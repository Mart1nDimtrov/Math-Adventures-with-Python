from random import randint


def numberGame():
	# choose a random number
	# between 1 and 100
	number = randint(1,100)

	print("I'm thinking of a number between 1 and 100.")
	guess = int(input("What's your guess? "))

	while True:
		if number == guess:
			print("That's correct! The number was", number)
			break
		elif number > guess:
			print("Nope. Higher.")
		else:
			print("Nope. Lower.")
		guess = int(input("What's your guess? "))	



numberGame()