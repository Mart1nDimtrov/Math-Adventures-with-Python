r1 = 100 #radius of big circle
r2 = 10 #radius of small circle
t = 0 #time variable
circleList = []

def setup():
    size(600,600)
    
def draw():
    global t
    background(200)
    #move to left-center of screen
    translate(width/4,height/2)
    
    noFill() #don't color in the circle
    stroke(0) #black outline
    ellipse(0,0,2*r1,2*r1)
    
    #circling ellipse:
    fill(255,0,0) #red
    y = r1*sin(t)
    x = r1*cos(t)
    ellipse(x,y,r2,r2) 
    
    stroke(0,255,0) #green for the line
    line(x,y,200,y)
    fill(0,255,0) #green for the ellipse
    ellipse(200,y,10,10)
    
    x = r1*sin(t)
    y = r1*cos(t)
    fill(255,0,0)
    ellipse(x,y,r2,r2)  
    
    stroke(0,255,0) #green for the line
    line(x,y,200,y)
    fill(0,255,0) #green for the ellipse
    ellipse(200,y,10,10)
 
    t += 0.1
  
