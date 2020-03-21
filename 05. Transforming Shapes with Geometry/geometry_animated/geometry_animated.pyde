t = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    global t
    #set background white
    background(255)
    translate(width/2,height/2)
    
    rotate(radians(-t))
    for i in range(1,13):
        pushMatrix() #save this orientation
        translate(200,0)
        rotate(radians(t*10))
        rect(0,0,50,50)
        popMatrix() #return to the saved orientation
        rotate(radians(360/12/i+1))
        
    rotate(radians(t+t))
    for i in range(1,13):
        pushMatrix() #save this orientation
        translate(-200,0)
        rotate(radians(-t*10))
        rect(0,0,50,50)
        popMatrix() #return to the saved orientation
        rotate(radians(-360/12/i+1))
    
    t += 1

#def draw():
#    global t
#    #set background white
#    background(255)
#    translate(width/2,height/2)
#    rotate(radians(t))
#    for i in range(12):
#        translate(200,0)
#        rotate(radians(t))
#        if i % 2 == 1:
#            ellipse(200,0,50,50)
#        else:
#            rect(200,0,50,50)
#        rotate(radians(360/12))
#    t += 1
