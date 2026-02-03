FILAS = 3
COLUMNAS = 3
TAM = 120
turno = 1
ganador = 0

def setup():
    size(FILAS*TAM, COLUMNAS*TAM)
    textAlign(CENTER, CENTER)
    textSize(64)
    strokeWeight(3)
    
    global tablero
    tablero = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(0)
        tablero.append(fila)

    
def draw():
    background(255)
    dibujar_tablero()
    dibujar_fichas()

def mousePressed():
    # marcamos elemento array en funcion de raton
    global turno, ganador
    
    if ganador == 0: #no hay aun ganador -> marco la casilla
        # miramos donde esta el raton
        fila = mouseY//TAM
        col  = mouseX//TAM
        print(fila, " ", col)
        
        if tablero[fila][col]==0: #si elemento esta vacio
            tablero[fila][col] = turno # llenamos
            if turno ==1: 
                turno=2
            else:
                turno=1
            comprobar_ganador()
            
def comprobar_ganador():
    global ganador
    #comprobar todas las filas
    i = 0
    while i<FILAS and ganador == 0:
        if tablero[i][1] == tablero[i][2] == tablero[i][0]:
            ganador = tablero[i][0]
        i+=1
    
    #comprobar columnas
    j = 0
    while i<COLUMNAS and ganador == 0:
        if tablero[0][j] == tablero[1][j] == tablero[2][j]:
            ganador = tablero[0][j]
        j+=1
    
    # comprobar diagonales
    if ganador == 0 and tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        ganador = tablero[0][0]
    elif ganador == 0 and tablero[0][2] ==  tablero[1][1] ==  tablero[2][0]!=0:
        ganador = tablero[1][1]
        

    # mirar si el tablero esta lleno -> busqueda de un elemento que sea 0
    if ganador == 0:
        i = 0
        lleno = True
        while i<FILAS and lleno:
            j = 0
            while j<COLUMNAS and lleno:
                #miro la casilla i,j
                if tablero[i][j] == 0:
                    lleno = False
                j+=1
            i+=1
        
        if lleno:
            print("empate")
    else:
        print("ganador", ganador)
    

def dibujar_fichas():
    # recorrer lista
    for i in range(FILAS):
        for j in range(COLUMNAS):
            #DONDE VOY A PONER EL TEXTO DE X/O
            x = j * TAM + TAM/2
            y = i * TAM + TAM/2
            
            if tablero[i][j] == 1:
                if turno == 1:
                    fill(0,0,255)
                else:
                    fill(42, 43, 43)
                text("X", x, y)
            elif tablero[i][j] == 2:
                
                fill(255,0,0)
                text("O", x, y)
            
def dibujar_tablero():

    for i in range(1, COLUMNAS):
        line(0, i*TAM, width, i*TAM)
    
    for i in range(1, FILAS):
        line(i*TAM, 0, i*TAM, height)
