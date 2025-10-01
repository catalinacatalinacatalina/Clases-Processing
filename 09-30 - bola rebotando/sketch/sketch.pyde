x = 2
y = 1
vel = 2
vely = 3
col = 0;

def setup():
    # solo se ejecuta una vez
    size(800,800)#x,y
    # width, height
    background(255, 170, 170);#red, green, blue
    
def draw(): # = while(true)
    # se ejecuta en bucle
    global col
    global x, vel, y, vely

    col=col+0.2;
    #background(255, 170, 170)# red, green, blue, transparencia
    rectMode(CENTER)
    fill(random(0,255)-col,random(0,255)-col,random(0,255)-col) # R, G, B
    noStroke()
    
    x = x+vel
    y = y+vely
    
    circle(x, y, 50) #circle(x,y,r)
    
    if x>width or x<0: # ha llegado a borde
        vel = -vel
    
    if y>height or y<0:
        vely = -vely
