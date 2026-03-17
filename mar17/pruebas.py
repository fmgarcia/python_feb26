import modulo_importar
import os

if __name__ == "__main__":
    print(modulo_importar.fran)
    modulo_importar.saludar_fran()
    persona = modulo_importar.Persona("Ana", 30)
    persona.presentarse()
    print(os.listdir())