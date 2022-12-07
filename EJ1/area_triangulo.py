from vectores import norma, diferencia, calcular_prod_vectorial

""""Recibe tres puntos de R3 y devuelve el área del triángulo formado por los mismos"""

def calcular_area_triangulo(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    (x1, y1, z1)= diferencia(a1, a2, a3, b1, b2, b3)
    (x2, y2, z2)= diferencia(a1, a2, a3, c1, c2, c3)
    (x4, y4, z4)= calcular_prod_vectorial(x1, y1, z1, x2, y2, z2)
    norma_vectores= norma(x4, y4, z4)
    area_triangulo= norma_vectores / 2
    area_triangulo_redondeado= round (area_triangulo, 2)
    return area_triangulo_redondeado

# Pruebas

assert calcular_area_triangulo(0, 0, -3, 4, 2, 0, 3, 3, 1) == (4.64)
assert calcular_area_triangulo(-2, 0, 2, -5, 2, 0, 6, -3, 7) == (4.06)
assert calcular_area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == (19.46)