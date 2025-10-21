n = 20
dim =0
margin = 20
def setup():
    size(800, 800)
    global dim
    
    # queremos que haya n cuadrados en width, height y quiero que se separe del margen
    dim = (width-margin*2)/n
    noLoop()
    
def draw():
    rectMode(CENTER)

    background(255,255,255)
    
    for j in range(n):
        for i in range(n):
            x = margin + i * dim
            y = margin + j * dim
            #square(x, y, dim)
            
            rnd = int(random(0,4))
            fill(random(255), random(255), random(255))
            noStroke()
            
            if rnd == 0:
                triangle(x + dim, y, x + dim, y + dim, x, y + dim)
            elif rnd == 1:
                triangle(x, y, x + dim, y, x, y + dim)
            elif rnd == 2:
                triangle(x, y, x + dim, y + dim, x, y + dim)
            else:
                triangle(x, y, x + dim, y, x + dim, y + dim)
                
                
def keyPressed():
    redraw()
