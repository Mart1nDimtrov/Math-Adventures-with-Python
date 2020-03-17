def equation(a,b,c,d):
	''''solves equations of the	form ax + b = cx + d'''
	return(d - b)/(a - c)

print(equation(2,5,0,13))
print(equation(4,-12,2,-9))

x = equation(12,18,-34,67) # assign to a variable
print(x)

print(equation((1/2),(2/3),(1/5),(7/8))) # different result
										 # web calc
# check last equation
x = equation((1/2),(2/3),(1/5),(7/8))
print(((1/2)*x) + (2/3))
print((1/5)*x + (7/8))