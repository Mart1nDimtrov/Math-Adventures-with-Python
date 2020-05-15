import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"

def makeList():
	'''Returns a list of characters the same length
	as the target'''
	char_list = []
	for i in range(len(target)):
		char_list.append(random.choice(characters))

	return char_list

def score(my_list):
	'''Returns one integer: the number of matches with target'''
	matches = 0
	for i in range(len(target)):
		if target[i] == my_list[i]:
			matches += 1

	return matches

def mutate(my_list):
	'''Returns mylist with one letter changed'''
	new_list = list(my_list)
	new_list[random.randint(0,len(my_list)-1)] = random.choice(characters)

	return new_list

random.seed()
my_list = makeList()

result_score = score(my_list)
list_len = len(target)
# check how many guesses were made
num_guess = 0

# iterate until result score and list_len are the same
while result_score != list_len:
	num_guess += 1
	new_list = mutate(my_list)
	new_score = score(new_list)
	# if the score is better turn the old list into the new one
	if new_score > result_score:
		my_list = new_list
		result_score = new_score
	print("".join(new_list))

print(num_guess)


