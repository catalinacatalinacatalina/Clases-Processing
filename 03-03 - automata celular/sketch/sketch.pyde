from Celda import Celda

TAM = 20
FILAS = 40
COLUMNAS = 40
grid = []

def setup():
    size(COLUMNAS * TAM, FILAS * TAM)
    global grid
    for i in range (FILAS):
        fila = []
        #llenamos esa fila
        for j in range (COLUMNAS):
            fila.append(Celda(i, j, TAM))
        grid.append(fila)
    
def draw():
    # dibujar cuadricula
    for i in range (FILAS):
        for j in range (COLUMNAS):
            grid[i][j].dibujar()
            
    #actualizo
    for i in range (FILAS):
        for j in range (COLUMNAS):
            grid[i][j].actualizar(grid, FILAS, COLUMNAS)
    
