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
