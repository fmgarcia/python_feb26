def triangle_path_finder_with_path(fila, columna, triangulo):
    if fila == len(triangulo):
        return 0, []
    else:
        camino1, camino2 = triangle_path_finder_with_path(fila + 1, columna, triangulo), triangle_path_finder_with_path(fila + 1, columna + 1, triangulo)
        minimo = min(camino1[0], camino2[0])
        if minimo == camino1[0]:
            return triangulo[fila][columna] + minimo, [triangulo[fila][columna]] + camino1[1]
        else:
            return triangulo[fila][columna] + minimo, [triangulo[fila][columna]] + camino2[1]

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
    resultado, camino = triangle_path_finder_with_path(0, 0, triangulo)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo es: {resultado}")
    print(f"El camino es: {camino}")
    resultado2, camino2 = triangle_path_finder_with_path(0, 0, triangulo2)
    print(f"El camino mínimo desde la parte superior hasta la parte inferior del triángulo2 es: {resultado2}")
    print(f"El camino es: {camino2}")
    