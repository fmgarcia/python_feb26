class Persona:
    
    especie = "Humano" # Atributo de clase que indica la especie a la que pertenece la persona. No necesita ser asignado a través del constructor __init__ porque es un atributo compartido por todas las instancias de la clase Persona. Este atributo se puede acceder tanto a través de una instancia de la clase como directamente a través de la clase misma, lo que demuestra que es un atributo común a todas las personas y no específico de cada instancia individual.
    contador_personas = 0 # Atributo de clase que se utiliza para contar el número de instancias de la clase Persona que se han creado. Se incrementa cada vez que se crea una nueva instancia de Persona en el constructor __init__, lo que permite llevar un registro del número total de personas creadas a lo largo del programa.   
    
    def __init__(self, name, age):
        self.id = Persona.contador_personas + 1 # Atributo de instancia que almacena el identificador único de cada persona, se asigna utilizando la función id() que devuelve un valor único para cada objeto en memoria. Este atributo es específico para cada instancia de la clase Persona y se utiliza para distinguir entre diferentes personas incluso si tienen el mismo nombre y edad.
        self.name = name # Atributo de instancia que almacena el nombre de la persona, se asigna a través del constructor __init__ y es específico para cada instancia de la clase Persona
        self.age = age # Atributo de instancia que almacena la edad de la persona, se asigna a través del constructor __init__ y es específico para cada instancia de la clase Persona
        Persona.contador_personas += 1
        
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def __str__(self):
        return f"Persona(name={self.name}, age={self.age}, id={self.id})"
    
    @classmethod
    def reiniciar_contador(cls, numero_personas=0):
        cls.contador_personas = numero_personas # Método de clase que reinicia el contador de personas a 0, lo cual puede ser útil para restablecer el conteo en ciertos contextos, como durante pruebas o al iniciar un nuevo ciclo de creación de personas. Este método se define como un método de clase utilizando el decorador @classmethod, lo que permite acceder al atributo de clase contador_personas a través del parámetro cls, que hace referencia a la clase Persona en lugar de a una instancia específica. Al llamar a este método, se restablecerá el contador de personas a 0 para todas las instancias de la clase Persona.

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18 # Método estático que determina si una persona es mayor de edad o no, basado en la edad proporcionada como argumento. Este método se define como un método estático utilizando el decorador @staticmethod, lo que significa que no tiene acceso a los atributos de instancia ni a los atributos de clase, y se puede llamar directamente a través de la clase Persona sin necesidad de crear una instancia. Al proporcionar una edad como argumento, este método devolverá True si la edad es mayor o igual a 18, indicando que la persona es mayor de edad, o False en caso contrario.

if __name__ == "__main__":
    alice = Persona("Alice", 30) # Crea una instancia de la clase Persona con el nombre "Alice" y la edad 30
    print(alice.introduce()) # Imprime la introducción de la persona utilizando el método introduce, que devuelve una cadena de texto con el nombre y la edad de la persona.
    print(alice) # Imprime la representación legible de la persona utilizando el método __str__, que muestra el nombre y la edad de la persona en un formato específico.
    fran = Persona("Fran García", 25) # Crea una instancia de la clase Persona con el nombre "Fran García" y la edad 25
    print(fran.introduce()) # Imprime la introducción de la persona utilizando el método introduce, que devuelve una cadena de texto con el nombre y la edad de la persona.
    print(fran) # Imprime la representación legible de la persona utilizando el método __str__, que muestra el nombre y la edad de la persona en un formato específico.
    print(f"Fran es un {fran.especie}.") # Imprime la especie a la que pertenece Fran utilizando el atributo de clase especie, lo cual muestra que Fran es un humano. El atributo de clase se accede a través de la instancia fran, pero también podría accederse directamente a través de la clase Persona, ya que es un atributo compartido por todas las instancias de la clase.
    print(f"Cualquier persona es un {Persona.especie}.") # Imprime la especie a la que pertenece cualquier persona utilizando el atributo de clase especie directamente a través de la clase Persona, lo cual muestra que cualquier persona es un humano. Esto demuestra que el atributo de clase es compartido por todas las instancias de la clase y se puede acceder tanto a través de una instancia como directamente a través de la clase.
    print(f"Total de personas creadas: {Persona.contador_personas}") # Imprime el número total de personas creadas utilizando el atributo de clase contador_personas, lo cual muestra que se han creado 2 personas hasta ahora.
    Persona.reiniciar_contador() # Llama al método de clase reiniciar_contador para restablecer el contador de personas a 0, lo cual puede ser útil para iniciar un nuevo ciclo de creación de personas o para restablecer el conteo durante pruebas.
    print(f"Contador de personas después de reiniciar: {Persona.contador_personas}") # Imprime el contador de personas después de haberlo reiniciado utilizando el método reiniciar_contador, lo cual muestra que el contador se ha restablecido a 0. Esto demuestra que el método de clase ha tenido el efecto deseado de reiniciar el conteo de personas creadas.
    Persona.reiniciar_contador(10)
    print(f"Contador de personas después de reiniciar a 10: {Persona.contador_personas}") # Imprime el contador de personas después de haberlo reiniciado a 10 utilizando el método reiniciar_contador, lo cual muestra que el contador se ha establecido a 10. Esto demuestra que el método de clase permite establecer el contador a un valor específico, lo cual puede ser útil en ciertos contextos donde se desea iniciar el conteo desde un número diferente a 0.
    print(f"¿Fran es mayor de edad? {'Sí' if Persona.es_mayor_de_edad(fran.age) else 'No'}") # Imprime si Fran es mayor de edad o no utilizando el método estático es_mayor_de_edad, lo cual muestra que Fran es mayor de edad ya que tiene 25 años. El método estático se llama directamente a través de la clase Persona, lo que demuestra que no requiere una instancia para ser utilizado y puede ser llamado en cualquier momento para verificar si una edad específica corresponde a una persona mayor de edad o no.