from cola import Queue
from dataclasses import dataclass

@dataclass
class Persona:
    def __init__(self, nombre, edad, llegada):
        self.nombre = nombre
        self.edad = edad
        self.llegada = llegada

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return self.__str__()
    

class ColaRestaurante (Queue):
    def __init__(self):
        super().__init__() 
        
    def obtener_precio(self, persona):
        if isinstance(persona, Persona):
            if persona.llegada < "12:00":
                return 8.0  # Precio reducido para personas que llegan antes de las 12:00, lo que incentiva a los clientes a llegar temprano al restaurante y permite ofrecer descuentos especiales para atraer a más clientes durante las horas menos concurridas del día.
        return 10.0  # Precio fijo para cada persona en el restaurante, lo que permite calcular el costo total de la cola de personas en función del número de personas presentes en la cola.  

    
if __name__ == "__main__":
    persona1 = Persona("Carlos", 30, "10:00")
    persona2 = Persona("Ana", 25, "12:05")
    persona3 = Persona("Luis", 40, "12:10")

    cola_personas = ColaRestaurante()
    cola_personas.enqueue(persona1)
    cola_personas.enqueue(persona2)
    cola_personas.enqueue(persona3)

    print(cola_personas)  # Muestra la cola con las personas en el orden en que fueron agregadas

    print(f"Precio para {cola_personas.peek().nombre}: ${cola_personas.obtener_precio(cola_personas.peek())}")  # type: ignore # Muestra el precio para la primera persona en la cola (persona1), que es 8.0 debido a su hora de llegada antes de las 12:00.
    print(cola_personas.dequeue())  # Elimina y muestra la primera persona en la cola (persona1)
    print(cola_personas)  # Muestra la cola después de eliminar la primera persona

    print(f"Precio para {cola_personas.peek().nombre}: ${cola_personas.obtener_precio(cola_personas.peek())}")  # type: ignore # Muestra el precio para la siguiente persona en la cola (persona2), que es 10.0 debido a su hora de llegada después de las 12:00.
    print(cola_personas.size())  # Muestra el número de personas restantes en la cola (2)