from pelota import Pelota

redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
suma_col = -50
bolas = []

# programa principal


def setup():
    size(1600, 800)
    colors()
    global color_back, suma_col
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
    
    for i in range(10):
        r = int(random(redMin, redMax))
        g = int(random(greenMin, greenMax))
        b = int(random(blueMin, blueMax))
        color_1 = color(r, g, b)
        bolas.append(Pelota(random(1, width), random(1, height),
                               random(5, 10), random(5,10), color_1))

def draw():
    background(color_back) # n <==> n,n,n
    
    # dibuja hilos
    for i in range(10):
        for j in range (i+1, 10): #(donde empieza j, donde termina-1)
            if(dist(bolas[i].x, bolas[i].y, bolas[j].x, bolas[j].y)<400):
                stroke(255)
                line(bolas[i].x, bolas[i].y, bolas[j].x, bolas[j].y)
    
    # dibuja pelotas
    for b in bolas:
        b.mover()
        b.dibujar()
    
    
def colors():
    global redMin, redMax, greenMin, greenMax, blueMin, blueMax
    greenMin = int(random(0, 255))
    greenMax = int(random(greenMin, 255))
    blueMin  = int(random(0, 255))
    blueMax  = int(random(blueMin, 255))
    redMin   = int(random(0, 255))
    redMax   = int(random(redMin, 255))
    
    print("Nueva paleta 🎨")
    print("green:", greenMin, "-", greenMax)
    print("red:  ", redMin, "-", redMax)
    print("blue: ", blueMin, "-", blueMax)
    
def mousePressed():
    
    i = 0
    bola_clicada = False

    # si yo quiero -> recorrer toda la lista -> for
    # si yo BUSCO -> while
    while(i<len(bolas) and not bola_clicada):
        
        if bolas[i].enPosicion(mouseX, mouseY):
            bolas[i].cambio_color()
            bola_clicada = True
        i+=1
    # se termina o cuando i llega a la longitud de la lista o cuando bola_clicada se pone a true
