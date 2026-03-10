class HashTableDNI:
    
    tabla_letra_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    def __init__(self):
        self.size = 23
        self.table = {}
        for i in range(self.size):
            self.table[i] = []
            
    def hash(self, dni): # Algoritmo de hash para calcular el índice de la tabla hash a partir del número de DNI. La complejidad de esta función es O(1) debido a que realiza una operación constante para calcular el índice.
        return dni % self.size  # Devuelve un número entre 0 y 22, que es el tamaño de la tabla hash.
    
    def insert(self, dni): # Algoritmo para insertar un número de DNI en la tabla hash. La complejidad de este algoritmo es O(1) en promedio, aunque en el peor caso puede ser O(n) si hay muchas colisiones.
        letra = self.tabla_letra_DNI[dni % 23]  # Calcula la letra correspondiente al número de DNI utilizando la tabla de letras.
        index = self.hash(dni)  # Calcula el índice de la tabla hash utilizando la función de hash.
        self.table[index].append(dni)  # Inserta el número de DNI y su letra correspondiente en la tabla hash.
    
    def search(self, dni): # Algoritmo para buscar un número de DNI en la tabla hash. La complejidad de este algoritmo es O(1) en promedio, aunque en el peor caso puede ser O(n) si hay muchas colisiones.
        index = self.hash(dni)  # Calcula el índice de la tabla hash utilizando la función de hash.
        for d in self.table[index]:  # Recorre la lista en el índice correspondiente para buscar el número de DNI.
            if d == dni:  # Si encuentra el número de DNI, devuelve su letra correspondiente.
                return self.tabla_letra_DNI[dni % 23]
        return None  # Si no encuentra el número de DNI, devuelve None.
    
    def devolver_letra(self, dni): # Algoritmo para devolver la letra correspondiente a un número de DNI. La complejidad de esta función es O(1) debido a que realiza una operación constante para calcular la letra.
        return self.tabla_letra_DNI[dni % 23]  # Devuelve la letra correspondiente al número de DNI utilizando la tabla de letras.  
    
if __name__ == "__main__":
    hash_table_dni = HashTableDNI()
    hash_table_dni.insert(12345678)
    hash_table_dni.insert(87654321)
    hash_table_dni.insert(11111111)
    hash_table_dni.insert(22222221)
    hash_table_dni.insert(33333333)
    hash_table_dni.insert(44444444)

    print(hash_table_dni.search(12345678))  # Salida: Z
    print(hash_table_dni.search(87654321))  # Salida: X
    print(hash_table_dni.search(11111111))  # Salida: H
    print(hash_table_dni.search(22222222))  # Salida: None (no existe en la tabla)
    
    print(hash_table_dni.table)  # Muestra la tabla hash completa con los números de DNI y sus letras correspondientes.

    