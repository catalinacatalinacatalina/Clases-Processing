"""

n = 25
def suma_digitos(n):
     suma = 0
     # operaciones
     
     while n>0:
         suma += n%10 # a la suma le añado el ultimo digito
         n//=10 # <--> n= n//10
     
     return suma

print(suma_digitos(n))
"""
nb = 10
margin = 40
dim = 0
color_ = list()

def setup():
    size(700, 700)
    global dim
    dim = (width - margin*2) / nb  # el espacio que hay entre dos bolas
    noLoop()
    noStroke()
    generar_colores()
    rectMode(CENTER)

def draw():
    #linea(100)
    cuadricula()
    
def dibujar_circulo(x, y):
    fill(color_[0], color_[1], color_[2])
    circle(x, y, 20)
    
def linea(y):
    for i in range(nb):
        x = margin + i*dim + dim/2
        dibujar_circulo(x, y)

def cuadricula():
    for j in range(nb):
        y = margin + j*dim + dim/2
        linea(y)
    
def generar_colores():
    global color_
    color_ = []
    for i in range(3):
        color_.append(random(255))
        
def keyPressed():
    generar_colores()
    redraw()
