from interfaz_grafica import usuario_gano, usuario_perdio, imprimir_cant_movimientos, imprimir_mensaje_despedida
from logica import crear_tablero, desordenar_tablero, mover_fichas

SALIR = "o"

def iniciar_juego(tablero_resuelto, tablero_desordenado, z, filas, columnas):
    """
        Inicia el juego y analiza luego de cada movimiento si el jugador ha ganado, ha perdido,
        o continua jugando.
        Pre: el tablero resuelto, el tablero actual, la cantidad de movimientos realizados para desordenar
        el tablero (z), las filas y columnas del tablero.
    """
    cant_movimientos = 0 # Establezco en 0 como inicio de los movimientos realizados por el usuario.
    while True: 
        if cant_movimientos <= z * 5 and tablero_resuelto == tablero_desordenado:
            usuario_gano(cant_movimientos, z)
            return
        elif cant_movimientos >= z * 5 and tablero_resuelto != tablero_desordenado:
            usuario_perdio(z)
            return
        entrada = imprimir_cant_movimientos(cant_movimientos, z)
        if entrada == SALIR:
            return SALIR
        tablero, mov_realizados = mover_fichas(tablero_desordenado, entrada, filas, columnas)
        cant_movimientos += mov_realizados 

def ejecutar_fifteen(filas, columnas): # Función principal (main)
    """
        Ejecuta el programa completo.
        Pre: las filas y columnas del tablero.
        Post: la ejecución total del programa.
    """
    tablero_resuelto = crear_tablero(filas, columnas)
    tablero_desordenado, z = desordenar_tablero(tablero_resuelto, filas, columnas) 
    tablero_resuelto = crear_tablero(filas, columnas)
    devolucion_iniciar_juego = iniciar_juego(tablero_resuelto, tablero_desordenado, z, filas, columnas)
    if devolucion_iniciar_juego == SALIR:
        imprimir_mensaje_despedida()

ejecutar_fifteen(3, 3)