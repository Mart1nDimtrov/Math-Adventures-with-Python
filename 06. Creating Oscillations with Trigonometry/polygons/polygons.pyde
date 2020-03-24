def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    background(255)
    beginShape()
    length = 100
    for i in range(6):
        vertex(length*cos(radians(i*60)),length*sin(radians(i*60)))
    endShape(CLOSE)
    
    
