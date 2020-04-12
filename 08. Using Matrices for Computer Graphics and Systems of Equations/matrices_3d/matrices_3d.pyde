#set the range of x-values
xmin = -10
xmax = 10

#range of y-values
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

fmatrix = [[0,0,0],[1,0,0],[1,2,0],[2,2,0],[2,3,0],[1,3,0],[1,4,0],
[3,4,0],[3,5,0],[0,5,0],
[0,0,1],[1,0,1],[1,2,1],[2,2,1],[2,3,1],[1,3,1],[1,4,1],
[3,4,1],[3,5,1],[0,5,1]]

#list of points to connect:
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],
[7,8],[8,9],[9,0],
[10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],
[17,18],[18,19],[19,10],
[0,10],[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],
[8,18],[9,19]]

def transpose(a):
    '''Transposes matrix a'''
    output = []
    m = len(a)
    n = len(a[0])
    #create an n x m matrix
    for i in range(n):
        output.append([])
        for j in range(m):
            #replace a[i][j] with a[j][i]
            output[i].append(a[j][i])
            
    return output

def multmatrix(a,b):
  #Returns the product of matrix a and matrix b
  m = len(a) #number of rows in first matrix
  n = len(b[0]) #number of columns in second matrix
  newmatrix = []
  for i in range(m):
    row = []
    #for every column in b
    for j in range(n):
      sum1 = 0
      #for every element in the column
      for k in range(len(b)):
        sum1 += a[i][k]*b[k][j]
      row.append(sum1)
    newmatrix.append(row)
  return newmatrix

def setup():
    global xscl, yscl
    size(600,600)
    #the scale factors for drawing on the grid:
    xscl= width/rangex
    yscl= -height/rangey
    noFill()
    
def draw():
    global xscl, yscl, fmatrix
    background(255) #white
    translate(width/2,height/2)
    grid(xscl, yscl)
    strokeWeight(2) #thicker line
    stroke(0)#black
    # newmatrix = transpose(multmatrix(transformation_matrix,transpose(fmatrix)))
    ang = map(mouseX,0,width,0,TWO_PI)
    rot_matrix = [[cos(ang),-sin(ang)],[sin(ang),cos(ang)]]
    newmatrix = transpose(multmatrix(rot_matrix,transpose(fmatrix)))
    graphPoints(fmatrix)
    stroke(255,0,0) #red resultant matrix
    graphPoints(newmatrix)
    
def grid(xscl,yscl):
    '''Draws a grid for graphing'''
    #cyan lines
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    

def graphPoints(pointList,edges):
    '''Graphs the points in a list using segments'''
    for e in edges:
        line(pointList[e[0]][0]*xscl,pointList[e[0]][1]*yscl,
        pointList[e[1]][0]*xscl,pointList[e[1]][1]*yscl)
    
    
