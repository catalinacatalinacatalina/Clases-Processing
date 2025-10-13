# -------------------------------
# Plantilla para clase 14/10 — Ondas de color
# -------------------------------

# Variables globales
redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
vel = 3
suma_col = -100

def setup():
    size(1600, 400)
    noStroke()
    colors()  # paleta inicial

    global color_back, y
    y = height / 2  # posición fija
    
    # color de fondo inicial (dentro de la paleta)
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )

def draw():
    background(color_back)
    
    # aqui haremos nuestros bucles y nuestras cosas

def colors():
    """Genera una paleta aleatoria (valores min y max por canal)"""
    global redMin, redMax, greenMin, greenMax, blueMin, blueMax
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

def keyPressed():
    """Cambia la paleta y el color de fondo"""
    colors()
    global color_back, suma_col
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
