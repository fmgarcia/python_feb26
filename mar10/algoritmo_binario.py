def binario(lista, objetivo): # Algoritmo binario para encontrar la posición de un elemento en una lista ordenada. La complejidad de este algoritmo es O(log n) debido a que divide la lista en mitades en cada iteración.
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    objetivo = 3
    resultado = binario(lista, objetivo)
    if resultado != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {resultado}.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista.")