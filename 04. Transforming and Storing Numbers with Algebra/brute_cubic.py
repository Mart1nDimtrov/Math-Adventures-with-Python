def g(x):
	return 6*x**3 + 31*x**2 + 3*x - 10

def plug():
	for x in range(-100,101):
		if g(x) == 0:
			print(f"x: {x}")

plug()