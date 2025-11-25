class Persona:
    def __init__(self, nombre, vida, fuerza, x, col):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.x = x     # posicion en pantalla
        self.col = col
        
    def dibujar(self):
        noStroke()
        fill(self.col)
        circle(self.x, 200, 120)

        # nombre
        fill(255)
        textAlign(CENTER)
        textSize(20)
        text(self.nombre, self.x, 280)
        
        # barra de vida
        fill(255)
        rect(self.x - 50, 300, 100, 15)
        fill(255,0,0)
        # apunte importante -> SUPONEMOS que la maxima vida es 100
        rect(self.x - 50, 300, self.vida, 15)
        
    def atacar(self, objetivo):
        print(self.nombre, "ataca a", objetivo.nombre)
        if random(1)<0.2:
            objetivo.vida = objetivo.vida - self.fuerza*2
            print("doble")
        else:
            objetivo.vida = objetivo.vida - self.fuerza    
        if(objetivo.vida<0):
            objetivo.vida = 0
        
