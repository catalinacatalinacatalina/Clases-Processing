secuencia = [] # los datos que tiene que meter el jugador
entrada = []   # los datos que va metiendo el jugador
margin = 20
e2 = 5
n = 2
my = 100 # margen superior

ciclo = 0


AZUL = color(100, 100, 255)
AZUL_BRILLANTE = color(150, 150, 255)
VERDE = color(100, 255, 100)
VERDE_BRILLANTE = color(150, 255, 150)
ROJO = color(255, 90, 90)
ROJO_BRILLANTE = color(255, 150, 150)
AMARILLO = color(255, 255, 100)
AMARILLO_BRILLANTE = color(255, 255, 170)

rojo_act = ROJO
azul_act = AZUL
verde_act = VERDE
amarillo_act = AMARILLO

def setup():
    size(800, 900)
    global tamano
    tamano = (width-margin*2-e2)/2
    rectMode(CENTER)
    secuencia.append(int(random(0, 4))) # anado un boton random en la secuencia
def draw():
    background(30)
    dibujarBotones()
    
def dibujarBotones():
    
    #azul
    fill(azul_act)
    square(margin + tamano/2, my+ tamano/2, tamano)
        
    # verde
    fill(verde_act)
    square(margin + tamano*3/2 + e2,  my+ tamano/2, tamano)
    
    # amarillo
    fill(amarillo_act)
    square(margin + tamano/2,  my + tamano*3/2+ e2, tamano)

    #rojo
    fill(rojo_act)
    square(margin + tamano*3/2 + e2,  my + tamano*3/2+ e2, tamano)


def mousePressed():
    
    boton_clickado = -1
    if primera_col():
        if primera_fila():
            print("azul")
            iluminar(0)
            boton_clickado = 0
        elif segunda_fila():
            print("amarillo")
            iluminar(2)
            boton_clickado = 2
        
    elif segunda_col():
        if primera_fila():
            print("verde")
            iluminar(1)
            boton_clickado = 1

        elif segunda_fila():
            print("clickaste el rojo")
            iluminar(3)
            boton_clickado = 3
    
    # si se ha clicado un boton -> check que sea el que toca
    if not(boton_clicado == -1):
        if(secuencia[i] == entrada[i]):
            print("siguiente fase")
        else:
            print("perdido")
        

def primera_col():
    return margin < mouseX and mouseX< tamano + margin
    
def segunda_col():
    return margin + tamano + e2 < mouseX and mouseX<width-margin

def primera_fila():
    return my < mouseY and mouseY < my + tamano

def segunda_fila():
    return my + tamano + e2 < mouseY and mouseY< 2*tamano + my + e2



def iluminar(boton):
    global azul_act, verde_act, amarillo_act, rojo_act
    
    if boton == 0:
         azul_act = AZUL_BRILLANTE
    elif boton == 1:
        verde_act = VERDE_BRILLANTE
    elif boton == 2:
        amarillo_act = AMARILLO_BRILLANTE
    elif boton == 3:
        rojo_act = ROJO_BRILLANTE

def mouseReleased():
    global azul_act, verde_act, amarillo_act, rojo_act
    azul_act =  AZUL
    verde_act = VERDE
    amarillo_act = AMARILLO
    rojo_act = ROJO
