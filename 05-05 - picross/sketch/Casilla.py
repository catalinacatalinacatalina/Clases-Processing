class Casilla:
    def __init__(self, x, y, solucion):
        self.x = x
        self.y = y
        self.solucion = solucion # EL VALOR QUE TIENE QUE ESTAR PARA QUE EL PUZLE ESTE BIEN
        self.estado = 0 # 0 = vacio, 1 = encendido, 2 = apagado

    def dibujar(self):
        px = OFFSET_X + self.x * CELL_SIZE
        py = OFFSET_Y + self.y * CELL_SIZE
        stroke(0)
        strokeWeight(1)
        # opcion 1 --> blanca
        if self.estado == 0:
            fill(245, 225, 240)
        # opcion 2 --> azul
        elif self.estado == 1:
            fill(100, 100, 255)
        # opcion 3 --> apagado 
        else:
            fill(120)

        square(px, py, CELL_SIZE)