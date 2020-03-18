#set the range of x-values
xmin = -10
xmax = 10

#range of y-values
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def f(x):
    return x**2

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    
    global xscl, yscl
    background(255) #white
    translate(width/2,height/2)
    grid(xscl,yscl) # draw the grid
    fill(-1)
    for i in range(-10,11,1):
        ellipse(i*xscl,f(i)*yscl,10,10)


def grid(xscl,yscl):
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    
    for i in range(xmin,xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
        
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
