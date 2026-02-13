# Este programa muestra todas las operaciones básicas de suma, resta, multiplicación, división, división entera, módulo y potencia utilizando dos números ingresados por el usuario.
# El programa también muestra el resultado de cada operación utilizando f-string para insertar las variables directamente en la cadena de texto que se imprime.
# Además, el programa incluye comentarios explicativos para cada operación y para la entrada de datos,
# lo que ayuda a entender el propósito de cada parte del código y cómo se realizan las operaciones básicas en Python.
# El programa es interactivo, ya que solicita al usuario que ingrese dos números, y luego muestra los resultados de las operaciones básicas realizadas con esos números.
# El programa es útil para aprender y practicar las operaciones básicas en Python, así como para entender cómo se pueden utilizar las variables y los comentarios para mejorar la legibilidad del código.
# El programa también muestra cómo se pueden utilizar diferentes tipos de operadores en Python, como el operador de suma (+), resta (-), multiplicación (*), división (/), división entera (//), módulo (%) y potencia (**).
# El programa es un ejemplo básico de cómo se pueden realizar operaciones matemáticas en Python y cómo se pueden mostrar los resultados de manera clara y legible utilizando f-string y comentarios explicativos.
# El programa también muestra cómo se pueden utilizar diferentes tipos de operadores en Python, como el operador de suma (+), resta (-), multiplicación (*), división (/), división entera (//), módulo (%) y potencia (**).
# El programa es un ejemplo básico de cómo se pueden realizar operaciones matemáticas en Python y cómo se pueden mostrar los resultados de manera clara y legible utilizando f-string y comentarios explicativos.

#numero1 = float(input("Introduce el primer número: ")) # solicita al usuario que ingrese el primer número y lo convierte a tipo float para permitir números decimales
#numero2 = float(input("Introduce el segundo número: ")) # solicita al usuario que ingrese el segundo número y lo convierte a tipo float para permitir números decimales
numero1 = 7.0
numero2 = 3.0
suma = numero1 + numero2 # realiza la operación de suma utilizando el operador +
resta = numero1 - numero2 # realiza la operación de resta utilizando el operador -
multiplicacion = numero1 * numero2 # realiza la operación de multiplicación utilizando el operador *
division = numero1 / numero2 # realiza la operación de división utilizando el operador /
division_entera = numero1 // numero2 # realiza la operación de división entera utilizando el operador //
modulo = numero1 % numero2 # realiza la operación de módulo utilizando el operador %
potencia = numero1 ** numero2 # realiza la operación de potencia utilizando el operador **
print(f"La suma de {numero1} y {numero2} es: {suma}") # imprime el resultado de la suma utilizando f-string para insertar las variables directamente en la cadena
print(f"La resta de {numero1} y {numero2} es: {resta}") # imprime el resultado de la resta utilizando f-string para insertar las variables directamente en la cadena
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}") # imprime el resultado de la multiplicación utilizando f-string para insertar las variables directamente en la cadena
print(f"La división de {numero1} entre {numero2} es: {division}") # imprime el resultado de la división utilizando f-string para insertar las variables directamente en la cadena
print(f"La división entera de {numero1} entre {numero2} es: {division_entera}") # imprime el resultado de la división entera utilizando f-string para insertar las variables directamente en la cadena
print(f"El módulo de {numero1} entre {numero2} es: {modulo}") # imprime el resultado del módulo utilizando f-string para insertar las variables directamente en la cadena
print(f"{numero1} elevado a la potencia de {numero2} es: {potencia}") # imprime el resultado de la potencia utilizando f-string para insertar las variables directamente en la cadena   


# básico de string
cadena = "hola mundo" # asigna la cadena de texto "hola mundo" a la variable cadena
print(cadena) # imprime el valor de la variable cadena, que es "hola mundo"
print(cadena[1]) # imprime el segundo carácter de la cadena, que es "o", utilizando indexación (los índices comienzan en 0)
# Uso de slicing para obtener subcadenas
print(cadena[0:4]) # imprime los primeros cuatro caracteres de la cadena, que es "hola", utilizando slicing (el índice final no se incluye)
print(cadena[:5]) # imprime los primeros cinco caracteres de la cadena, que es "hola ", utilizando slicing (el índice final no se incluye)
print(cadena[5:]) # imprime los caracteres desde el índice 5 hasta el final de la cadena, que es "mundo", utilizando slicing (el índice inicial se incluye)
print(cadena[-5:]) # imprime los últimos cinco caracteres de la cadena, que es "mundo", utilizando slicing con índices negativos (el índice final no se incluye)
print(cadena[-5:-1]) # imprime los caracteres desde el índice -5 hasta el índice -1, que es "mund", utilizando slicing con índices negativos (el índice final no se incluye)
print(cadena[::2]) # imprime los caracteres de la cadena con un paso de 2, que es "hl ud", utilizando slicing con un paso (el índice final no se incluye)
print(cadena[1::2]) # imprime los caracteres de la cadena con un paso de 2 comenzando desde el índice 1, que es "oamno", utilizando slicing con un paso (el índice final no se incluye)
print(cadena[::-1]) # imprime la cadena al revés, que es "odnum aloh", utilizando slicing con un paso negativo (el índice final no se incluye)

# Uso de comentarios en Python
# Esto es un comentario de una línea
'''
Esto es un comentario de varias líneas
que se puede utilizar para explicar partes del código o para incluir información adicional que no forma parte del
código ejecutable. Es útil para mejorar la legibilidad del código y para proporcionar contexto o detalles sobre lo que hace el código.
También se puede utilizar para comentar temporalmente partes del código que no se quieren ejecutar, sin eliminarlas completamente.
Los comentarios de varias líneas se delimitan con tres comillas dobles (""")  al inicio y al final del comentario.
'''