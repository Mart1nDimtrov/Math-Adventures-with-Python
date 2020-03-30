t = 0
points = []

def setup():
    size(600,600)
    noStroke()
    
def draw():
    
    global t, points
    a1,a2 = 100,200 #amplitudes
    f1,f2 = 1.5,2 #frequencies
    p1,p2 = 0,PI/2 #phase shifts
    d1,d2 = 0.02,0.02 #decay constants
    
    background(255)
    translate(width/2,height/2)
    x = a1*cos(f1*t + p1)*exp(-d1*t) 
    y = a2*cos(f2*t + p2)*exp(-d2*t)
    points.append([x,y])
    fill(0) #black
    ellipse(x,y,5,5)
    for i,v in enumerate(points):
        ellipse(x,y,5,5)
        stroke(0) #black
        if i < len(points) - 1:
            line(v[0],v[1],points[i+1][0],points[i+1][1])
        
    t += .1
