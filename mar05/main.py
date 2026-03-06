from cuenta_bancaria import CuentaBancaria  # Importa la clase CuentaBancaria desde el módulo cuenta_bancaria.py para poder utilizarla en este archivo principal (main.py)



if __name__ == "__main__":
    cuenta = CuentaBancaria("Fran García", 2000)  # Crea una instancia de la clase CuentaBancaria con el titular "Fran García" y un saldo inicial de 2000
    print(cuenta)  # Imprime la representación legible de la cuenta bancaria utilizando el método __str__
    cuenta.depositar(500)  # Llama al método depositar para agregar 500 al saldo de la cuenta
    cuenta.retirar(200)    # Llama al método retirar para restar 200 del saldo de la cuenta
    cuenta.mostrar_saldo() # Llama al método mostrar_saldo para imprimir el saldo actual de la cuenta
    print(f"Saldo final de la cuenta: {cuenta.saldo}")  # Imprime el saldo final de la cuenta utilizando f-string para insertar la variable directamente en la cadena de texto  
    print(f"Titular de la cuenta: {cuenta.titular}")  # Imprime el titular de la cuenta utilizando f-string para insertar la variable directamente en la cadena de texto
    cuenta.saldo = -1000 # Intenta establecer un saldo negativo utilizando el setter definido en la clase CuentaBancaria, lo cual activará la validación que establece el saldo a 0 y mostrará un mensaje de advertencia
    print(cuenta) # Imprime la representación legible (método __str__) de la cuenta bancaria nuevamente para mostrar el efecto de intentar establecer un saldo negativo, que resultará en un saldo de 0 debido a la validación en el setter.
    cuenta.titular = "María López" # Modifica el titular de la cuenta utilizando el setter definido en la clase CuentaBancaria, que asigna el nuevo valor a la variable de instancia _titular
    print(cuenta)
    print(cuenta.titular) # Imprime el titular de la cuenta utilizando el getter definido en la clase CuentaBancaria, que devuelve solo los primeros 3 caracteres del nombre seguido de "..." para proteger la privacidad del titular.
    print(cuenta._titular) # Imprime el valor completo del titular de la cuenta accediendo directamente a la variable de instancia _titular, lo cual no es recomendable ya que rompe el encapsulamiento y puede exponer información sensible. Se muestra aquí solo para ilustrar la diferencia entre el getter y el acceso directo a la variable de instancia.
    print(cuenta) # Imprime la representación legible de la cuenta bancaria utilizando el método __str__, que muestra el titular (protegido por el getter) y el saldo actual de la cuenta.
    cuenta2 = CuentaBancaria("Fran García", 3000)
    cuenta._titular = "Fran García" # Modifica el titular de la cuenta2 directamente accediendo a la variable de instancia _titular, lo cual no es recomendable ya que rompe el encapsulamiento y puede exponer información sensible. Se muestra aquí solo para ilustrar la diferencia entre el getter y el acceso directo a la variable de instancia.
    if cuenta == cuenta2: # Compara dos instancias de la clase CuentaBancaria utilizando el operador de igualdad (==), lo cual por defecto compara las referencias de los objetos y no sus contenidos, por lo que esta comparación devolverá False a menos que se haya implementado un método __eq__ en la clase para comparar los atributos relevantes de las cuentas.
        print("Las cuentas son iguales.")
    else:
        print("Las cuentas son diferentes.")
      
    # Ejemplo de uso del método __add__ para sumar dos cuentas bancarias, lo cual requiere que se haya implementado un método __add__ en la clase CuentaBancaria para definir cómo se combinan los atributos de las dos cuentas al realizar la suma.
    # Es un método mágico que permite usar el operador + para crear una nueva cuenta bancaria que combine el titular y el saldo de las dos cuentas originales.  
    cuenta3 = cuenta + cuenta2
    print(cuenta3) # Imprime la representación legible de la nueva cuenta bancaria creada al sumar cuenta y cuenta2 utilizando el operador +, lo cual requiere que se haya implementado un método __add__ en la clase CuentaBancaria para definir cómo se combinan los atributos de las dos cuentas al realizar la suma.
    print(cuenta3._titular) # Imprime el titular completo de la nueva cuenta bancaria creada al sumar cuenta y cuenta2 accediendo directamente a la variable de instancia _titular, lo cual no es recomendable ya que rompe el encapsulamiento y puede exponer información sensible. Se muestra aquí solo para ilustrar la diferencia entre el getter y el acceso directo a la variable de instancia.
    print(len(cuenta3))