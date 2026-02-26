import os

def mostrar_menu():
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")
    

if __name__ == "__main__":
    inventario = {}
    if os.path.exists("inventario.txt"): # Si el archivo existe, lo leemos y cargamos el inventario
        with open("inventario.txt", "r") as f:
            for linea in f:
                producto, cantidad = linea.strip().split(": ")
                inventario[producto] = int(cantidad)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                inventario[producto] = cantidad
            case "2":
                producto = input("Ingrese el nombre del producto a eliminar: ")
                if producto in inventario:
                    del inventario[producto]
                else:
                    print("Producto no encontrado.")
            case "3":
                print("Inventario:")
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")
            case "4":
                with open("inventario.txt", "w") as f: # Guardamos el inventario en el archivo antes de salir
                    for producto, cantidad in inventario.items():
                        f.write(f"{producto}: {cantidad}\n")
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")