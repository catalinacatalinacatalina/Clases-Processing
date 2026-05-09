secuencia = [] # los datos que tiene que meter el jugador
entrada = []   # los datos que va metiendo el jugador
margin = 20
e2 = 5
n = 2
my = 100

AZUL = color(100, 100, 255)
AZUL_BRILLANTE = color(130, 130, 255)
VERDE = color(100, 255, 100)
VERDE_BRILLANTE = color(120, 255, 120)
ROJO = color(255, 100, 100)
ROJO_BRILLANTE = color(255, 120, 120)
AMARILLO = color(255, 255, 100)
AMARILLO_BRILLANTE = color(255, 255, 140)

rojo_act = ROJO

def setup():
    size(800, 900)
    global tamano
    tamano = (width-margin*2-e2)/2
    rectMode(CENTER)
def draw():
    background(30)
    dibujarBotones()
    
def dibujarBotones():
    
    #azul
    fill(AZUL)
    square(margin + tamano/2, my+ tamano/2, tamano)
        
    # verde
    fill(VERDE)
    square(margin + tamano*3/2 + e2,  my+ tamano/2, tamano)
    
    # amarillo
    fill(AMARILLO)
    square(margin + tamano/2,  my + tamano*3/2+ e2, tamano)

    #rojo
    fill(rojo_act)
    square(margin + tamano*3/2 + e2,  my + tamano*3/2+ e2, tamano)


def keyPressed():
    if key == 'r' or key == 'R':
        # si estoy en rojo -> me voy al brillante
        # si estoy en brillante -> me voy al normal
        if rojo_act == ROJO:
            rojo_act = ROJO_BRILLANTE
        else:
            rojo_act = ROJO
            
        
