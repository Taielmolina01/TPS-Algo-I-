JUGADOR_X = "x"
JUGADOR_O = "o"
COLUMNAS = 10
FILAS = 10

def juego_crear():
    """Inicializar el estado del juego"""
    simbolos_almacenados = []
    for i in range(FILAS):
        simbolos_almacenados.append([])
        for j in range(COLUMNAS):
            simbolos_almacenados[i].append("")
    # Creo la estructura de datos adonde voy almacenar donde se ha dibujado una "x" o un "o".
    return simbolos_almacenados

def turno_jugador(turno_numero):
    if turno_numero % 2 == 0:
        jugador_actual = JUGADOR_X
    else:
        jugador_actual = JUGADOR_O
    return jugador_actual

def pixeles_a_coordenadas(x, y):
    x = x // 30
    y = y // 30
    return x, y

def espacios_invalidos(x, y):
    if x % 30 == 0 or y % 30 == 0 or y > 300:
        return True
    return False