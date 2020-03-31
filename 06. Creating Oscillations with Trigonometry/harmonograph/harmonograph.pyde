t = 0
points = []

def setup():
    size(600,600)
    noStroke()
    
def harmonograph(t):
    a1,a2 = 100,200 #amplitudes
    f1,f2 = 1.5,2 #frequencies
    p1,p2 = 0,PI/2 #phase shifts
    d1,d2 = 0.02,0.02 #decay constants    
    x = a1*cos(f1*t + p1)*exp(-d1*t) 
    y = a2*cos(f2*t + p2)*exp(-d2*t)
    
    return [x,y]
    
    
def draw():
    global t, points
    background(255)
    translate(width/2,height/2)

    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01
        
    for i,v in enumerate(points):
        stroke(0) #black
        if i < len(points) - 1:
            line(v[0],v[1],points[i+1][0],points[i+1][1])
        
