from random import uniform

class Objeto:
    def __init__(self, tipo, x, y, width, height, imagenes):
        self.tipo = tipo  # "Piedra", "Papel" o "Tijera"
        self.x = x
        self.y = y
        self.vx = uniform(-2, 2)
        self.vy = uniform(-2, 2)
        self.tam = 50
        self.width = width
        self.height = height
        self.imagenes = imagenes  # Diccionario de imagenes: {"Piedra": img1, ...}

    def mover(self):
        # Mueve el objeto y rebota en los bordes
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > self.width:
            self.vx *= -1
        if self.y < 0 or self.y > self.height:
            self.vy *= -1

    def mostrar(self):
        # Dibuja la imagen correspondiente
        img = self.imagenes[self.tipo]
        imageMode(CENTER)
        image(img, self.x, self.y, self.tam, self.tam)

    def interactuar(self, otro):
        # Comprueba si colisionan y aplica las reglas
        distancia = dist(self.x, self.y, otro.x, otro.y)
        if distancia < (self.tam + otro.tam) / 2:
            ganador = self.ganar(otro.tipo)
            if ganador == 1:
                otro.tipo = self.tipo
            elif ganador == -1:
                self.tipo = otro.tipo

    def ganar(self, otro_tipo):
        # Devuelve 1 si self gana, -1 si pierde, 0 si empate
        reglas = {
            "Piedra": "Tijera",
            "Tijera": "Papel",
            "Papel": "Piedra"
        }
        if self.tipo == otro_tipo:
            return 0
        elif reglas[self.tipo] == otro_tipo:
            return 1
        else:
            return -1
