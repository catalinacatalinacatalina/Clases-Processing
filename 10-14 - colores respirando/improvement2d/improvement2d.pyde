redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
circulosX = 5
circulosY = 5
vel = 0.05
suma_col =-100

def setup():
    size(1600, 1000)
    noStroke()
    colors()  # inicializar paleta
    global color_back, suma_col
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
def draw():
    
    background(color_back)  # limpiar pantalla cada frame
    
    # repartir los círculos en Y
    for j in range(circulosY):
        y = map(j, 0, circulosY-1, 100, height-100);
        for i in range(circulosX):
            # posición Y repartida uniformemente
            x = map(i, 0, circulosX-1, 100, width-100)
            
            # aqui al explicar quitar el desfase
            desfase = (i+j)/2;
            radio = map(sin(frameCount * vel + desfase), -1, 1, 30, 150)
            
            # color aleatorio dentro de la paleta
            r = int(random(redMin, redMax))
            g = int(random(greenMin, greenMax))
            b = int(random(blueMin, blueMax))
            fill(r, g, b)
                        
            circle(x, y, radio)

def colors():
    global redMin, redMax, greenMin, greenMax, blueMin, blueMax
    greenMin = int(random(0, 255))
    greenMax = int(random(greenMin, 255))
    blueMin  = int(random(0, 255))
    blueMax  = int(random(blueMin, 255))
    redMin   = int(random(0, 255))
    redMax   = int(random(redMin, 255))
    
    print("Nueva paleta")
    print("green:", greenMin, "-", greenMax)
    print("red:  ", redMin, "-", redMax)
    print("blue: ", blueMin, "-", blueMax)


def keyPressed():
    colors()
    global color_back
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
