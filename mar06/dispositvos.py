class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        print(f"{self.marca} {self.modelo} se ha encendido.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} se ha apagado.")

class Smartphone(Dispositivo):
    def __init__(self, sistema_operativo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sistema_operativo = sistema_operativo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Sistema Operativo: {self.sistema_operativo}")
        
if __name__ == "__main__":
    smartphone = Smartphone(marca="Samsung", modelo="Galaxy S21", sistema_operativo="Android")
    smartphone2 = Smartphone("iOS", marca="Apple", modelo="iPhone 13")
    smartphone3 = Smartphone("Android", "Google", "Pixel 6")
    smartphone4 = Smartphone("Android", "OnePlus", modelo="9 Pro")