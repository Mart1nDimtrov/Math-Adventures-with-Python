GRID_W = 60
GRID_H = 60
#size of cell
SZ = 10
generation = 0

class Cell:
    def __init__(self,r,c,state=0):
        self.c = c
        self.r = r
        self.state = state
        
    def display(self):
        if self.state == 1:
            fill(0) #black
        else:
            fill(random(255)) #white
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
            
    def checkNeighbors(self):
        if self.state == 1: return 1 #on Cells stay on
        neighbs = 0
        #check the neighbor above
        for dr,dc in[[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if cell_list[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if neighbs in[1,4]:
            return 1
        else:
            return 0
            

def setup():
    global SZ, cell_list
    size(700,700)
    SZ = width// GRID_W + 1
    cell_list = create_cell_list()
    
def draw():
    global generation,cell_list
    frameRate(10)
    cell_list = update(cell_list)
    for row in cell_list:
        for cell in row:
            cell.display()
    
    generation += 1
    if generation == 30:
        generation = 1
        cell_list = create_cell_list()
            
        
def update(cell_list):
    new_list = []
    for r,row in enumerate(cell_list):
        new_list.append([])
        for c,cell in enumerate(row):
            new_list[r].append(Cell(r,c,cell.checkNeighbors()))
            
    return new_list[::]

            
def create_cell_list():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    new_list=[]#empty list for cells
    #populate the initial cell list
    for j in range(GRID_H):
        new_list.append([]) #add empty row
        for i in range(GRID_W):
            new_list[j].append(Cell(i,j,0)) #add off Cells or zeroes
            #center cell is set to on
    new_list[GRID_H//2][GRID_W//2].state = 1
            
    return new_list


        
