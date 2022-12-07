import random

class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        self.alto = alto
        self.ancho = ancho
        self.color = 0
        self.tablero = []
        self.colores = 0
        for i in range(self.alto):           # Filas
            self.tablero.append([])
            for j in range(self.ancho):      # Columnas
                self.tablero[i].append(self.color)
        self.color_actual = self.tablero[0][0]

    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        self.colores = n_colores
        for i in range (len(self.tablero)):
            for j in range (len(self.tablero[0])):
                self.tablero[i][j] = random.choice(range(n_colores))

    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        return self.tablero[fil][col]

    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        return [x for x in range (self.colores)]

    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        return (self.alto, self.ancho)

    def _flood_actual(self, camino, fila = 0, columna = 0):
        """
        Ejecuta el algoritmo recursivo que permite encontrar el bloque del Flood actual. Es la función que utiliza el wrapper cambiar_color.
        Argumentos: el diccionario vacío donde se guardará el Flood actual, la fila y columna de cada celda, inicializadas ambas en 0.
        Devuelve: el diccionario con las coordenadas de las celdas pertenecientes al Flood actual.
        """
        if self.tablero[fila][columna] != self.tablero[0][0]:
            return
        
        coordenada = (fila, columna)
        if coordenada not in camino:
            camino[coordenada] = coordenada
            if fila < self.alto - 1:
                self._flood_actual(camino, fila + 1, columna)
            if columna < self.ancho - 1:
                self._flood_actual(camino, fila, columna + 1)
            if fila > 0:
                self._flood_actual(camino, fila - 1, columna)
            if columna > 0:
                self._flood_actual(camino, fila, columna - 1)
        
        return camino

    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        camino = {}
        camino = self._flood_actual(camino)
        if camino:
            for coordenada in camino:
                self.tablero[coordenada[0]][coordenada[1]] = color_nuevo

    def clonar(self):
        """
        Devuelve: 
        Flood: Copia del Flood actual
        """
        copia = Flood(self.alto, self.ancho)
        copia.colores = self.colores
        for i in range (len(self.tablero)):
            copia.tablero[i] = self.tablero[i].copy()
        return copia

    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        suma = 0
        for i in range(self.alto):           
            for j in range(self.ancho - 1):
                if self.tablero[i][j] == self.tablero[i][j + 1]:
                    suma += 1
        return suma == self.alto * (self.ancho - 1)

    def celdas_adyacentes_al_flood_actual(self, camino_flood_act, bloque_adyacentes, fila = 0, columna = 0):
        """
        Ejecuta el mismo algoritmos que utiliza _flood_actual, pero guarda en un diccionario aquellas celdas adyacantes al Flood actual.
        Argumentos: dos diccionarios vacios, la fila y columna de la celda a analizar.
        Devuelve: el diccionario con las celdas de los bloques que son adyacentes al flood actual.
        """
        coordenada = (fila, columna)
        if coordenada not in camino_flood_act:
            camino_flood_act[coordenada] = coordenada
            if self.tablero[fila][columna] != self.tablero[0][0]:
                bloque_adyacentes[coordenada] = coordenada
                return

            if fila < self.alto - 1:
                self.celdas_adyacentes_al_flood_actual(camino_flood_act, bloque_adyacentes, fila + 1, columna)
            if columna < self.ancho - 1:
                self.celdas_adyacentes_al_flood_actual(camino_flood_act, bloque_adyacentes, fila, columna + 1)
            if fila > 0:
                self.celdas_adyacentes_al_flood_actual(camino_flood_act, bloque_adyacentes, fila - 1, columna)
            if columna > 0:
                self.celdas_adyacentes_al_flood_actual(camino_flood_act, bloque_adyacentes, fila, columna - 1)
        
        return bloque_adyacentes

    def calcular_celdas_en_bloque(self, bloque_ady, camino, f, c, fila, columna):
        """
        Ejecuta el mismo algoritmo que la funcion _flood_actual, guardando la cantidad de apariciones de cada color adyacente al Flood actual
        en su respectivo bloque.
        Argumentos: dos diccionarios vacíos, la fila y columna de la celda hallada en la funcion adyacentes_flood (f y c), la fila y columna del bloque a analizar.
        Devuelve: el diccionario con los colores que rodean al Flood actual y las apariciones de dichos colores en sus respectivos bloques.
        """
        coordenada = (fila, columna)
        color = self.tablero[f][c]
        if coordenada not in camino:
            camino[coordenada] = coordenada
            
            if self.tablero[fila][columna] != self.tablero[f][c]:
                return

            bloque_ady[color] = bloque_ady.get(color, 0) + 1
            if fila < self.alto - 1:
                self.calcular_celdas_en_bloque(bloque_ady, camino, f, c, fila + 1, columna)
            if columna < self.ancho - 1:
                self.calcular_celdas_en_bloque(bloque_ady, camino, f, c, fila, columna + 1)
            if fila > 0:
                self.calcular_celdas_en_bloque(bloque_ady, camino, f, c, fila - 1, columna)
            if columna > 0:
                self.calcular_celdas_en_bloque(bloque_ady, camino, f, c, fila, columna - 1)

        return bloque_ady