from math import sqrt

def cAdd(a,b):
	'''Returns the sum of two complex numbers'''
	return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
	'''Returns the product of two complex numbers'''
	return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(z):
	return sqrt(z[0]**2 + z[1]**2)


u = [1,2]
v = [3,4]


print(cAdd(u,v))
print(cMult(u,v))

# rotate a number
print(cMult([3,4],[0,1]))

# return the absolute value of the complex numbers
print(magnitude(u))