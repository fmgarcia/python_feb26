import math

def area_circulo(radio):
    return math.pi * radio ** 2


if __name__ == "__main__":
    radio = 5
    area = area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {area}")
    print(f"El seno de 0 es: {math.sin(0)}")