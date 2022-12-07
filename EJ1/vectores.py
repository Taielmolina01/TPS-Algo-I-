def norma(x4, y4, z4):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x4**2 + y4**2 + z4**2) ** 0.5

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

def calcular_prod_vectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    x3 = y1 * z2 - z1 *y2
    y3 = z1 * x2 - x1 * z2
    z3 = x1 * y2 - y1 * x2
    return x3, y3, z3
