dict_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def romano_a_entero(romano): # Algoritmo para convertir un número romano a entero. La complejidad de este algoritmo es O(n) debido a que se recorre la cadena de caracteres del número romano una vez.
    total = 0
    prev_value = 0
    for char in romano:
        value = dict_romanos[char]
        if prev_value < value:
            total += value - 2 * prev_value  # Restamos el valor anterior que se sumó
        else:
            total += value
        prev_value = value
    return total

# Ejemplo de Hash Table utilizando un diccionario en Python. La complejidad de acceso a los elementos en un diccionario es O(1) en promedio, lo que lo hace muy eficiente para almacenar y recuperar datos.
precios = {"manzana": 0.5, "banana": 0.3, "naranja": 0.8} # Ejemplo muy básico de tabla hash utilizando un diccionario en Python. La complejidad de acceso a los elementos en un diccionario es O(1) en promedio, lo que lo hace muy eficiente para almacenar y recuperar datos.

# Ejemplo de Hash para contar la frecuencia de aparaciones de una palabra en un texto. La complejidad de este algoritmo es O(n) debido a que se recorre la lista de palabras una vez.
def contar_palabras(texto):
    frecuencia = {}
    palabras = texto.split()
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

# Eliminar duplicados y búsquedas con Conjuntos (Sets) en Python. La complejidad de eliminar duplicados utilizando un conjunto es O(n) debido a que se recorre la lista de elementos una vez para agregar los elementos al conjunto, y la complejidad de búsqueda en un conjunto es O(1) en promedio.
elementos = [1, 2, 3, 4, 5, 2, 3, 1]
conjunto = set(elementos)  # Eliminar duplicados utilizando un conjunto. La complejidad de este proceso es O(n) debido a que se recorre la lista de elementos una vez para agregar los elementos al conjunto.



if __name__ == "__main__":
    numero_romano = "MCMXCIV"
    resultado = romano_a_entero(numero_romano)
    print(f"El número romano {numero_romano} se convierte a entero: {resultado}.")
    
    print(f"El precio de una manzana es: {precios['manzana']} euros.")
    
    texto = "La manzana es una fruta. La banana es otra fruta. La naranja es también una fruta."
    frecuencia = contar_palabras(texto)  # Orden de complejidad O(n) debido a que se recorre la lista de palabras una vez.
    print(f"Frecuencia de palabras en el texto: {frecuencia}")
    print(f"La frecuencia de la palabra 'fruta' es: {frecuencia.get('fruta', 0)}") # Orden de complejidad O(1) para acceder a la frecuencia de una palabra específica en el diccionario.
    print(f"Elementos únicos en la lista: {conjunto}") # Orden de complejidad O(n) para eliminar duplicados utilizando un conjunto.
    print(f"¿Está el número 3 en el conjunto? {'Sí' if 3 in conjunto else 'No'}") # Orden de complejidad O(1) para buscar un elemento en un conjunto.