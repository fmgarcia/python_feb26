# Programación recursiva: Llamamos a la función dentro de sí misma para resolver el problema.
def triangle_pascal_recursive(fila, columna, triangulo):
    if fila == len(triangulo):
        return 0
    else:
        minimo = min(
            triangle_pascal_recursive(fila + 1, columna, triangulo),
            triangle_pascal_recursive(fila + 1, columna + 1, triangulo)
        )
        return triangulo[fila][columna] + minimo


# Programación dinámica: Guardamos los resultados de las llamadas anteriores para evitar cálculos repetidos.    
def triangle_pascal_memorizado(fila, columna, triangulo, memoria={}):
    if (fila, columna) in memoria:
        return memoria[(fila, columna)]
    if fila == len(triangulo):
        return 0
    else:
        minimo = min(
            triangle_pascal_memorizado(fila + 1, columna, triangulo, memoria),
            triangle_pascal_memorizado(fila + 1, columna + 1, triangulo, memoria)
        )
        memoria[(fila, columna)] = triangulo[fila][columna] + minimo
        return memoria[(fila, columna)]
    
if __name__ == "__main__":
    triangulo = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    resultado = triangle_pascal_recursive(0, 0, triangulo)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo de Pascal es: {resultado}")
    
    resultado_memorizado = triangle_pascal_memorizado(0, 0, triangulo)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo de Pascal (memorizado) es: {resultado_memorizado}")