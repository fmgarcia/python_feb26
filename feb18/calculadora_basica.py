print("Introduzca una operación a realizar:") # se muestra un mensaje al usuario indicando que debe introducir una operación a realizar
print("1. Suma") # se muestra la opción 1 para realizar una suma
print("2. Resta") # se muestra la opción 2 para realizar una resta
print("3. Multiplicación") # se muestra la opción 3 para realizar una multiplicación
print("4. División") # se muestra la opción 4 para realizar una división
operacion = input("Ingrese el número de la operación que desea realizar: ") # se solicita al usuario que ingrese el número de la operación que desea realizar, y se almacena en la variable "operacion"
numero1 = float(input("Ingrese el primer número: ")) # se solicita al usuario que ingrese el primer número, se convierte a tipo entero utilizando int() y se almacena en la variable "numero1"
numero2 = float(input("Ingrese el segundo número: ")) # se solicita al usuario que ingrese el segundo número, se convierte a tipo entero utilizando int() y se almacena en la variable "numero2"
if operacion == "1": # se verifica si la operación seleccionada es la opción
    resultado = numero1 + numero2 # se realiza la operación de suma utilizando el operador + y se almacena el resultado en la variable "resultado"
    print(f"El resultado de la suma es: {resultado}") # se imprime el resultado de la suma utilizando f-string para insertar la variable "resultado" directamente en la cadena de texto que se imprime
elif operacion == "2": # se verifica si la operación seleccionada es la opción 2
    print(f"El resultado de la resta es: {numero1 - numero2}") # se imprime el resultado de la resta utilizando f-string para insertar la variable "resultado" directamente en la cadena de texto que se imprime
elif operacion == "3": # se verifica si la operación seleccionada es la opción 3
    resultado = numero1 * numero2 # se realiza la operación de multiplicación utilizando el operador * y se almacena el resultado en la variable "resultado"
    print(f"El resultado de la multiplicación es: {resultado}") # se imprime el resultado de la multiplicación utilizando f-string para insertar la variable "resultado" directamente en la cadena de texto que se imprime
elif operacion == "4": # se verifica si la operación seleccionada es la opción 4
    if numero2 != 0: # se verifica si el segundo número es diferente de cero para evitar la división por cero
        resultado = numero1 / numero2 # se realiza la operación de división utilizando el operador / y se almacena el resultado en la variable "resultado"
        print(f"El resultado de la división es: {resultado}") # se imprime el resultado de la división utilizando f-string para insertar la variable "resultado" directamente en la cadena de texto que se imprime
    else:
        print("Error: No se puede dividir por cero.") # se imprime un mensaje de error si el segundo número es cero, indicando que no se puede realizar la división por cero
else:
    print("Operación no válida. Por favor, seleccione una opción del 1 al 4.") # se imprime un mensaje de error si la operación seleccionada no es válida, indicando que el usuario debe seleccionar una opción del 1 al 4 para realizar una operación válida