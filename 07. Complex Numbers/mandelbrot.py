from math import sqrt

def cAdd(a,b):
	'''Returns the sum of two complex numbers'''
	return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
	'''Returns the product of two complex numbers'''
	return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(z):
	return sqrt(z[0]**2 + z[1]**2)

z = [0.25,1.5]
z2 = cMult(z,z)
print(z2)

z3 = cAdd(z2,z)
print(magnitude(z3))

z = [0.25,0.75]

z2 = cMult(z,z)
z3 = cAdd(z2,z)
print(magnitude(z3))

z2 = cMult(z3,z3)
z3 = cAdd(z2,z)
print(magnitude(z3))