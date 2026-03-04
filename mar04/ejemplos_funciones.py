IVA = 0.21
RUTA_API = "https://api.ejemplo.com/v1/"

def basica():
    print("Hola, soy una función básica")

def con_parametros(nombre):
    print(f"Hola, {nombre}. Soy una función con parámetros")
    
def con_dos_parametros(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años. Soy una función con dos parámetros")
  
# Uso de parámetros variables (*args)  
def parametros_variables(*args):
    print("Hola, soy una función con parámetros variables")
    print("Los parámetros recibidos son:", args)
    
def puestos_trabajo(*parametros):
    if parametros:
        print("Los puestos de trabajo son:")
        for puesto in parametros:
            print("-", puesto)
    else:
        print("No hay puestos de trabajo disponibles")
        
# Funciones con parámetros por defecto
# Si no se proporciona un valor para el parámetro, se usará el valor por defecto
# En el momento que ponga un parámetro por defecto, todos los siguientes también deben tener un valor por defecto
def saludo(nombre="Invitado"):
    print(f"Hola, {nombre}. Bienvenido a la función con parámetros por defecto")
    
def saludo2(nombre="Invitado", mensaje="Bienvenido a la función con parámetros por defecto"):
    print(f"Hola, {nombre}. {mensaje}")
    
# Uso de parámetros nominales (keyword arguments)
def saludo3(nombre, mensaje=""):
    print(f"Hola, {nombre}. {mensaje}")
    
# Función con retorno de valor
def suma(a, b):
    return a + b

def operaciones(a, b):
    """Esta función devuelve las operaciones básicas sobre 2 números
    la suma, la resta, la multiplicación y la división

    Args:
        a (float): el primer operando
        b (float): el segundo operando, en las divisiones no puede ser 0

    Returns:
        tuple: Es una tupla con los resultados de las operaciones en el orden suma, resta, multiplicación y división
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

def operaciones2(a: float, b: float) -> tuple[float, float, float, float]:
    """Esta función devuelve las operaciones básicas sobre 2 números
    la suma, la resta, la multiplicación y la división

    Args:
        a (float): el primer operando
        b (float): el segundo operando, en las divisiones no puede ser 0

    Returns:
        tuple(float,float,float,float): Es una tupla con los resultados de las operaciones en el orden suma, resta, multiplicación y división
    """   
    suma = a + b
    print("El resultado de la suma es:", suma)
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else 0
    return suma, resta, multiplicacion, division


def calculo_precio_con_iva(precio):
    """Calcula el precio con IVA incluido

    Args:
        precio (float): el precio sin IVA

    Returns:
        float: el precio con IVA incluido
    """
    return precio * (1 + IVA)





basica()
con_parametros("Fran")
con_dos_parametros("Ana", 25)
con_dos_parametros(25, "Ana")  # Esto no es correcto, pero Python no lo detecta como error
parametros_variables("Fran", 30, "Madrid", "Programador")
parametros_variables()  # Sin parámetros, también es válido
puestos_trabajo("Programador", "Diseñador", "Analista")
puestos_trabajo()  # Sin parámetros, también es válido
saludo()  # Sin parámetros, también es válido
saludo("Carlos")  # Con parámetro, también es válido
saludo2()  # Sin parámetros, también es válido
saludo2("Carlos", "Gracias por venir")  # Con parámetros, también es válido
saludo2("Carlos")  # Con un parámetro, el otro usará el valor por defecto
saludo3(nombre="Carlos", mensaje="Gracias por venir")  # Uso de parámetros nominales
saludo3(mensaje="Gracias por venir", nombre="Carlos")  # El orden no importa cuando se usan parámetros nominales
resultado_suma = suma(5, 3)
print("La suma de 5 y 3 es:", resultado_suma)
resultados_operaciones = operaciones(10, 5)
print("Resultados de las operaciones:")
print("Suma:", resultados_operaciones[0])
print("Resta:", resultados_operaciones[1])
print("Multiplicación:", resultados_operaciones[2])
print("División:", resultados_operaciones[3])
rsuma, resta, multiplicacion, division = operaciones(10, 5)
print("Resultados de las operaciones:")
print("Suma:", rsuma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
resultados_operaciones2 = operaciones2(10, 5)
print("Resultados de las operaciones con anotaciones de tipo:")
print("Suma:", resultados_operaciones2[0])
print("Resta:", resultados_operaciones2[1])
print("Multiplicación:", resultados_operaciones2[2])
print("División:", resultados_operaciones2[3])
print("Precio con IVA incluido:", calculo_precio_con_iva(100))