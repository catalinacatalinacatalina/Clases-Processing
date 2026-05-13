import Config
from Casilla import Casilla

board = []
rowHints = []
colHints = []

def setup():
    size(500, 500)
    llena_tablero()

def draw():
    dibujarPistas()
    dibujarTablero()
    
def llena_tablero():
    global board

    for i in range(Config.GRID_SIZE):
        fila = []
        # crear fila
        for j in range(Config.GRID_SIZE):
            solucion = 1
            if random(1)< 0.45:
                solucion = 2

            cel =  Casilla(j, i, solucion)
            fila.append(cel)

        board.append(fila)

    generarPistas()

def generarPistas():
    global colHints, rowHints
    # buscamos las pistas por filas
    blanco_ant = False
    for i in range(Config.GRID_SIZE):  # para cada fila
        pistas = []             # pistas en esta fila
        contador = 0
        for j in range(Config.GRID_SIZE): # para cada casilla en esta fila
            if board[i][j].solucion == 1: # AZUL
                contador+=1
            else:
                if contador>0:
                    pistas.append(contador)
                    contador = 0
        if contador > 0:
            pistas.append(contador)
        if len(pistas)==0:
            pistas.append(0)

        rowHints.append(pistas)
        
    # buscamos por colummnas
        for x in range(Config.GRID_SIZE):

            pistas = []
            contador = 0
    
            for y in range(Config.GRID_SIZE):
    
                if board[y][x].solucion == 1:
                    contador += 1
    
                else:
                    if contador > 0:
                        pistas.append(contador)
                        contador = 0
    
            if contador > 0:
                pistas.append(contador)
    
            if len(pistas) == 0:
                pistas.append(0)

        colHints.append(pistas)
        
        
def dibujarTablero():
    for y in range(Config.GRID_SIZE): # para cada fila 
        for x in range(Config.GRID_SIZE): # para cada elemento de esa fila
            board[y][x].dibujar()

def dibujarPistas(): #[[1,2,3], [2, 4, 1] .... ]
    fill(0)
    textSize(18)
    
    # pintamos las filas
    for y in range(Config.GRID_SIZE):
        texto =  " ".join(str(n) for n in rowHints[y])
        text(texto, Config.OFFSET_X - 50, Config.OFFSET_Y + y* Config.CELL_SIZE + Config.CELL_SIZE/2)
        
    # Columnas
    for x in range(Config.GRID_SIZE):
        texto = "\n".join(str(n) for n in colHints[x])
        text(texto,
             Config.OFFSET_X + x * Config.CELL_SIZE + Config.CELL_SIZE / 2,
             Config.OFFSET_Y - 50)

def mousePressed():
    gridX = (mouseX - Config.OFFSET_X)// Config.CELL_SIZE
    gridY = (mouseY - Config.OFFSET_Y)// Config.CELL_SIZE
    
    
    
