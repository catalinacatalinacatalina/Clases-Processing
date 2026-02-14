x = 400
y = 400
r = 150
extra_rojo = 0
extra_azul = 0
extra_verde = 0

# como si estuviera col_back
def setup():
    size(800,800)
    global col_back, velx, vely
    col_back = color(200, 200, 255)
    background(col_back) # red, green, blue
    frameRate(9999)
    velx = random(-3.0, 3.0)
    vely = random(-3.0, 3.0)
    
def draw(): # es exactamente igual que while true:
    global x, y, velx, vely, rojo
    #background(200, 200, 255)
    x+=velx
    y+=vely
    #x= mouseX
    #y= mouseY
    
    noStroke()
    rojo = map(x, 0, width, 0, 255) + extra_rojo
    verde = map(y, 0, height, 0, 255) + extra_verde
    azul = map(((y+x)/2), 0, (width+height)/2, 0, 255) + extra_azul
    fill(rojo, verde, azul) #r,g,b
    circle(x, y, r) #x, y, d
    
    print(rojo, extra_rojo)
    
    if x >= width-r/2 or x<=r/2:
        velx = -velx
    if y >= height-r/2 or y<=r/2:
        vely = -vely

def mousePressed():
    global r
    r+=2
    
def keyPressed():
    global r, x, y, extra_rojo, extra_azul
    if key == 'W' or key == 'w' and r>4:
        r-=2
    if key == 'Q' or key == 'q':
        background(col_back)
        x = width//2
        y = height//2
        
    if (key == 'R' or key == 'r') and rojo + extra_rojo<=255:
        extra_rojo+=5
    if key == 'A' or key == 'a':
        extra_azul+=5
    if key == 'V' or key == 'v':
        extra_verde+=5
