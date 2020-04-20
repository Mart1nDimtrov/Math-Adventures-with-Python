sheeps = []

class Sheep:
    
    def __init__(self,x,y):
        self.x = x #x-position
        self.y = y #y-position
        self.sz = 10 #size
        
    def update(self):
        #make sheep walk randomly
        move = 10 #the maximum it can move in any direction
        self.x += random(-move, move)
        self.y += random(-move, move)
        fill(255) #white
        ellipse(self.x,self.y,self.sz,self.sz)
        
def setup():
    size(600,600)
    #create a Sheep object called shawn at (300,200)
    for s in range(3):
        sheeps.append(Sheep(random(height),random(width)))
    
def draw():
    background(255)
    for s in sheeps:
        s.update()
