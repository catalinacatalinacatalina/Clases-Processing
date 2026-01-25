import py5 as p

class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.texto = texto
        self.color = (100, 150, 255)
        self.color_hover = (50, 100, 200)
        self.clickeado = False
    
    def mostrar(self):
        # Cambiar color si el ratón está sobre el botón
        if self.dentro():
            p.fill(*self.color_hover) # el operador * hace que (r, g, b) se convierta en (r), (g), (b)
        else:
            p.fill(*self.color)
        
        p.rect(self.x, self.y, self.ancho, self.alto)
        
        # Dibujar texto
        p.fill(255)
        p.text_align(p.CENTER, p.CENTER)
        p.text(self.texto, self.x + self.ancho/2, self.y + self.alto/2)
    
    def dentro(self):
        return (self.x < p.mouse_x < self.x + self.ancho and
                self.y < p.mouse_y < self.y + self.alto)
    
    def presionado(self):
        if self.dentro():
            self.clickeado = True
            return True
        return False
