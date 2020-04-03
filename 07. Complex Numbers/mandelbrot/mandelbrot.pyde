def cAdd(a,b):
  '''Returns the sum of two complex numbers'''
  return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
  '''Returns the product of two complex numbers'''
  return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(z):
  return sqrt(z[0]**2 + z[1]**2)

def mandelbrot(z,num):
    '''runs the process num times
    and returns the diverge count '''
    count=0
    #define z1 as z
    z1=z
    while count<=num:
        print(magnitude(z1))
        # check the magnitude
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1,z1),z)
        count+=1
        
    return num

mandelbrot([0.25,0.75],100)
