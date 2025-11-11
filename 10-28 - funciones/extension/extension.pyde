nb = 10
margin = 40
dim = 0
colores = list()

def setup():
    size(700, 700)
    global dim
    dim = (width - 2*margin) / nb
    noLoop()
    generar_colores()
    noStroke()

def draw():
    background(230)
    for j in range(nb):
        dibujar_fila(j)

def dibujar_celda(x, y, tam, col):
    fill(col[0], col[1], col[2])
    circle(x + tam/2, y + tam/2, tam*0.8)

def generar_colores():
    global colores
    colores = []  # elimina el contenido pero mantiene la lista
    for i in range(5):
        colores.append((random(255), random(255), random(255)))

def dibujar_fila(j):
    print("fila", j)
    for i in range(nb):
        x = margin + i*dim
        y = margin + j*dim
        dibujar_celda(x, y, dim, colores[(i + j) % len(colores)])

def keyPressed():
    print("pressed")
    generar_colores()
    redraw()
