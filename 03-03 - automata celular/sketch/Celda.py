from random import randint

class Celda:
    def __init__(self, i, j, tamano):
        self.i = i
        self.j = j
        self.tamano = tamano
        self.viva = bool(randint(0,1))
        self.prox_estado = self.viva

    def dibujar(self):
        if self.viva:
            fill(0)
        else:
            fill(255)
        stroke(200)
        rect(self.j*self.tamano, self.i*self.tamano, self.tamano, self.tamano)
        
    def actualizar(self, grid, filas, columnas):
        vecinas_vivas = self.contar_vecinas(grid, filas, columnas) # devolvera cuantas casillas vecinas estan vivas
        
        if self.viva and (vecinas_vivas == 2 or vecinas_vivas==3):
            self.prox_estado = True
        elif not self.viva and vecinas_vivas==3:
            self.prox_estado = True
        else:
            self.prox_estado = False
            
    def aplicar_actualizacion(self):
        self.viva = self.prox_estado
        
    def contar_vecinas(self, grid, filas, columnas):
        vivas = 0
        
        # superior izq
        if self.i >0 and self.j >0 and grid[self.i-1][self.j-1].viva:
            vivas+=1
        
        # Vecina superior
        if self.i-1>=0 and grid[self.i-1][self.j].viva:
            vivas+=1

        # Vecina superior derecha
        if self.i>0 and self.j<columnas-1 and grid[self.i-1][self.j+1].viva:
            vivas+=1
            
        # Vecina izquierda
        if self.j > 0 and grid[self.i][self.j-1].viva:
            vivas += 1
        
        # Vecina derecha
        if self.j < columnas-1 and grid[self.i][self.j+1].viva:
            vivas += 1
        
        # Vecina inferior izquierda
        if self.i < filas-1 and self.j > 0 and grid[self.i+1][self.j-1].viva:
            vivas += 1
        
        # Vecina inferior
        if self.i < filas-1 and grid[self.i+1][self.j].viva:
            vivas += 1
        
        # Vecina inferior derecha
        if self.i < filas-1 and self.j < columnas-1 and grid[self.i+1][self.j+1].viva:
            vivas += 1
        
        return vivas
    
    def toggle(self):
        self.viva = not self.viva
