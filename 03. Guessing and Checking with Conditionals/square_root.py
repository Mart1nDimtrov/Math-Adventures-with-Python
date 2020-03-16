def average(a,b):
	return (a+b)/2

def square_root(number):
	'''Finds the square root of num by
	playing the Number Guessing Game
	strategy by guessing over the
	range from "low" to "high"'''
	high = number / 2
	low = 0
	
	for i in range(1,1000):
		avg = average(low,high) 
		if avg**2 == number:
			print(f"Root is: {avg}")
			break 
		elif avg**2 > number:
			high = avg
			print(low, avg)
		else:
			low = avg
			
			print(high, low)

square_root(200)
square_root(1000)
square_root(50000)



			