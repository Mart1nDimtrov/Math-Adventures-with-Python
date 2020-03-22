def setup():
    size(600,600)
    colorMode(HSB)
    
# draw a colorful interactive grid    
def draw():
    background(0)
    
    for x in range(0,20):
        for y in range(0,20):
            d = dist(30*x,30*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(x*30,y*30,25,25)
 
# draw a colorful grid        
#def draw():
#    background(0)
#    
#    for x in range(0,20):
#        for y in range(0,20):
#            fill(x*y,255,255)
#            rect(x*30,y*30,25,25)
    
# draw a checkered board
#def draw():
#    background(255)
#    
#    for x in range(0,20):
#        for y in range(0,20):
#            if (x+y+1)%2 == 1:
#                fill(122)
#            else:
#                fill(255)
#            rect(x*30,y*30,20,20)
