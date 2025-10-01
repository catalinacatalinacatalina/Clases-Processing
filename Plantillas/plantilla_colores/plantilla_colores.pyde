redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
suma_col = -50
def setup():
    size(800, 800)
    colors()  # inicializar paleta
    global color_back, suma_col
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
def draw():
    background(color_back)  # limpiar pantalla cada frame

    # color aleatorio dentro de la paleta
    r = int(random(redMin, redMax))
    g = int(random(greenMin, greenMax))
    b = int(random(blueMin, blueMax))
    fill(r, g, b)
    noStroke();
    circle(width/2, height/2, 50)

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
