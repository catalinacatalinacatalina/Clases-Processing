# -----------------------------
# Clase Luz
# -----------------------------
class Luz:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.encendida = False
    
    def set_electricidad(self, b): #setter
        self.encendida = b
    
    def dibujar(self):
        if self.encendida:
            fill(self.color[0], self.color[1], self.color[2])
        else:
            fill(80)
        
        ellipse(self.x, self.y, 30, 30)


estado = "ROJO"
bus = False

cambio_estado = False
tiempo_estado = 0
siguiente = "VERDE"

# -----------------------------
def setup():
    size(400, 300)
    global luz_roja, luz_amarilla, luz_verde
    luz_roja = Luz(200, 110, (255, 0, 0))
    luz_amarilla = Luz(200, 150, (255, 255, 0))
    luz_verde = Luz(200, 190, (0, 255, 0))
    

# -----------------------------
def draw():
    global estado, bus, tiempo_estado, cambio_estado, siguiente, luz_roja, luz_amarilla, luz_verde
    
    background(30)
    
    # dibujar carcasa
    fill(50)
    rect(180, 80, 40, 140, 10)

    # -------- MAQUINA DE ESTADOS --------
    print(tiempo_estado)
    if estado == "ROJO":
        # start
        if cambio_estado:
            tiempo_estado = 0
            cambio_estado = False
        
        #update
        luz_roja.set_electricidad(True)
        luz_amarilla.set_electricidad(False)
        luz_verde.set_electricidad(False)
        
        tiempo_estado+=1
        
        # transit (cambio de estado)
        if bus:
            estado = "VERDE"
            cambio_estado = True
            bus = False
        elif tiempo_estado >500:
            estado = "AMARILLO"
            cambio_estado = True
            siguiente = "VERDE"

        
    elif estado == "AMARILLO":
        # start
        if cambio_estado:
            tiempo_estado = 0
            cambio_estado = False
        
        #update
        luz_roja.set_electricidad(False)
        luz_amarilla.set_electricidad(True)
        luz_verde.set_electricidad(False)
        
        tiempo_estado+=1
        
        # transit (cambio de estado)
        if bus:
            estado = "VERDE"
            cambio_estado = True
            bus = False
        elif tiempo_estado > 200:
            estado = siguiente
            if siguiente == "VERDE":
                siguiente = "ROJO"
            else:
                siguiente = "VERDE"
            cambio_estado = True
    elif estado == "VERDE":
        # start
        if cambio_estado:
            tiempo_estado = 0
            cambio_estado = False
        
        #update
        luz_roja.set_electricidad(False)
        luz_amarilla.set_electricidad(False)
        luz_verde.set_electricidad(True)
        
        tiempo_estado+=1
        
        # transit (cambio de estado)
        if tiempo_estado > 500:
            estado = "AMARILLO"
            siguiente = "ROJO"
            cambio_estado = True

    
    
    # -----------------------------------
    luz_roja.dibujar()
    luz_amarilla.dibujar()
    luz_verde.dibujar()


def keyPressed():
    global bus
    if key == 'b' or key == 'B':
        bus=True
