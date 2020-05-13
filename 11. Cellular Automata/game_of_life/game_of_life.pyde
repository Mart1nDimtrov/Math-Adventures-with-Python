from random import choice

GRID_W = 60
GRID_H = 60
#size of cell
SZ = 10

class Cell:
    def __init__(self,r,c,state=0):
        self.c = c
        self.r = r
        self.state = state
        
    def display(self):
        if self.state == 1:
            fill(0) #black
        else:
            fill(255) #white
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
            
    def checkNeighbors(self):

        neighbs = 0
        #check the neighbors
        for dr,dc in[[-1,0],[1,0],[0,-1],[0,1],[-1,1],[-1,-1],[1,1],[1,-1]]:
            try:
                if cell_list[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state == 1:
            if neighbs in[2,3]:
                return 1
            else:
                return 0  
        if neighbs == 3:
            return 1
        return 0    
                

def setup():
    global SZ, cell_list
    size(700,700)
    SZ = width// GRID_W + 1
    cell_list = create_cell_list()
    
def draw():
    global cell_list
    frameRate(10)
    cell_list = update(cell_list)
    for row in cell_list:
        for cell in row:
            cell.display()
            
        
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
            new_list[j].append(Cell(i,j,choice([0,1]))) #add off Cells or zeroes
            #center cell is set to on
            
    return new_list


        
