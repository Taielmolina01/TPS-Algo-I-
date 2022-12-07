from random import choice
from interfaz_grafica import imprimir_tablero

teclas_validas = ("w", "a", "s", "d", "o")

ARRIBA = teclas_validas[0]
IZQUIERDA = teclas_validas[1]
ABAJO = teclas_validas[2]
DERECHA = teclas_validas[3]

def crear_tablero(filas, columnas): 
    """
        Crea el tablero del juego resuelto.
        Pre: recibe las filas y columnas del mismo, siendo valores mayores a 0.
        Post: devuelve como salida el tablero resuelto.
    """
    tablero_resuelto = []
    contador_de_pos = 1
    for i in range (filas):
        tablero_resuelto.append([])
        for j in range (columnas):
            tablero_resuelto[i].append(contador_de_pos) 
            contador_de_pos += 1
    tablero_resuelto[filas - 1].pop(columnas - 1)
    tablero_resuelto[filas - 1].append("")
    return tablero_resuelto

def donde_esta_espacio_blanco(tablero, filas, columnas):
    """
        Indica la posición en la que se encuentra el espacio en blanco.
        Pre: el tablero del juego en su estado actual, junto a la cantidad de filas y columnas.
        Post: la posición del espacio vacío.
    """
    for f_vacio in range (filas):
        for c_vacio in range (columnas):
            if tablero[f_vacio][c_vacio] == "":
                return f_vacio, c_vacio

def validar_entrada(tablero, f_vacio, c_vacio, caracter_entrada, filas, columnas):
    """
        Valida los caracteres ingresados por el usuario, y los movimientos realizables.
        Pre: los caracteres de movimiento, el tablero del juego en su estado actual, filas y columnas totales, 
        y la posición del espacio vacio.
        Post: si el caracter ingresado/el movimiento solicitado es válido/realizable.
    """
    if not caracter_entrada in teclas_validas:
        return False
    f_vacio, c_vacio = donde_esta_espacio_blanco(tablero, filas, columnas)
    if c_vacio == columnas - 1 and caracter_entrada == IZQUIERDA: # No se puede mover la ficha hacia la izquierda.
        return False
    elif c_vacio == 0 and caracter_entrada == DERECHA: # No se puede mover la ficha hacia la derecha.
        return False
    elif f_vacio == filas - 1 and caracter_entrada == ARRIBA: # No se puede mover hacia arriba.        
        return False
    elif f_vacio == 0 and caracter_entrada == ABAJO: # No se puede mover hacia abajo.
        return False
    return True     # El movimiento es válido.

def desordenar_tablero(tablero_resuelto, filas, columnas):
    """
        Elige aleatoreamiente los movimientos que va a realizar el tablero para desordenarse.
        Pre: el tablero resuelto, la posición vacía y la cantidad de filas y columnas.
        Post: devuelve el tablero desordenado y la cantidad de movimientos realizados para desordenarlo (z).
    """
    movimientos_desordenar_tablero = []
    for i in range (filas * columnas * 4):
        movimientos_desordenar_tablero.append(choice(teclas_validas[:-1]))
    tablero_desordenado, z = mover_fichas(tablero_resuelto, movimientos_desordenar_tablero, filas, columnas)
    return tablero_desordenado, z

def mover_fichas(tablero, entrada, filas, columnas):
    """
        Mueve las fichas del juego.
        Pre: el tablero en su estado actual, la entrada del usuario/la entrada para desordenar el tablero inicial,
        las filas y columnas del tablero.
        Post: el tablero luego de los movimientos solicitados, luego de ser validados.
    """
    z = 0
    for caracter_entrada in entrada: # Recorro caracter a caracter la entrada
        f_vacio, c_vacio  = donde_esta_espacio_blanco(tablero, filas, columnas)
        if not validar_entrada(tablero, f_vacio, c_vacio, caracter_entrada, filas, columnas):   # Verifico que el movimiento sea valido.
            continue
        elif caracter_entrada == ARRIBA: # Letra W.
            tablero[f_vacio].insert(c_vacio, tablero[f_vacio + 1][c_vacio])
            tablero[f_vacio].pop(c_vacio + 1)
            tablero[f_vacio + 1].insert(c_vacio, "")
            tablero[f_vacio + 1].pop(c_vacio + 1)
            z += 1
        elif caracter_entrada == IZQUIERDA: # Letra A.
            tablero[f_vacio].insert(c_vacio + 2, "")
            tablero[f_vacio].pop(c_vacio)
            z += 1
        elif caracter_entrada == ABAJO: # Letra S.
            tablero[f_vacio].insert(c_vacio, tablero[f_vacio - 1][c_vacio])
            tablero[f_vacio].pop(c_vacio + 1)
            tablero[f_vacio - 1].insert(c_vacio, "")
            tablero[f_vacio - 1].pop(c_vacio + 1)
            z += 1
        else: # Letra D.
            tablero[f_vacio].insert(c_vacio - 1, "")
            tablero[f_vacio].pop(c_vacio + 1)
            z += 1
    imprimir_tablero(filas, columnas, tablero)
    return tablero, z