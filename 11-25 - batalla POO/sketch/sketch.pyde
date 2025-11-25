from persona import Persona

def setup():
    size(600, 400)
    global p1, p2, turno
    p1 = Persona("Juan", 100, 10, width/3, color(100,200,233))
    p2 = Persona("Manolo", 70, 12, 2*width/3, color(245,100,233))
    turno = 1
    
def draw():
    background(0)
    p1.dibujar()
    p2.dibujar()
    
    textSize(32)
    # si alguien pierde:
    if p1.vida<=0:
        texto = p1.nombre + " ha perdido"
        text(texto, width/2, 360)
        noLoop()
    if p2.vida<=0:
        texto = p2.nombre + " ha perdido"
        text(texto, width/2, 360)
        noLoop()
    
def keyPressed():
    global turno
    if key == ' ':
        if turno == 1:
            #ataca jugador 1
            p1.atacar(p2)
            turno = 2
        else:
            #ataca jugador 2
            p2.atacar(p1)
            turno = 1
