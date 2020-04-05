#range of x-values
xmin = -1.5
xmax = 1.5

#range of y-values
ymin = -1.5
ymax = 1.5

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def cAdd(a,b):
  '''Returns the sum of two complex numbers'''
  return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
  '''Returns the product of two complex numbers'''
  return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(z):
  return sqrt(z[0]**2 + z[1]**2)

def julia(z,c,num):
    '''runs the process num times
    and returns the diverge count '''
    count=0
    #define z1 as z
    z1=z
    while count<=num:
        # check the magnitude
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1,z1),c)
        count+=1
        
    return num

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height

def draw():
    # [-0.8,0.156]
    # [-0.4,0.6]
    # [0.4,0.6]
    # [0.285,0.01]
    c = [0.275,0.01]
    #go over all x's and y's on the grid
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl) ,
            (ymin + y * yscl) ]
            #put it into the mandelbrot function
            col=julia(z,c,100)
            #if mandelbrot returns 0
            if col == 100:
                fill(0) #make the rectangle black
            else:
                fill(3*col,255,255) #make the rectangle white
            #draw a tiny rectangle
            rect(x,y,1,1)
