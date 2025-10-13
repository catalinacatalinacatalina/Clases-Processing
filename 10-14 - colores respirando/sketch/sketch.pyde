redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
y = 0  #posición fija en Y (centro)
numCirculos = 5
vel = 3
suma_col =-100

def setup():
    size(1600, 400)
    noStroke()
    colors()  # inicializar paleta
    global color_back, suma_col, y
    y = height/2
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
def draw():
    global x
    
    background(color_back)  # limpiar pantalla cada frame
    
    # repartir los círculos en Y
    for i in range(numCirculos):
        # posición Y repartida uniformemente
        x = map(i, 0, numCirculos-1, 100, width-100)
        
        radio = map(sin(frameCount * 0.05 + i), -1, 1, 30, 150)
        
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
    
    print("Nueva paleta 🎨")
    print("green:", greenMin, "-", greenMax)
    print("red:  ", redMin, "-", redMax)
    print("blue: ", blueMin, "-", blueMax)


def keyPressed():
    colors()
    global color_back, suma_col

    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
