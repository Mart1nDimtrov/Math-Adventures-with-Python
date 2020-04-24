sheeps = []
grassList = [] #list to store grass
patchSize = 10 #size of each patch of grass

#setting the constants for colors
WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)

class Sheep:
    
    def __init__(self,x,y):
        self.x = x #x-position
        self.y = y #y-position
        self.sz = 10 #size
        self.energy = 20
        
    def update(self):
        #make sheep walk randomly
        move = 1 #the maximum it can move in any direction
        self.energy -= 1 #walking costs energy
        if self.energy <= 0:
            sheeps.remove(self)
        self.x += random(-move, move)
        self.y += random(-move, move)
        fill(255) #white
        ellipse(self.x,self.y,self.sz,self.sz)
        
class Grass:
    
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 5 #energy from eating this patch
        self.eaten = False #hasn't been eaten yet
        self.sz = sz
        
    def update(self):
        fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)
        
def setup():
    global patchSize
    noStroke()
    size(600,600)
    #create a Sheep object called shawn at (300,200)
    for s in range(3):
        sheeps.append(Sheep(random(height),random(width)))
    #creating the grass
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
    
def draw():
    background(255)
    #update the grass first
    for grass in grassList:
        grass.update()
    #update the sheep
    for s in sheeps:
        s.update()
    
