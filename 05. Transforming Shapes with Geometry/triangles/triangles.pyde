
def setup():
    size(600,600)
    rectMode(CENTER)
    
t = 0

def draw():
    global t
    background(255)
    translate(width/2,height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix() 
        translate(-100,-100)
        rotate(radians(t*2))
        tri(180)
        tri(140)
        tri(100)
        tri(60)
        tri(20)
        tri(10)
        popMatrix()
        rotate(radians(360/12))
    t += 1

# make two triangles spin in opposite directions
#def draw():
#    global t
#    translate(width/2,height/2)
#    rotate(radians(-t*2))
#    tri(200) #draw the equilateral triangle
#    rotate(radians(t*4))
#    tri(200)
#
#    t += 1


def tri(length):
    '''Draws an equilateral triangle
    around center of triangle'''
    triangle(0,-length,
    -length*sqrt(3)/2, length/2,
    length*sqrt(3)/2, length/2)

#def draw():
#    global t
#    translate(height/2,width/2)
#    for i in range(20):
#        rotate(radians(t))
#        triangle(0,0,100,100,200,-200)
#        rotate(360/12)
#        
#   t += 0.1
    
    
