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

my_list = makeList()

for i in range(20000):
	new_list = mutate(my_list)
	if score(my_list) < score(new_list):
		my_list = new_list

print(target)
print(''.join(my_list))
print(score(my_list))


