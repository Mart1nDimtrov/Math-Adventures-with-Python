'''The guess method'''
def f(x):
	return 2*x**2 + 7*x - 15

def average(a,b):
	return (a + b)/2.0

def guess():
	lower = 1
	upper = 2
	for i in range(100):
		midpt = average(lower,upper)
		if f(midpt) == 0:
			return midpt
		elif f(midpt) < 0:
			upper = midpt
		else:
			lower = midpt
		# print(upper,lower)
	return midpt

# print(f(-5)) first root
x = guess()
print(x,f(x)) # 1.5 second root