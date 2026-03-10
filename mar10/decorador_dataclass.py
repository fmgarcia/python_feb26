from dataclasses import dataclass

# El uso del decorador @dataclass en Python simplifica la creación de clases que se utilizan principalmente para almacenar datos. 
# Al aplicar este decorador, se generan automáticamente métodos especiales como __init__, __repr__, __eq__, 
# entre otros, lo que facilita la definición de clases sin tener que escribir código repetitivo.
# Ejemplos títpicos de uso de @dataclass incluyen la creación de clases para representar entidades como productos,
# personas, o cualquier tipo de datos estructurados.
# También para guardar configuraciones, 
# Resultados de una base de datos: Mapear filas de una base de datos a objetos de Python.
# DTO (Data Transfer Object): Para transferir datos entre diferentes partes de una aplicación o entre aplicaciones.
@dataclass
class Producto:
    nombre: str
    precio: float
    
    
# Ejemplo de uso
producto1 = Producto("Laptop", 999.99)
producto2 = Producto("Smartphone", 499.99)
nombre = "Ordenador"
print(producto1)  # Salida: Producto(nombre='Laptop', precio=999.99)
print(producto2)  # Salida: Producto(nombre='Smartphone', precio=499.99)
if producto1 == producto2:
    print("Los productos son iguales.")
else:
    print("Los productos no son iguales")
    
# La librería attrs es una alternativa a dataclasses que ofrece más funcionalidades y flexibilidad. Aquí hay un ejemplo de cómo usar attrs para definir una clase similar a Producto:
# pydantic es otra alternativa a dataclasses que se centra en la validación de datos y la gestión de modelos de datos. Aquí hay un ejemplo de cómo usar pydantic para definir una clase similar a Producto:
