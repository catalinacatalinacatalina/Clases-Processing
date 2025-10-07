x = 100
y = 100
vel = 2
vely = 3
col = 0;
diametro = 50;
velCol =0.1;
col_back = None

redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0;

def setup():
    # solo se ejecuta una vez
    #size(1000,800)#x,y
    fullScreen()
    # width, height
    colors()
    
    background(col_back);#red, green, blue
    
def draw(): # = while(true)
    # se ejecuta en bucle
    global col
    global x, vel, y, vely
    rectMode(CENTER)

    # calcular color
    r = int(random(redMin,redMax));
    g = int(random(greenMin, greenMax))
    b = int(random(blueMin, blueMax))
    fill(r,g,b) # R, G, B
    noStroke()
    
    #aumento velocidades
    x = x+vel
    y = y+vely
    
    #display
    circle(x, y, diametro) #circle(x,y,r)
    
    
    #rebote
    if x>width-diametro/2 or x<diametro/2: # ha llegado a borde
        vel = -vel
    
    if y>height-diametro/2 or y<diametro/2:
        vely = -vely
        

def colors():
    global redMin, redMax, greenMin, greenMax, blueMin, blueMax
    global col_back
    greenMin = int(random(0, 255))
    greenMax = int(random(greenMin, 255))
    blueMin  = int(random(0, 255))
    blueMax  = int(random(blueMin, 255))
    redMin   = int(random(0, 255))
    redMax   = int(random(redMin, 255))
    
    print("Nueva paleta:")
    print("green:", greenMin, "-", greenMax)
    print("red:  ", redMin, "-", redMax)
    print("blue: ", blueMin, "-", blueMax)
    
    #componentes
    diferencia = 50
    r_back = int(random(redMin,redMax)) - diferencia
    g_back = int(random(greenMin, greenMax)) - diferencia
    b_back = int(random(blueMin, blueMax)) - diferencia
    
    col_back = color(r_back, g_back, b_back)
    background(col_back)

    
def mousePressed():
    colors()
    
    
def keyPressed():
    background(220, 240, 120)
