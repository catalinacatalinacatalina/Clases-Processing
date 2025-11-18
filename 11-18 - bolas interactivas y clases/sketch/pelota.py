
class Pelota:
    def __init__(self, x, y, dx, dy, col):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.tam = 100
        self.tam_base = 100
        self.col = col
        self.grande = False

    def mover(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > width - self.tam/2 or self.x <= self.tam/2:
            self.dx *= -1
        if self.y > height - self.tam/2 or self.y <= self.tam/2:
            self.dy *= -1

    def dibujar(self):
        noStroke()
        fill(self.col)
        circle(self.x, self.y, self.tam)

    def enPosicion(self, mx, my):
        d = dist(mx, my, self.x, self.y)
        return d <= self.tam/2

    def cambio_color(self):
        self.col = color(200, 200, 255)
        
        if self.grande:
            self.tam = self.tam_base * 0.5
            self.grande = False
        else:
            self.tam = self.tam_base * 1.5
            self.grande = True
