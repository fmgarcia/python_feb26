class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre # atributo público, se puede acceder directamente desde fuera de la clase
        self._precio = precio # atributo protegido, se puede acceder desde fuera de la clase pero se recomienda no hacerlo directamente, ya que el guion bajo (_) es una convención en Python que indica que el atributo es para uso interno de la clase y no debe ser accedido directamente desde fuera de la clase. Sin embargo, esto no impide que se pueda acceder a este atributo desde fuera de la clase, por lo que es importante seguir esta convención para mantener la integridad de los datos y evitar posibles problemas al modificar el precio directamente sin pasar por métodos específicos que puedan validar o controlar los cambios en el precio.
        self.__cantidad = cantidad # atributo privado, no se puede acceder directamente desde fuera de la clase, ya que los atributos que comienzan con dos guiones bajos (__) son tratados como privados en Python y no son accesibles desde fuera de la clase. Esto ayuda a proteger la integridad de los datos y a controlar el acceso a esta información a través de métodos específicos dentro de la clase, como getters y setters, que permiten obtener y modificar el valor de la cantidad de manera controlada.

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")
            
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("La cantidad no puede ser negativa.")

    def __str__(self):
        return f"{self.nombre}: ${self._precio:.2f} y cantidad: {self.__cantidad}"
    
if __name__ == "__main__":
    producto = Producto("Laptop", 999.99, 10) # Crea una instancia de la clase Producto con el nombre "Laptop", un precio de 999.99 y una cantidad de 10
    print(producto) # Imprime la representación legible del producto utilizando el método __str__, que muestra el nombre, el precio formateado a dos decimales y la cantidad del producto.
    producto.nombre = "Smartphone" # Modifica el nombre del producto directamente accediendo al atributo público nombre, lo cual es posible pero no se recomienda si se desea mantener la integridad de los datos y controlar los cambios a través de métodos específicos.
    print(producto) # Imprime la representación legible del producto nuevamente para mostrar el cambio
    producto._precio = 899.99 # Modifica el precio del producto utilizando el método setter, lo cual es la forma recomendada de controlar los cambios en el precio.
    print(producto) # Imprime la representación legible del producto nuevamente para mostrar el cambio
    producto.precio = -100 # Intenta establecer un precio negativo utilizando el método setter, lo cual activará la validación que evita que el precio sea negativo y mostrará un mensaje de advertencia.
    print(producto) # Imprime la representación legible del producto nuevamente para mostrar el efecto
    producto.__cantidad = 20 # Intenta modificar la cantidad del producto directamente accediendo al atributo privado __cantidad, lo cual no es posible debido a la convención de nombres en Python que hace que el atributo sea inaccesible desde fuera de la clase. Para modificar la cantidad, se podría implementar un método setter dentro de la clase Producto que permita cambiar el valor de __cantidad de manera controlada.
    print(producto) # Imprime la representación legible del producto nuevamente para mostrar que la cantidad no ha cambiado debido a que el intento de modificar el atributo privado __cantidad directamente desde fuera de la clase no es posible. Para modificar la cantidad, se debería utilizar un método setter que permita cambiar el valor de __cantidad de manera controlada y que incluya validaciones para garantizar que la cantidad sea un valor válido (por ejemplo, no negativo).
    producto.cantidad = 20 # Modifica la cantidad del producto utilizando el método setter, lo cual es la forma recomendada de controlar los cambios en la cantidad.
    print(producto) # Imprime la representación legible del producto nuevamente para mostrar el cambio
    