from Objeto import Objeto
from random import choice, uniform

WIDTH = 800
HEIGHT = 600
NUM_OBJETOS = 20
objetos = []
imagenes = {}

def setup():
    global objetos, imagenes
    size(WIDTH, HEIGHT)

    # Cargar imágenes
    imagenes["Piedra"] = loadImage("piedra.png")
    imagenes["Papel"] = loadImage("papel.png")
    imagenes["Tijera"] = loadImage("tijera.png")

    tipos = ["Piedra", "Papel", "Tijera"]
    for i in range(NUM_OBJETOS):
        tipo = choice(tipos)
        x = uniform(0, WIDTH)
        y = uniform(0, HEIGHT)
        objetos.append(Objeto(tipo, x, y, WIDTH, HEIGHT, imagenes))

def draw():
    background(50, 150, 200)  # cielo azul
    
    # Mover y mostrar todos
    for obj in objetos:
        obj.mover()
        obj.mostrar()
    
    # Comprobar interacciones
    for i in range(len(objetos)):
        for j in range(i+1, len(objetos)):
            objetos[i].interactuar(objetos[j])
