cwidth = 0
cheight = 0
xcor = 0
ycor = 0

def setup():
    global cwidth,cheight,xcor,ycor
    size(600,600)
    cwidth = width
    cheight = height
    xcor = cwidth / 2
    ycor = cheight / 2
    
def draw():
    global xcor,ycor,cwidth,cheight
    background(0) #black background
    print(xcor,ycor)
    if cwidth >= xcor + 20:
        xcor += 1
    if cheight >= ycor + 20:
        ycor += 1
    ellipse(xcor,ycor,20,20)
