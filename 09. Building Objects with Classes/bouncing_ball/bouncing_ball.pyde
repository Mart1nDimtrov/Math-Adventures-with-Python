xcor = 300
ballList=[] #empty list to put the balls in

class Ball:
    def __init__(self,x,y):
        '''How to initialize a Ball'''
        self.xcor = x
        self.ycor = y
        self.xvel = random(-3,3)
        self.yvel = random(-3,3)
        self.colors = [random(255) for x in range(3)]
        self.radius = random(20,35)

    def update(self): 
        self.xcor += self.xvel
        self.ycor += self.yvel
        #if the ball reaches a wall, switch direction.
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        if self.ycor > height or self.ycor < 0:
            self.yvel = -self.yvel
        fill(self.colors[0],self.colors[1],self.colors[2])
        ellipse(self.xcor,self.ycor,self.radius,self.radius)
        

def setup():
    size(600,600)
    for i in range(45):
        ballList.append(Ball(random(width),
        random(height)))
    
def draw():
    background(0) #black
    for ball in ballList:
        ball.update()
    
   
