def setup():
    size(600,600)

def draw():
    translate(width/2,height/2)
    for i in range(12):
        rect(200,0,50,50)
        rotate(radians(360/12))

#def draw():
#    translate(width/2,height/2)
#    ellipse(0,0,20,20)
#    for i in range(1,20):
#        ellipse(100,100,20,20)
#        rotate(radians(30))

#def draw():
#    translate(width/2,height/2)
#    ellipse(0,0,20,20)
#    ellipse(width/3,height/3,20,20)
#    ellipse(width/3,-height/3,20,20)
#    ellipse(-width/3,height/3,20,20)
#    ellipse(-width/3,-height/3,20,20)
    
    

#def draw():
#    translate(width/2,height/2)
#    rotate(radians(20))
#    ellipse(200,100,20,20)
#    rect(20,40,50,30)
