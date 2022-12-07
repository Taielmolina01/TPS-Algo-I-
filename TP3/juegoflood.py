from flood import Flood
from pila import Pila
from cola import Cola

class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho)
        self.flood.mezclar_tablero(n_colores)
        self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()
        self.pasos_hechos = Pila()
        self.pasos_deshechos = Pila()
        self.flood_inicial = Flood.clonar(self.flood)

    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """

        self.color_sin_actualizar = self.flood.tablero[0][0]
        self.flood.cambiar_color(color)
        if self.color_sin_actualizar != self.flood.tablero[0][0]:
            while not self.pasos_deshechos.esta_vacia():
                self.pasos_deshechos.desapilar()
            self.n_movimientos += 1
            self.pasos_hechos.apilar(Flood.clonar(self.flood))
        
            if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color:
                self.pasos_solucion.desencolar()
            else:
                self.pasos_solucion = Cola()

    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """

        if not self.pasos_hechos.esta_vacia():
            self.pasos_deshechos.apilar(self.pasos_hechos.desapilar())
            if self.pasos_hechos.esta_vacia():
                self.flood = Flood.clonar(self.flood_inicial)
            else:
                self.flood = self.pasos_hechos.ver_tope()
            self.n_movimientos -= 1
            self.pasos_solucion = Cola()

    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """

        if not self.pasos_deshechos.esta_vacia():
            self.pasos_hechos.apilar(self.pasos_deshechos.desapilar())
            self.flood = self.pasos_hechos.ver_tope()
            self.n_movimientos += 1
            self.pasos_solucion = Cola()


    def _calcular_movimientos(self):
        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.
        El algoritmo de solución elige el color que más casilleros agregaría al flood actual.
        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """
        copia = Flood.clonar(self.flood)
        self.max_movimientos = 0
        self.pasos_a_seguir = Cola()
        while not Flood.esta_completado(copia):
            bloque_flood_actual = Flood._flood_actual(copia, {})
            ady = {}
            camino = {}
            ady_flood = Flood.celdas_adyacentes_al_flood_actual(copia, camino, ady)
            bloque_ady = {}
            for coordenada in ady_flood:
                f = coordenada[0]
                c = coordenada[1]
                Flood.calcular_celdas_en_bloque(copia, bloque_ady, {}, f, c, f, c)
            color_a_elegir = max(bloque_ady, key = lambda clave: bloque_ady[clave])
            for coordenada in bloque_flood_actual:
                fila = coordenada[0]
                columna = coordenada[1]
                copia.tablero[fila][columna] = color_a_elegir
            self.max_movimientos += 1
            self.pasos_a_seguir.encolar(color_a_elegir)
        
        return self.max_movimientos, self.pasos_a_seguir 
            

    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()


    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """

        # else: 
        #     raise ValueError("No hay una solución calculada")
        return self.pasos_solucion.ver_frente()


    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()


    def dimensiones(self):
        return self.flood.dimensiones()


    def obtener_color(self, fil, col):
        return self.flood.obtener_color(fil, col)


    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()


    def esta_completado(self):
        return self.flood.esta_completado()