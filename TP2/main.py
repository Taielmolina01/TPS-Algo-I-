import gamelib
from logica import lector_archivo_movimientos, juego_nuevo, mover_piezas, nivel_nuevo, estado_del_nivel, guardar_juego, cargar_juego
from interfaz_grafica import juego_mostrar, pixeles_a_coordenadas, espacios_invalidos, ANCHO_VENTANA, ALTO_VENTANA

ICONO_VENTANA = "TPS\\TP2\\img\\chess2.gif"
MOVIMIENTOS_CSV = "TPS\\TP2\\movimientos.csv"
ARCHIVO_INICIO_NIVEL = "inicio_nivel.txt"
ARCHIVO_PARTIDA_GUARDADA = "partida_guardada.txt"

def desea_cargar_partida(movimientos_piezas):
    """
        Le pregunta al usuario si quiere cargar la última partida jugada, en su estado final.
        Pre: los movimientos de las piezas.
        Post: el inicio del juego, sea uno nuevo, o una partida anterior.
    """
    while True:
        respuesta = gamelib.input("¿Desea cargar la partida anterior? Y/N")
        if respuesta in 'yY':
            juego, nivel_actual = cargar_juego(ARCHIVO_PARTIDA_GUARDADA)
            return juego, nivel_actual
        elif respuesta in 'nN':
            juego = juego_nuevo()
            nivel_actual = 1
            juego = nivel_nuevo(juego, movimientos_piezas, nivel_actual)
            guardar_juego(juego, ARCHIVO_INICIO_NIVEL, nivel_actual)
            return juego, nivel_actual

def main():
    """
        Ejecuta el juego completo.
    """
    gamelib.title("Shape Shifter Chess")
    gamelib.icon(ICONO_VENTANA)
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    try:
        movimientos_piezas = lector_archivo_movimientos(MOVIMIENTOS_CSV)
    except IOError:
        gamelib.say("Error al abrir el archivo de movimientos")
        raise IOError

    try:
        juego, nivel_actual = desea_cargar_partida(movimientos_piezas)
    except FileNotFoundError:
        gamelib.say("No hay partidas anteriores")
        raise FileNotFoundError

    while gamelib.is_alive():
        
        juego_mostrar(juego, nivel_actual, movimientos_piezas)
        guardar_juego(juego, ARCHIVO_PARTIDA_GUARDADA, nivel_actual)

        ev = gamelib.wait()
        if not ev:
            break
        
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:

            x, y = ev.x, ev.y

            if espacios_invalidos(x, y): 
                continue

            x, y = pixeles_a_coordenadas(x, y)
            
            juego = mover_piezas(juego, x, y, movimientos_piezas)

            if estado_del_nivel(juego):
                nivel_actual += 1                    
                juego = juego_nuevo()
                juego = nivel_nuevo(juego, movimientos_piezas, nivel_actual)
                guardar_juego(juego, ARCHIVO_INICIO_NIVEL, nivel_actual)
            else:
                continue
            
        elif ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break

        elif ev.type == gamelib.EventType.KeyPress and ev.key in 'zZ':
            juego, nivel_actual = cargar_juego(ARCHIVO_INICIO_NIVEL)

gamelib.init(main)