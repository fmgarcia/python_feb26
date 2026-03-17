fran = 49

def saludar_fran():
    print(f"Hola, soy Fran y tengo {fran} años.")
    
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

