def f(x):
	return 6*x**3 + 31*x**2 + 3*x - 10

def average(a,b):
	return (a+b)/2


def guess(high,low):
	avg = 0
	for i in range(1,101):
		avg = average(high,low)
		if f(avg) == 0:
			break
		elif f(avg) > 0:
			high = avg
		else:
			low = avg
	return avg

# plug in the values from the graphic to 
# find the exact values

print(guess(-1,0))
print(f(-0.6666666666666666))
