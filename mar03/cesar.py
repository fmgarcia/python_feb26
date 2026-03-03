import string

def cifrar(palabra):
    resultado = ""
    for letra in palabra:
        if letra in todas_las_letras:
            indice = todas_las_letras.index(letra)
            resultado += letras_cifradas[indice]
        else:
            resultado += letra
    return resultado

def descifrar(palabra):
    resultado = ""
    for letra in palabra:
        if letra in letras_cifradas:
            indice = letras_cifradas.index(letra)
            resultado += todas_las_letras[indice]
        else:
            resultado += letra
    return resultado

codigo_cifrado = 5
todas_las_letras = string.ascii_uppercase
letras_cifradas = todas_las_letras[codigo_cifrado:] + todas_las_letras[:codigo_cifrado]

print("Alfabeto original:", todas_las_letras)
print("Alfabeto cifrado:", letras_cifradas)

if __name__ == "__main__":
    print("Cifrado César")
    print("1. Cifrar")
    print("2. Descifrar")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        palabra = input("Ingrese la palabra a cifrar: ")
        resultado = cifrar(palabra.upper())
        print(f"Palabra cifrada: {resultado}")
        
    elif opcion == "2":
        palabra = input("Ingrese la palabra a descifrar: ")
        resultado = descifrar(palabra.upper())
        print(f"Palabra descifrada: {resultado}")
        
    else:
        print("Opción no válida")