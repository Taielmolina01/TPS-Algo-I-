import gamelib
from logica_5_en_linea import turno_jugador, pixeles_a_coordenadas, espacios_invalidos, juego_crear

ANCHO_JUEGO = 300 
ALTO_JUEGO = ANCHO_JUEGO # Al ser un cuadrado, alto_juego y ancho_juego deben ser iguales.
ANCHO_VENTANA = ANCHO_JUEGO 
PADDING_INF = 50
ALTO_VENTANA = ALTO_JUEGO + PADDING_INF
ANCHO_CELDA = 30
ALTO_CELDA = ANCHO_CELDA # Idem que con alto_juego y ancho_juego.
FILAS = 10
COLUMNAS = 10

def juego_actualizar(juego, x, y, jugador_actual):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    if juego[y][x] == "":
        juego[y][x] = jugador_actual
        return True
    return False   

def juego_mostrar(juego, posicion_actual, jugador_actual):
    """Actualizar la ventana"""
    # Creo la ventana inicial
    gamelib.title("5 en linea")
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_JUEGO, outline = "white", fill = "black")
    for t in range(ANCHO_CELDA, ALTO_JUEGO + 1, ANCHO_CELDA):
        gamelib.draw_line(t, 0, t, ANCHO_VENTANA, fill = "white")
        gamelib.draw_line(0, t, ANCHO_VENTANA, t, fill = "white")
    gamelib.draw_text(f"Turno: {jugador_actual}", ANCHO_VENTANA // 2, ALTO_JUEGO + PADDING_INF // 2)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if juego[i][j]:
                gamelib.draw_text(juego[i][j], ((j + 1) * ANCHO_CELDA) - (ANCHO_CELDA // 2), ((i + 1) * ALTO_CELDA) - (ALTO_CELDA // 2))

def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    turno_numero = 1

    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:

        jugador_actual = turno_jugador(turno_numero)
        if turno_numero == 1:
            posicion_actual = 0

        gamelib.draw_begin()
        juego_mostrar(juego, posicion_actual, jugador_actual)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click
            if espacios_invalidos(x, y):
                continue

            x, y = pixeles_a_coordenadas(x, y)
            if juego_actualizar(juego, x, y, jugador_actual):
                turno_numero += 1

gamelib.init(main)