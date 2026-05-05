GRID_SIZE = 5
CELL_SIZE = 40

OFFSET_X = 140
OFFSET_Y = 140

board = []
rowHints = []
colHints = []

def setup():
    llena_tablero()

def draw():
    pass

def llena_tablero():
    global board

    for i in range (GRID_SIZE):
        fila = []
        # crear fila
        for j in range(GRID_SIZE):
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
    for i in range(GRID_SIZE):  # para cada fila
        pistas = []             # pistas en esta fila
        contador = 0
        for j in range(GRID_SIZE): # para cada casilla en esta fila
            if board[j][i].solucion == 1: # AZUL
                contador+=1
            else:
                if contador>0:
                    pistas.append(contador)
                    contador = 0
        if len(pistas)==0:
            pistas.append(0)

        rowHints.append(pistas)

    # buscamos por colummnas
