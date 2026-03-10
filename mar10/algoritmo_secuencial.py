def secuencial(lista, objetivo): # Algoritmo secuencial para encontrar la posición de un elemento en una lista. En el peor caso, el elemento no se encuentra en la lista, lo que resulta en una complejidad de O(n).
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1 # Si el elemento no se encuentra en la lista, se devuelve -1

def masgrande(lista): # Otro ejemplo de algoritmo secuencial para encontrar el elemento más grande en una lista
    if not lista:
        return None  # Retorna None si la lista está vacía
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def find_two(lista): # Algoritmo secuencial para encontrar los índices del elemento más grande y el más pequeño en una lista
    if not lista:
        return None, None  # Retorna None si la lista está vacía
    x = y = 0 # Inicializamos x e y con el índice del primer elemento de la lista
    for i in range(1, len(lista)):
        if lista[x] < lista[i]:
            x = i
        elif lista[y] > lista[i]:
            y = i
    return x, y

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    objetivo = 10
    resultado = secuencial(lista, objetivo)
    if resultado != -1:
        print(f"El elemento {objetivo} se encuentra en la posición {resultado}.")
    else:
        print(f"El elemento {objetivo} no se encuentra en la lista.")
    
    mayor = masgrande(lista)
    print(f"El elemento más grande en la lista es: {mayor}")
    
    x, y = find_two(lista)
    print(f"Los índices del elemento más grande y el más pequeño son: {x}, {y}")