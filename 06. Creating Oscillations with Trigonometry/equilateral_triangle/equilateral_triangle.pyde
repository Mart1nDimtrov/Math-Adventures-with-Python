def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    polygon(8,100) #3 sides, vertices 100 units from the center
    
def polygon(sides,sz):
    '''draws a polygon given the number
    of sides and length from the center'''
    step = radians(360/sides)
    beginShape()
    for side in range(sides):
        vertex(sz*cos(side*step),sz*sin(side*step))
    endShape(CLOSE)
