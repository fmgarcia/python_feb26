class Circulo:
    def __init__(self, radio): # __ doble underscore (dunder) 
        self.__radio = radio # El atributo __radio es privado, lo que significa que no se puede acceder directamente desde fuera de la clase. Esto se logra mediante la convención de nombres en Python, donde los atributos que comienzan con dos guiones bajos (__) son tratados como privados y no son accesibles desde fuera de la clase. En este caso, el radio del círculo se almacena en el atributo privado __radio, lo que ayuda a proteger la integridad de los datos y a controlar el acceso a esta información a través de métodos específicos dentro de la clase.
        
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, nuevo_radio):
        if nuevo_radio > 0:
            self.__radio = nuevo_radio
        else:
            print("El radio debe ser un valor positivo.")

    def area(self):
        return 3.14 * self.__radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.__radio

if __name__ == "__main__":
    circulo = Circulo(5)  # Crea una instancia de la clase Circulo con un radio de 5
    print(f"Área del círculo: {circulo.area()}")  # Imprime el área del círculo utilizando el método area()
    print(f"Perímetro del círculo: {circulo.perimetro()}")  # Imprime el perímetro del círculo utilizando el método perimetro()
    # Intento de acceder al atributo privado __radio directamente desde fuera de la clase, lo cual no es posible debido a la convención de nombres en Python que hace que el atributo sea inaccesible desde fuera de la clase. Se muestra aquí solo para ilustrar la diferencia entre un atributo privado y un atributo público.
    print(f"Radio del círculo: {circulo.get_radio()}")  # Esto generará un error de atributo, ya que __radio es un atributo privado y no se puede acceder directamente desde fuera de la clase. Para acceder al valor del radio, se podría implementar un método getter dentro de la clase Circulo que devuelva el valor de __radio de manera controlada.
    circulo.set_radio(10)  # Intenta establecer un nuevo valor para el radio utilizando un método setter, lo cual es una práctica común para controlar el acceso a los atributos privados y garantizar que se mantengan las invariantes de la clase.
    print(f"Nuevo radio del círculo: {circulo.get_radio()}")  # Imprime el nuevo valor del radio del círculo utilizando el método getter después de haberlo modificado con el método setter.