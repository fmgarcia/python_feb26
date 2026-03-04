# Uso de lambda

def suma(a, b):
    return a + b

# Lambda function equivalent to the sum function
suma_lambda = lambda a, b: a + b


print("Resultado de la suma normal:", suma(5, 3))
print("Resultado de la lambda:", suma_lambda(5, 3)) # lamda anónima, no tiene nombre, se define en el momento de su uso
print("Suma de lambda anónima:", (lambda a, b: a + b)(5, 3)) # lambda anónima, se define y se ejecuta en el mismo momento, no tiene nombre, no se puede reutilizar

# Programación funcional con map, filter y reduce
numeros = [1, 2, 3, 4, 5]
# Usando map para elevar al cuadrado cada número
# Map aplica una función a cada elemento de una lista y devuelve un iterador con los resultados
# List es una función que convierte el iterador devuelto por map en una lista
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

# Con listas por comprensión
cuadrados2 = [x**2 for x in numeros] # List comprehension, es una forma más concisa de crear listas a partir de iterables
print("Cuadrados con list comprehension:", cuadrados2)

# Con programación estructurada
cuadrados3 = []
for numero in numeros:
    cuadrados3.append(numero**2)
    
nombres = ["Ana", "Luis", "Carlos", "María"]
letras_nombres = list(map(lambda nombre: len(nombre), nombres)) # Map para obtener la longitud de cada nombre
print("Longitudes de los nombres:", letras_nombres)

dnis = ["12345678A", "87654321B", "11223344C"]
dnis_anonimos = list(map(lambda dni: dni[:3] + "****" + dni[-2:], dnis)) # Map para anonimizar los DNI
print("DNI anonimizados:", dnis_anonimos)

dnis_anonimos_comprension = [dni[:3] + "****" + dni[-2:] for dni in dnis] # List comprehension para anonimizar los DNI
print("DNI anonimizados con list comprehension:", dnis_anonimos_comprension)

# Ejemplos de filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres = ["Ana", "Luis", "Carlos", "María"]
# Usando filter para obtener los números pares
# Con programación estructurada clásica
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print("Números pares con programación estructurada:", pares)
# Con filter
pares_filter = list(filter(lambda x: x % 2 == 0, numeros)) # Filter aplica una función a cada elemento de una lista y devuelve un iterador con los elementos para los que la función devuelve True
print("Números pares con filter:", pares_filter)
# Con list comprehension
pares_comprension = [x for x in numeros if x % 2 == 0] # List comprehension para obtener los números pares
print("Números pares con list comprehension:", pares_comprension)
# nombres con más de 4 letras usando filter
nombres_largos_filter = list(filter(lambda nombre: len(nombre) > 4, nombres)) # Filter para obtener los nombres con más de 4 letras
print("Nombres con más de 4 letras con filter:", nombres_largos_filter)

# Reduce lo que hace es aplicar una función de reducción a los elementos de una lista, reduciéndolos a un solo valor.
from functools import reduce
numeros = [1, 2, 3, 4, 5]
# Usando reduce para obtener el producto de todos los números
producto = reduce(lambda x, y: x * y, numeros) # Reduce para obtener el producto de todos los números
print("Producto de los números con reduce:", producto)
nombres = ["Ana", "Luis", "Carlos", "María"]
# Usando reduce para concatenar todos los nombres
nombres_concatenados = reduce(lambda x, y: x + ";" + y, nombres) # Reduce para concatenar todos los nombres con punto y coma como separador
print("Nombres concatenados con reduce:", nombres_concatenados)
nombres_concatenados_con_fran = reduce(lambda x, y: x + ";" + y, nombres, "Fran") # Reduce para concatenar todos los nombres con punto y coma como separador, con un valor inicial "Fran"
print("Nombres concatenados con reduce y valor inicial:", nombres_concatenados_con_fran)
# reduce con listas por comprensión
nombres_concatenados_comprension = reduce(lambda x, y: x + ";" + y, [nombre for nombre in nombres]) # Reduce para concatenar todos los nombres con punto y coma como separador, usando list comprehension para crear la lista de nombres
print("Nombres concatenados con reduce y list comprehension:", nombres_concatenados_comprension)


# Ejemplos de map y filter al mismo tiempo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Usando map para elevar al cuadrado los números pares
cuadrados_pares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros))) # Filter para obtener los números pares y map para elevarlos al cuadrado
print("Cuadrados de los números pares con map y filter:", cuadrados_pares)

cuadrados_pares_comprension = [x**2 for x in numeros if x % 2 == 0] # List comprehension para elevar al cuadrado los números pares

# Sobre la lista de números, quiero elevar al cuadrado los números pares y quedarme solo con los resultados mayores que 10
cuadrados_pares_mayores_10 = list(filter(lambda x: x > 10, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros))))
print("Cuadrados de los números pares mayores que 10 con map y filter:", cuadrados_pares_mayores_10)

cuadrados_pares_mayores_10_comprension = [x**2 for x in numeros if x % 2 == 0 and x**2 > 10] # List comprehension para elevar al cuadrado los números pares y quedarnos solo con los resultados mayores que 10

# lo mismo con programación estructurada clásica
cuadrados_pares_mayores_10_estructurada = []
for numero in numeros:
    if numero % 2 == 0:
        cuadrado = numero**2
        if cuadrado > 10:
            cuadrados_pares_mayores_10_estructurada.append(cuadrado)
            
multiplicacion_cuadrados_pares_mayores_10 = reduce(lambda x, y: x * y, 
                                                   filter(lambda x: x > 10, 
                                                          map(lambda x: x**2, 
                                                              filter(lambda x: x % 2 == 0, numeros)))) # Reduce para multiplicar los cuadrados de los números pares mayores que 10 
print("Multiplicación de los cuadrados de los números pares mayores que 10 con reduce:", multiplicacion_cuadrados_pares_mayores_10)