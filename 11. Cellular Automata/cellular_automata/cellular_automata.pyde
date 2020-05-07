GRID_W = 20
GRID_H = 20
#size of cell
SZ = 20

class Cell:
    def __init__(self,c,r,state=0):
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
    global cell_list,SZ
    SZ = width // GRID_W 
    size(600,600)
    cell_list = createCellList()
    
    
def draw():
    for row in cell_list:
        for cell in row:
            cell.state = cell.checkNeighbors()
            cell.display()
            
def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    newList=[]#empty list for cells
    #populate the initial cell list
    for j in range(GRID_H):
        newList.append([]) #add empty row
        for i in range(GRID_W):
            newList [j].append(Cell(i,j,0)) #add off Cells or zeroes
            #center cell is set to on
    newList [GRID_H//2][GRID_W//2].state = 1
            
    return newList
        
