from random import choice
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
colorList = [WHITE,RED,YELLOW,PURPLE]

class Sheep:
    
    def __init__(self,x,y,col):
        self.x = x #x-position
        self.y = y #y-position
        self.sz = 10 #size
        self.energy = 20
        self.col = col
        
    def update(self):
        #make sheep walk randomly
        move = 10 #the maximum it can move in any direction
        self.energy -= 1 #walking costs energy
        if self.energy <= 0:
            sheeps.remove(self)
        self.x += random(-move, move)
        self.y += random(-move, move)
        #"wrap" the world Asteroids-style
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        #find the patch of grass you're on in the grassList:
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass + yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz)
        
class Grass:
    
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 5 #energy from eating this patch
        self.eaten = False #hasn't been eaten yet
        self.sz = sz
        
    def update(self):
        if self.eaten:
            fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)
        
def setup():
    global patchSize,rows_of_grass
    rows_of_grass = height/patchSize
    noStroke()
    size(600,600)
    #create a Sheep object called shawn at (300,200)
    for s in range(20):
        rand_col = colorList[int(random(len(colorList)))]
        sheeps.append(Sheep(random(height),random(width),rand_col))
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
    
