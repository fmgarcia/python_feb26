# Ejercicio Q1 pag 62 tema 7
# Obtener 3 múltiplos del 5 entre el 0 y el 100 aleatoriamente
import random

def ejercicio1():   
    multiplos_5 = [i for i in range(1, 101) if i % 5 == 0]
    resultado = random.sample(multiplos_5, 3)
    print("3 múltiplos de 5 entre 0 y 100:", resultado)
    
def ejercicio1b():
    for _ in range(3):
        print(random.randrange(5, 101, 5))

# Ejercicio Q2 pag 63 tema 7
# Obtener el 100-day aniversary de una fecha dada por el usuario
from datetime import datetime, timedelta

def ejercicio2():
    fecha_str = input("Introduce una fecha (YYYY-MM-DD): ")
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    aniversario = fecha + timedelta(days=100)
    print(f"El aniversario de 100 días es: {aniversario.strftime('%Y-%m-%d')}")

def tirar_dado():
    return random.randint(1, 10)


if __name__ == "__main__":
    #ejercicio1()
    #ejercicio1b()
    #ejercicio2()
    print("Resultado del dado:", tirar_dado())
    print("Segundo dado:", tirar_dado())
    