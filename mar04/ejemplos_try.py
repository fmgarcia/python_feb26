def ejemplo1():
    try:
        a = 10
        b = 5

        division = a / b
        print("El resultado de la división es:", division)
        
        nombres = ["Ana", "Luis", "Carlos", "María"]
        print(nombres[10]) # Esto va a generar un error de índice
        
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except IndexError:
        print("Error: Índice fuera de rango.")
    except Exception as e: # Captura cualquier otro tipo de excepción que no hayamos previsto
        print("Ha ocurrido un error inesperado:", str(e))
        
def ejemplo2():
    try:
        numero = int(input("Introduce un número: "))
        print("El número introducido es:", numero)
    except ValueError:
        print("Error: No has introducido un número válido.")
    except Exception as e:
        print("Ha ocurrido un error inesperado:", str(e))
        
def ejemplo3():
    try:
        with open("archivo_inexistente.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print("Ha ocurrido un error inesperado:", str(e))
        
def ejemplo4confinally():
    try:
        a = 10
        b = 0
        division = a / b
        print("El resultado de la división es:", division)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    finally:
        print("Este bloque se ejecuta siempre, haya habido error o no.")
        
def ejemplo5confinallyliberacionrecursos():
    try:
        archivo = open("archivo_inexistente.txt", "r")
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    finally:
        try:
            archivo.close() # Intentamos cerrar el archivo, aunque no se haya abierto correctamente
            print("Archivo cerrado.")
        except NameError:
            print("No se pudo cerrar el archivo porque no se abrió correctamente.")
   
def ejemplo6conExceptGeneral():
    try:
        a = 10
        b = 0
        division = a / b
        print("El resultado de la división es:", division)
    except Exception as e:
        print("Ha ocurrido un error:", str(e))     
        
        
#ejemplo1()
#ejemplo2()
#ejemplo3()
#ejemplo4confinally()
#ejemplo5confinallyliberacionrecursos()
ejemplo6conExceptGeneral()



print("Fin del programa, no se ha detenido por los errores.")