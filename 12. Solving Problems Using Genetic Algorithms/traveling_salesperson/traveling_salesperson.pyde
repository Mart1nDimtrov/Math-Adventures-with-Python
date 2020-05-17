import random

cities = []
N_CITIES = 100
random_improvements = 0
mutated_improvements = 0
population = []
POP_N = 1000 #number of routes

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
        
    def calc_length(self):
        self.distance = 0
        for i,num in enumerate(self.cityNums):
            # find the distance from the current city to the previous city
            self.distance += dist(cities[num].x,
            cities[num].y,
            cities[self.cityNums[i-1]].x,
            cities[self.cityNums[i-1]].y)
        return self.distance
    
    def mutate(self,num):
        indices = random.sample(list(range(N_CITIES)),num)
        child = Route()
        child.cityNums = self.cityNums[::]
        for i in range(num-1):
            child.cityNums[indices[i]],child.cityNums[indices[(i+1)%num]] = \
            child.cityNums[indices[(i+1)%num]],child.cityNums[indices[i]]
        return child
    
    def crossover(self,partner):
        '''Splice together genes with partner's genes'''
        index_splice = random.randint(0,N_CITIES-2)
        child = Route()
        child.cityNums = self.cityNums[:index_splice]
        if random.random()<0.5:
            child.cityNums = child.cityNums[::-1]
        #list of numbers not in the slice
        child.cityNums = child.cityNums + [x for x in partner.cityNums if x not in child.cityNums]
        
        return child
        
def create_cities(num):
    cit = []
    
    for i in range(num):
        cit.append(City(
            random.randint(50,width-50),random.randint(50,height-50),i))
                      
    return cit
        
def setup():
    global record_distance,best,cities,population
    size(600,600)
    cities = create_cities(N_CITIES)
    for i in range(POP_N):
        population.append(Route())
        
    best = random.choice(population)
    record_distance = best.calc_length()
    first = record_distance
    
def draw():
    global best,record_distance,population
    background(0)
    best.display()
    println(record_distance)
    #println(best.cityNums) #If you need the exact Route through the cities!
    population.sort(key=Route.calc_length)
    population = population[:POP_N] #limit size of population
    length_1 = population[0].calc_length()
    if length_1 < record_distance:
        record_distance = length_1
        best = population[0]
        
    #do crossover on population
    for i in range(POP_N):
        parentA,parentB = random.sample(population,2)
        #reproduce:
        child = parentA.crossover(parentB)
        population.append(child)
    
    #mutateN the best in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = best.mutate(i)
            population.append(new)
        
    #mutateN random Routes in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = random.choice(population)
            new = new.mutate(i)
            population.append(new)
    


    
    
    
