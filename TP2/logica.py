import random

FILAS = 8
COLUMNAS = 8
PIEZAS = ("alfil", "caballo", "torre")
PIEZA_ACTIVA = "_rojo"

def lector_archivo_movimientos(ruta_origen):
    """
        Lee el archivo .csv en el que se hallan los movimientos, y devuelve un diccionario con
        los movimientos que puede realizar cada pieza. El formato de cada reglon del mismo debe ser
        'pieza, dir_x; dir_y, extensible'.
        dir_x: se mueve hacia la derecha si es positivo, hacia la izquierda si es negativo.
        dir_y: se mueve hacia abajo si es positivo, hacia arriba si es negativo.
        Extensible (Boolean): True si el movimiento puede repetirse hasta el fin del tablero, False de lo contrario.
        Pre: la ruta donde se encuentra el archivo movimientos.csv.
        Post: los movimientos válidos de cada pieza.
    """
    movimientos_piezas = {}
    with open (ruta_origen) as origen:
        for linea in origen:
            linea = linea.rstrip("\n").split(",")
            pieza = linea[0]
            movimientos = linea[1].split(";")
            movimientos[0] = int(movimientos[0])
            movimientos[1] = int(movimientos[1])
            extensible = linea[2]
            if extensible == "false":   extensible = ""
            movimientos_piezas[pieza] = movimientos_piezas.get(pieza, [])
            if extensible:
                for i in range(1, 8):
                    movimientos_piezas[pieza].append((i * movimientos[0], i * movimientos[1]))
            else:
                movimientos_piezas[pieza].append((movimientos[0], movimientos[1]))
    return movimientos_piezas

def juego_nuevo():
    """ 
        Inicializa el estado del juego. Crea la estructura de datos adonde se almacena el tablero del juego.
    """
    tablero = []
    for i in range(FILAS):
        tablero.append([])
        for j in range(COLUMNAS):
            tablero[i].append("")
    return tablero
        
def guardar_juego(tablero, ruta, nivel_actual):
    """
        Guarda el juego.
        Pre: el tablero en su estado actual y la ruta donde se desea guardar el juego.
        Post: el archivo con el juego guardado.
    """
    with open (ruta, "w") as f:
        for fila in range (len(tablero)):
            for columna in range (len(tablero[0])):
                if tablero[fila][columna]:
                    f.write(f"{tablero[fila][columna]};{columna},{fila} \n")
        f.write(f"{nivel_actual}")

def cargar_juego(ruta):
    """
        Carga el juego.
        Pre: la ruta donde se encuentra el archivo del juego guardado.
        Post: el juego guardado ahora es el juego actual.
    """
    with open (ruta) as f:
        juego_anterior = {}
        for linea in f:
            linea = linea.rstrip().split(";")
            if len(linea) == 1:
                nivel_actual = int(linea[0])
                break
            pieza = linea[0]
            posicion = linea[1].split(",")
            juego_anterior[pieza] = juego_anterior.get(pieza, [])
            juego_anterior[pieza].append((posicion[0], posicion[1]))
    tablero = juego_nuevo()
    for pieza, posiciones in juego_anterior.items():
        for posicion in posiciones:
            tablero[int(posicion[1])][int(posicion[0])] = pieza
    return tablero, nivel_actual

def nivel_nuevo(tablero, movimientos_piezas, nivel_actual):
    """
        Genera un nivel nuevo.
        Pre: el tablero vacío, los movimientos de las piezas del juego, y el nivel actual.
        Post: el tablero con las fichas correspondientes al nivel.
    """
    pieza_actual = random.choice(PIEZAS)
    pos_inicial_x, pos_inicial_y = random.choice(range(COLUMNAS)), random.choice(range(FILAS))
    tablero[pos_inicial_y][pos_inicial_x] = pieza_actual + PIEZA_ACTIVA
    piezas_colocadas = 1
    while piezas_colocadas < nivel_actual + 2:
        mov_sig = random.choice(movimientos_piezas[pieza_actual])
        pos_sig = (pos_inicial_x + mov_sig[0], pos_inicial_y + mov_sig[1])
        if pos_sig[0] in range (COLUMNAS) and pos_sig[1] in range (FILAS) and not tablero[pos_sig[1]][pos_sig[0]]:
            tablero[pos_sig[1]][pos_sig[0]] = random.choice(PIEZAS)
            pieza_actual = tablero[pos_sig[1]][pos_sig[0]]
            pos_inicial_x = pos_sig[0]
            pos_inicial_y = pos_sig[1]
            piezas_colocadas += 1
    return tablero

def donde_esta_pieza_activa(tablero):
    """
        Devuelve donde está la pieza activa.
        Pre: el tablero en su estado actual.
        Post: las coordenadas de la posición actual, y la pieza actual.
    """
    for i in range (FILAS):
        for j in range (COLUMNAS):
            if tablero[i][j][-5:] == PIEZA_ACTIVA:
                pos_actual_x = j
                pos_actual_y = i
    pieza_actual = tablero[pos_actual_y][pos_actual_x][:-5]
    return pos_actual_x, pos_actual_y, pieza_actual

def mover_piezas(tablero, x, y, movimientos_piezas):
    """
        Mueve las piezas del tablero, si es posible.
        Pre: el tablero en su estado actual, la celda donde clickeo el usuario,
            y los movimientos de las piezas.
        Post: devuelve el tablero de la misma forma si es inválido el movimiento,
            y si hubo una modificación devuelve el tablero modificado.
    """
    pos_actual_x, pos_actual_y, pieza_actual = donde_esta_pieza_activa(tablero)
    movimientos = movimientos_piezas[pieza_actual]
    if (pos_actual_x - x, pos_actual_y - y) in movimientos and tablero[y][x]:
        tablero[y][x] = tablero[y][x] + PIEZA_ACTIVA
        tablero[pos_actual_y].pop(pos_actual_x)
        tablero[pos_actual_y].insert(pos_actual_x, "")
    return tablero

def estado_del_nivel(tablero):
    """
        Verifica si el nivel fue completado o no.
        Pre: el tablero del juego en su estado actual.
        Post: devuelve un True si está completado el nivel,
            un False si no lo está.
    """
    contador = 0
    for i in range (FILAS):
        for j in range (COLUMNAS):
            if tablero[i][j]:
                contador += 1
    return contador == 1