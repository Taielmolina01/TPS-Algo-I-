import gamelib
from logica import donde_esta_pieza_activa

TAMANIO_LETRA = 11
FUENTE_LETRA = "Victor Mono"
AZUL_TABLERO = "#10131C" 
NEGRO_TABLERO = "#0C0C0C"
GRIS_TABLERO = "#131313"
COLOR_RECTANGULO =  "#A92650"
ALFIL_BLANCO = "TPS\\TP2\\img\\alfil_blanco.gif"
ALFIL_ROJO = "TPS\\TP2\\img\\alfil_rojo.gif"
CABALLO_BLANCO = "TPS\\TP2\\img\\caballo_blanco.gif"
CABALLO_ROJO =  "TPS\\TP2\\img\\caballo_rojo.gif"
TORRE_BLANCO =  "TPS\\TP2\\img\\torre_blanco.gif"
TORRE_ROJO =  "TPS\\TP2\\img\\torre_rojo.gif"
ANCHO_JUEGO = 400
ALTO_JUEGO = ANCHO_JUEGO
PADDING_INF = 100
ANCHO_VENTANA = ANCHO_JUEGO
ALTO_VENTANA = ALTO_JUEGO + PADDING_INF
ANCHO_CELDA = ANCHO_VENTANA // 8
ALTO_CELDA = ANCHO_CELDA
FILAS = 8
COLUMNAS = 8
ANCHO_IMG = 34 # Las imagenes del tablero son de 34x34
PADDING_IMG = (ANCHO_CELDA - ANCHO_IMG) // 2

def pixeles_a_coordenadas(x, y):
    x = x // ANCHO_CELDA
    y = y // ALTO_CELDA
    return x, y

def espacios_invalidos(x, y):
    if x % ANCHO_CELDA == 0 or y % ALTO_CELDA == 0 or y > ALTO_JUEGO:
        return True
    return False

def juego_mostrar(juego, nivel_actual, movimientos_piezas):
    """
        Actualiza la ventana.
        Pre: el tablero del juego, el nivel actual, y los movimientos de las piezas.
        Post: la ventana de la interfaz con el juego en su estado actual. 
    """
    imagenes = {"alfil" : ALFIL_BLANCO,
                "alfil_rojo" : ALFIL_ROJO,
                "caballo" : CABALLO_BLANCO,
                "caballo_rojo" : CABALLO_ROJO, 
                "torre" : TORRE_BLANCO,
                "torre_rojo" : TORRE_ROJO,
                }
    gamelib.draw_begin()
    for l in range (1, ANCHO_JUEGO - ANCHO_CELDA + 1, ANCHO_CELDA * 2):
        for k in range (1, ANCHO_JUEGO + 1, ANCHO_CELDA * 2):
            gamelib.draw_rectangle(k, l, ANCHO_CELDA - 2 + k, ALTO_CELDA - 2 + l, fill = AZUL_TABLERO) 
            gamelib.draw_rectangle(ANCHO_CELDA + k, l, ANCHO_CELDA * 2 - 2 + k, ALTO_CELDA - 2 + l, fill = NEGRO_TABLERO)
            gamelib.draw_rectangle(ANCHO_CELDA + k, ALTO_CELDA + l, ANCHO_CELDA * 2 - 2 + k, ALTO_CELDA * 2 - 2 + l, fill = AZUL_TABLERO) 
            gamelib.draw_rectangle(k, ALTO_CELDA + l, ANCHO_CELDA - 2 + k, ALTO_CELDA * 2 - 2 + l, fill = NEGRO_TABLERO) 
    gamelib.draw_rectangle(0, ALTO_JUEGO + 1, ANCHO_VENTANA, ALTO_VENTANA, fill = GRIS_TABLERO)
    gamelib.draw_line(0, ALTO_JUEGO + 1, ANCHO_JUEGO, ALTO_JUEGO + 1, fill = "black", width = 3)
    gamelib.draw_text("SHAPE SHIFTER CHESS", ANCHO_JUEGO // 2 - ANCHO_CELDA * 2, ALTO_JUEGO + PADDING_INF // 3 - 3, size = TAMANIO_LETRA, font = FUENTE_LETRA)
    gamelib.draw_text("Salir: Esc", ANCHO_JUEGO // 2 + ANCHO_CELDA * 2, ALTO_JUEGO + PADDING_INF // 3 - 3, size = TAMANIO_LETRA, font = FUENTE_LETRA)
    gamelib.draw_text(f"Nivel: {nivel_actual}", ANCHO_JUEGO // 2 - ANCHO_CELDA * 2, ALTO_JUEGO + (PADDING_INF // 3 * 2) + 5, size = TAMANIO_LETRA, font = FUENTE_LETRA)
    gamelib.draw_text("Reintentar: Z", ANCHO_JUEGO // 2 + ANCHO_CELDA * 2, ALTO_JUEGO + (PADDING_INF // 3 * 2) + 5, size = TAMANIO_LETRA, font = FUENTE_LETRA)
    pos_actual_x, pos_actual_y, pieza_actual = donde_esta_pieza_activa(juego)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if juego[i][j]:
                img = imagenes[juego[i][j]]
                gamelib.draw_image(img, j * ANCHO_CELDA + PADDING_IMG, i * ALTO_CELDA + PADDING_IMG)
                if (pos_actual_x - j, pos_actual_y - i) in movimientos_piezas[pieza_actual]:
                    gamelib.draw_rectangle(j * ANCHO_CELDA, i * ALTO_CELDA,  (j + 1) * ANCHO_CELDA, (i + 1) * ALTO_CELDA, fill = None, outline = COLOR_RECTANGULO, width = 2)
    gamelib.draw_end()