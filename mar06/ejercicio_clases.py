class Student:

    def __init__(self, name, ID, notaIngles, notaMatematica, notaCiencias):
        self.__name = name
        self.__ID = ID
        self.__notaIngles = notaIngles
        self.__notaMatematica = notaMatematica
        self.__notaCiencias = notaCiencias

    def getName(self):
        return self.__name[:2] + "..."

    def getID(self):
        return self.__ID

    def setName(self, name):
        self.__name = name

    def setID(self, ID):
        self.__ID = ID

    @property
    def notaIngles(self):
        if self.__notaIngles < 0:
            self.__notaIngles = 0
        return self.__notaIngles

    @property
    def notaMatematica(self):
        if self.__notaMatematica < 0:
            self.__notaMatematica = 0
        return self.__notaMatematica

    @property
    def notaCiencias(self):
        if self.__notaCiencias < 0:
            self.__notaCiencias = 0
        return self.__notaCiencias
    
    @notaIngles.setter
    def notaIngles(self, nota):
        if nota < 0:
            self.__notaIngles = abs(nota)
        else:
            self.__notaIngles = nota

    @notaMatematica.setter
    def notaMatematica(self, nota):
        if nota < 0:
            self.__notaMatematica = abs(nota)
        else:
            self.__notaMatematica = nota

    @notaCiencias.setter
    def notaCiencias(self, nota):
        if nota < 0:
            self.__notaCiencias = 0
        else:
            self.__notaCiencias = abs(nota)
            
    def obtenerNombreCompleto(self):
        return self.__name

    def __str__(self):
        cadena = f"Nombre: {self.getName()}, ID: {self.__ID}\n"
        cadena += f"Nota Inglés: {self.notaIngles}\n"
        cadena += f"Nota Matemáticas: {self.notaMatematica}\n"
        cadena += f"Nota Ciencias: {self.notaCiencias}\n"
        cadena += f"Total: {self.notaIngles + self.notaMatematica + self.notaCiencias:.2f} "
        cadena += f"Nota Media: {(self.notaIngles + self.notaMatematica + self.notaCiencias) / 3:.2f}"
        return cadena
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Student):
            return self.__ID == other.__ID
        return NotImplemented
    
if __name__ == "__main__":
    estudiante = Student("Fran", "123", 5.50, 7.80, 9.40)
    estudiante.__name = "Francisco"  # Esto no cambiará el nombre del estudiante, ya que el atributo name es privado y no se puede acceder directamente desde fuera de la clase. Para cambiar el nombre del estudiante, se debería utilizar el método setter setName() proporcionado en la clase Student, lo que garantiza que se mantenga la encapsulación y se controle el acceso a los atributos privados de la clase.
    estudiante.setName("Francisco")  # Esto cambiará el nombre del estudiante a "Francisco" utilizando el método setter setName() proporcionado en la clase Student, lo que garantiza que se mantenga la encapsulación y se controle el acceso a los atributos privados de la clase.
    estudiante.notaMatematica = -8.50  # Esto cambiará la nota de matemáticas del estudiante a 8.50, ya que el atributo notaMatematica es público y se puede acceder directamente desde fuera de la clase. Sin embargo, es importante tener en cuenta que modificar los atributos públicos directamente desde fuera de la clase puede no ser la mejor práctica, ya que puede romper el encapsulamiento y hacer que sea más difícil controlar los cambios en los datos del estudiante. En este caso, sería recomendable implementar un método setter específico para modificar la nota de matemáticas de manera controlada, lo que permitiría validar el valor antes de asignarlo al atributo y garantizar que se mantenga la integridad de los datos del estudiante.
    estudiante2 = Student("Francisco", "123", 4.50, 9.80, 9.40)
    print(estudiante)
    print(estudiante.obtenerNombreCompleto())
    if estudiante == estudiante2: 
        print("Los estudiantes son iguales.")
    else:
        print("Los estudiantes son diferentes.")