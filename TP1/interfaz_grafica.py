def imprimir_tablero(filas, columnas, tablero):
    print(":    Fifteen    :")
    for f in range(filas):
        for c in range(columnas):
            print("{:^7}".format(tablero[f][c]), end = "|")
        print()

def usuario_gano(cant_movimientos, z):
    print(f"Movimientos: {cant_movimientos} / {z*5}")
    print("¡Has ganado!")

def usuario_perdio(z):
    print(f"Movimientos: {z*5} / {z*5}")
    print("¡Has perdido!")

def imprimir_cant_movimientos(cant_movimientos, z):
    print(f"Movimientos: {cant_movimientos} / {z*5}")
    entrada = input("Entrada: ")
    return entrada

def imprimir_mensaje_despedida():
    print("¡Gracias por jugar!")