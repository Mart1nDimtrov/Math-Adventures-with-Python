def factors(num):
	'''returns a list of the factors of num'''
	factors = []
	for i in range(1,num+1):
		if num % i == 0:
			factors.append(i)

	return factors

print(factors(120))
