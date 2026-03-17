def triangle_path_finder_recursive(fila, columna, triangulo):
    if fila == len(triangulo):
        return 0
    else:
        minimo = min(
            triangle_path_finder_recursive(fila + 1, columna, triangulo),
            triangle_path_finder_recursive(fila + 1, columna + 1, triangulo)
        )
        return triangulo[fila][columna] + minimo
    
if __name__ == "__main__":
    triangulo = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    triangulo2 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [100, 101, 102, 3]
    ]
    resultado = triangle_path_finder_recursive(0, 0, triangulo)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo es: {resultado}")
    resultado2 = triangle_path_finder_recursive(0, 0, triangulo2)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo2 es: {resultado2}")
    
    