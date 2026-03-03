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
    
    #actualizo
    for i in range (FILAS):
        for j in range (COLUMNAS):
            grid[i][j].aplicar_actualizacion()
            

def mouseMoved():
    i = mouseY // TAM
    j = mouseX // TAM
    
    if i>=0 and i< FILAS and j>=0 and j< COLUMNAS:
        grid[i][j].toggle()
