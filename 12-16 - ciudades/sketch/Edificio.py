class Edificio:
    def __init__(self, x, y, h2):
        self.x = x
        self.y = y
        self.h2 = h2 #altura de cada piso
        
        self.n = int(random(10,100)) # numero de pisos
        self.w = random(100, 150)
        self.c1 = int(random(10, 100))
        self.c2 = int(random(0, 255))
        self.c3 = int(random(0, 255))
                
    def show(self):
        noStroke()
        fill(self.c1, self.c2, self.c3)
        
        # tapa
        beginShape()
        vertex(self.x - self.w/2, self.y - self.h2)
        vertex(self.x, self.y - 2*self.h2)
        vertex(self.x + self.w/2, self.y - self.h2)
        vertex(self.x, self.y)
        vertex(self.x - self.w/2, self.y - self.h2)
        endShape()
        
        # cuerpo
        aux_c1 = self.c1
        aux_c2 = self.c2
        aux_c3 = self.c3
        for i in range(self.n):
            aux_c1 -= 15
            aux_c2 -= 15
            aux_c3 -= 15
            fill(aux_c1, aux_c2, aux_c3)
            
            beginShape()
            vertex(self.x, self.y + self.h2*i)
            vertex(self.x - self.w/2, self.y + self.h2*i - self.h2)
            vertex(self.x - self.w/2, self.y + self.h2*i)
            vertex(self.x, self.y + self.h2*i + self.h2)
            vertex(self.x + self.w/2, self.y + self.h2*i)
            vertex(self.x + self.w/2, self.y + self.h2*i - self.h2)
            vertex(self.x, self.y + self.h2*i)
            endShape()
