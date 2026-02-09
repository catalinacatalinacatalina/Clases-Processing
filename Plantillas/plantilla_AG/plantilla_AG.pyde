from Color import Color

numColors = 20
generacion = 0
numSelected = numColors/2

tasaMutacion = 0.4

poblacion = []
descendientes = []
mejores = []
cruzados = []

evaluacion = []       # Fitness de cada individuo (distancia al objetivo)
mejoresPosiciones = []# Índices de los mejores individuos
mutados = []          # Marca qué individuos han mutado


# Variables para visualización
wItem = 0
hItem = 0
terminado = False
target = None




def setup():
    global target
    size(1600, 900)
    target = Color(255, 225, 0)
    inicializar(numColors)


def draw():
    global generacion

    background(255)
    evaluar()

    if not esTerminado():
        # esquema básico de un algoritmo genético:
        seleccionar()
        cruzar()
        mutar()
        display()
        generacion += 1
        setNextGen()
        noLoop()
    else:
        display()


# =========================
# ALGORITMO GENÉTICO
# =========================

def inicializar(num):
    pass

def evaluar():
    pass

def seleccionar():
    pass

def cruzar():
    pass

def mutar():
    pass

def esTerminado():
    pass


def getBestPosition(exclude=None):

    bestEval = float('inf')
    bestPos = -1

    for i in range(len(evaluacion)):
        if evaluacion[i] < bestEval:
            if exclude is None or i not in exclude:
                bestEval = evaluacion[i]
                bestPos = i

    return bestPos


def getBestPositions(n):
    positions = []
    for _ in range(n):
        p = getBestPosition(positions)
        positions.append(p)
    return positions


def setNextGen():
    pass


# =========================
# DISPLAY
# =========================

def display():

    fill(0)
    textSize(44)
    textAlign(CENTER)

    if terminado:
        fill(0, 255, 0)
        text("¡ENCONTRADO!", width/2, height-50)
        fill(0)
        noLoop()

    text("GENERACION " + str(generacion), width/2, 60)

    displayColores(poblacion, 80)

    textSize(18)
    text("Evaluacion", width/2, 182)
    displayEvaluacion(185)

    text("Seleccion", width/2, 285)
    displayMejores(288)

    text("Cruzamiento", width/2, 385)
    displayColores(cruzados, 390)

    text("Mutacion (" + str(tasaMutacion) + ")", width/2, 495)
    displayMutados(500)

    text("Descendientes", width/2, 605)
    displayColores(descendientes, 610)


def displayColores(array, y):
    for i in range(len(array)):
        array[i].display(i*wItem + 5 + wItem/2,
                         y + hItem/2,
                         wItem, hItem)


def displayEvaluacion(y):
    for i in range(len(evaluacion)):
        pushStyle()
        rectMode(CORNER)
        fill(255)
        rect(i*wItem + 5, y, wItem, hItem)
        fill(0)
        textSize(12)
        textAlign(CENTER)
        text(str(round(evaluacion[i], 2)),
             i*wItem + 5 + wItem/2,
             y + hItem/2)
        popStyle()


def displayMejores(y):
    for i in range(len(mejores)):
        pushStyle()
        c = mejores[i]
        n = mejoresPosiciones[i]
        fill(c.getColor())
        rectMode(CORNER)
        rect(n*wItem + 5, y, wItem, hItem)
        popStyle()


def displayMutados(y):
    for i in range(len(mutados)):
        pushStyle()
        if mutados[i]:
            fill(255, 0, 0)
        else:
            fill(255)
        rectMode(CORNER)
        rect(i*wItem + 5, y, wItem, hItem)
        popStyle()


# =========================
# CONTROLES
# =========================

def keyPressed():
    global terminado, generacion

    if key == 'd' or key == 'D':
        loop()

    elif key == ' ':
        terminado = False
        generacion = 0
        inicializar(numColors)
        loop()
