import random

N_CITIES = 10
cities = []

class City():
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num # identifying number
        
    def display(self):
        textSize(20)
        text(self.num,self.x-10,self.y-10)
        fill(0,255,255)
        ellipse(self.x,self.y,10,10)
        noFill()
        
class Route:
    def __init__(self):
        self.distance = 0
        #put cities in a list in order:
        self.cityNums = random.sample(list(range(N_CITIES)),N_CITIES)
        
    def display(self):
        strokeWeight(3)
        stroke(255,0,255) #purple
        beginShape()
        print(cities[0].x)
        for i in self.cityNums:
            vertex(cities[i].x,cities[i].y)
            cities[i].display()
        
        # end the path and close it
        endShape(CLOSE)
        
        
def create_cities(num):
    cit = []
    
    for i in range(num):
        cit.append(City(
            random.randint(50,width-50),random.randint(50,height-50),i))
                      
    return cit
        
def setup():
    global cities
    size(600,600)
    background(0)
    cities = create_cities(N_CITIES)
    route_1 = Route()
    route_1.display()



    
    
    
