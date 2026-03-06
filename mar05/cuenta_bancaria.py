class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):  # Constructor de la clase CuentaBancaria que inicializa el titular y el saldo inicial de la cuenta
        self.titular = titular      # Asigna el nombre del titular a la variable de instancia self.titular
        self.saldo = saldo_inicial  # Asigna el saldo inicial a la variable de instancia self.saldo, que se puede modificar posteriormente mediante los métodos de la clase

    # Métodos getters y setters para el saldo, que permiten obtener y modificar el saldo de la cuenta de manera controlada, asegurando que el saldo no sea negativo
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("El saldo no puede ser negativo. Se establece a 0.")
            self._saldo = 0
        else:
            self._saldo = valor
    
    @property
    def titular(self):
        return self._titular[:3] + "..."
    @titular.setter
    def titular(self, valor):
        self._titular = valor
        
        
    # Médodos de la clase CuentaBancaria para realizar operaciones como depositar, retirar y mostrar el saldo de la cuenta
    # Método para depositar dinero en la cuenta, que verifica que la cantidad sea positiva antes de agregarla al saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    # Método para retirar dinero de la cuenta, que verifica que la cantidad sea positiva y que haya fondos suficientes antes de restarla del saldo
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")
    # Método para mostrar el saldo actual de la cuenta, que imprime el saldo utilizando f-string para insertar la variable directamente en la cadena de texto
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
    
    # Método especial __str__ para proporcionar una representación legible de la cuenta bancaria, que muestra el titular y el saldo actual de la cuenta    
    def __str__(self) -> str:
        return f"Cuenta de {self.titular}, saldo: {self.saldo}"
    
    # Método especial __eq__ para comparar dos instancias de la clase CuentaBancaria, que devuelve True si los titulares y los saldos son iguales, y False en caso contrario
    def __eq__(self, other) -> bool:
        if isinstance(other, CuentaBancaria):
            return self.titular == other.titular and self.saldo == other.saldo
        return NotImplemented
    
    # Definimos el método especial __add__ para permitir la suma de dos cuentas bancarias, que devuelve una nueva instancia de CuentaBancaria con el titular combinado y el saldo sumado de ambas cuentas
    def __add__(self, other):
        if isinstance(other, CuentaBancaria):
            nuevo_titular = f"{self._titular} y {other._titular}"
            nuevo_saldo = self.saldo + other.saldo
            return CuentaBancaria(nuevo_titular, nuevo_saldo)
        return NotImplemented
    
    def __len__(self):
        return len(self._titular)  # Devuelve la longitud del nombre del titular de la cuenta utilizando el método __len__, lo cual permite usar la función len() para obtener esta información de manera conveniente.

class CuentaBancariaSantander(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, vive_en_santander=False):
        super().__init__(titular, saldo_inicial)  # Llama al constructor de la clase base CuentaBancaria para inicializar el titular y el saldo
        self.vive_en_santander = vive_en_santander  # Agrega un nuevo atributo vive_en_santander específico para la clase CuentaBancariaSantander, que indica si el titular vive en Santander

    def mejora_residentes_santander(self):
        if self.vive_en_santander:
            self.saldo += 100  # Si el titular vive en Santander, se mejora su saldo agregando 100 a la cuenta como un beneficio adicional para los residentes de Santander.
            print(f"¡Beneficio aplicado! Nuevo saldo: {self.saldo}")
        else:
            print("Este beneficio solo está disponible para residentes de Santander.")
    
    def __str__(self) -> str:
        return f"Cuenta Santander de {self.titular}, vive en Santander: {self.vive_en_santander}, saldo: {self.saldo}"  # Sobrescribe el método __str__ para proporcionar una representación legible específica para las cuentas bancarias de Santander, que incluye la información sobre si el titular vive en Santander además del titular y el saldo.

class CuentaBancariaSabadell(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, habla_catalan=False):
        super().__init__(titular, saldo_inicial)  # Llama al constructor de la clase base CuentaBancaria para inicializar el titular y el saldo
        self.habla_catalan = habla_catalan  # Agrega un nuevo atributo habla_catalan específico para la clase CuentaBancariaSabadell, que indica si el titular habla catalán

    def __str__(self) -> str:
        if self.habla_catalan:
            return f"Vosté té una quantitat de {self.saldo} euros a la seva compte de Sabadell, i parla català."  # Si el titular habla catalán, se proporciona una representación legible en catalán que incluye el saldo de la cuenta y la información sobre el idioma.
        else:
            return f"Cuenta Sabadell de {self.titular}, habla catalán: {self.habla_catalan}, saldo: {self.saldo}"  # Si el titular no habla catalán, se proporciona una representación legible en español que incluye el titular, la información sobre el idioma y el saldo de la cuenta. 
            
            
if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan Pérez", 1000)  # Crea una instancia de la clase CuentaBancaria con el titular "Juan Pérez" y un saldo inicial de 1000
    print(cuenta)  # Imprime la representación legible de la cuenta bancaria utilizando el método __str__
    cuenta.depositar(500)  # Llama al método depositar para agregar 500 al saldo de la cuenta
    cuenta.retirar(200)    # Llama al método retirar para restar 200 del saldo de la cuenta
    cuenta.mostrar_saldo() # Llama al método mostrar_saldo para imprimir el saldo actual de la cuenta
    santanderino1 = CuentaBancariaSantander("María López", 1500, vive_en_santander=True)  # Crea una instancia de la clase CuentaBancariaSantander con el titular "María López", un saldo inicial de 1500 y vive_en_santander establecido en True
    print(santanderino1)  # Imprime la representación legible de la cuenta
    if santanderino1.vive_en_santander:  # Verifica si el titular de la cuenta santanderino1 vive en Santander utilizando el atributo vive_en_santander, lo cual es necesario para determinar si se le puede aplicar el beneficio adicional para residentes de Santander.
        santanderino1.mejora_residentes_santander()  # Si el titular vive en Santander, llama al método mejora_residentes_santander para aplicar el beneficio y mejorar su saldo.
    print(santanderino1)  # Imprime la representación legible de la cuenta nuevamente para mostrar el efecto de aplicar el beneficio para residentes de Santander.
    santanderino1.depositar(300)  # Llama al método depositar para agregar 300 al saldo de la cuenta santanderino1
    print(santanderino1)  # Imprime la representación legible de la cuenta nuevamente para mostrar el cambio después de depositar 300.
    sabadell1 = CuentaBancariaSabadell("Carlos Martínez", 2000, habla_catalan=True)  # Crea una instancia de la clase CuentaBancariaSabadell con el titular "Carlos Martínez", un saldo inicial de 2000 y habla_catalan establecido en True
    print(sabadell1)  # Imprime la representación legible de la cuenta bancaria
    sabadell2 = CuentaBancariaSabadell("Ana Gómez", 2500, habla_catalan=False)  # Crea una instancia de la clase CuentaBancariaSabadell con el titular "Ana Gómez", un saldo inicial de 2500 y habla_catalan establecido en False
    print(sabadell2)  # Imprime la representación legible de la cuenta bancaria
    
    print("POLIMORFISMO EN ACCIÓN:")  # Imprime un mensaje para indicar que se demostrará el polimorfismo en acción, lo cual se refiere a la capacidad de diferentes clases (CuentaBancaria, CuentaBancariaSantander y CuentaBancariaSabadell) de ser tratadas de manera uniforme a través de una interfaz común (método __str__) para mostrar su información de manera legible, a pesar de que cada clase tiene su propia implementación específica del método __str__.
    lista_cuentas = [cuenta, santanderino1, sabadell1, sabadell2]  # Crea una lista que contiene todas las cuentas bancarias creadas para facilitar la iteración y el manejo de múltiples cuentas.
    for cuenta in lista_cuentas:  # Itera sobre la lista de cuentas bancarias   
        print(cuenta)  # Imprime la representación legible de cada cuenta bancaria en la lista utilizando el método __str__ definido en cada clase, lo cual muestra la información relevante de cada cuenta de manera clara y legible.