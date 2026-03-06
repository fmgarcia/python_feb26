class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Empleado:
    def __init__(self, salario):
        self.salario = salario

    def mostrar_salario(self):
        return f"Mi salario es {self.salario} dólares."
    
    def presentarse(self):
        return f"Soy un empleado con un salario de {self.salario} dólares."
    
class Trabajador(Persona, Empleado):
    def __init__(self, nombre, edad, salario):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, salario)
        
    def presentarse(self):
        return f"{Persona.presentarse(self)} {Empleado.presentarse(self)}"  # Llama a los métodos presentarse de ambas clases base (Persona y Empleado) para proporcionar una presentación completa del trabajador, que incluye tanto su información personal como su información laboral. Esto demuestra cómo la herencia múltiple permite combinar funcionalidades de múltiples clases base en una clase derivada, y cómo se pueden llamar explícitamente a los métodos de cada clase base para resolver cualquier conflicto que pueda surgir debido a la presencia de métodos con el mismo nombre en ambas clases base.

if __name__ == "__main__":
    trabajador = Trabajador("Carlos", 30, 50000)
    print(trabajador.presentarse())  # Llama al método presentarse, que se resuelve utilizando el método de la clase Persona debido al orden de herencia (Persona primero, luego Empleado). Esto demuestra cómo la herencia múltiple permite que una clase derive de múltiples clases base y cómo se resuelven los métodos en caso de conflicto. En este caso, el método presentarse de la clase Persona se utiliza en lugar del método presentarse de la clase Empleado debido al orden en que se definen las clases en la declaración de la clase Trabajador.
    print(trabajador.mostrar_salario())  # Llama al método mostrar_salario, que se resuelve utilizando el método de la clase Empleado, lo cual demuestra que el trabajador tiene acceso a los métodos de ambas clases base (Persona y Empleado) gracias a la herencia múltiple.