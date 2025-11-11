redMin = redMax = greenMin = greenMax = blueMin = blueMax = 0
color_back = None
suma_col = -50
bolas = []

class Pelota:
    # tam, x, y, dx, dy 
    def __init__(self, x, y, dx, dy, col): #constructor
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.tam = 100
        self.col = col
    
    
    def mover(self):
        self.x = self.x + self.dx #   <==>  self.x += self.dx
        self.y += self.dy 
        
        if self.x>width-self.tam/2 or self.x<=0+self.tam/2:
            self.dx *= -1 # <==> self.dx = self.dx * -1
        if self.y>height-self.tam/2 or self.y<=0+self.tam/2:
            self.dy *= -1
    
    def dibujar(self):
        noStroke()
        fill(self.col)
        circle(self.x, self.y, self.tam)

# programa principal


def setup():
    size(1600, 800)
    colors()
    global color_back, suma_col
    color_back = color(
        int(random(redMin, redMax)) + suma_col,
        int(random(greenMin, greenMax)) + suma_col,
        int(random(blueMin, blueMax)) + suma_col
    )
    
    for i in range(10):
        r = int(random(redMin, redMax))
        g = int(random(greenMin, greenMax))
        b = int(random(blueMin, blueMax))
        color_1 = color(r, g, b)
        bolas.append(Pelota(random(1, width), random(1, height),
                               random(5, 10), random(5,10), color_1))

def draw():
    background(color_back) # n <==> n,n,n
    
    # dibuja hilos
    for i in range(10):
        for j in range (i+1, 10): #(donde empieza j, donde termina-1)
            if(dist(bolas[i].x, bolas[i].y, bolas[j].x, bolas[j].y)<400):
                stroke(255)
                line(bolas[i].x, bolas[i].y, bolas[j].x, bolas[j].y)
    
    # dibuja pelotas
    for b in bolas:
        b.mover()
        b.dibujar()
    
    
def colors():
    global redMin, redMax, greenMin, greenMax, blueMin, blueMax
    greenMin = int(random(0, 255))
    greenMax = int(random(greenMin, 255))
    blueMin  = int(random(0, 255))
    blueMax  = int(random(blueMin, 255))
    redMin   = int(random(0, 255))
    redMax   = int(random(redMin, 255))
    
    print("Nueva paleta 🎨")
    print("green:", greenMin, "-", greenMax)
    print("red:  ", redMin, "-", redMax)
    print("blue: ", blueMin, "-", blueMax)
