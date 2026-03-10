class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)] # type: ignore
        else:
            for i, (k, v) in enumerate(self.table[index]): # type: ignore
                if k == key:
                    self.table[index][i] = (key, value) # type: ignore
                    return
            self.table[index].append((key, value)) # pyright: ignore[reportAttributeAccessIssue]

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]: # type: ignore
                if k == key:
                    return v
        return None
    
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("manzana", 0.5)
    hash_table.insert("banana", 0.3)
    hash_table.insert("naranja", 0.8)

    print(hash_table.search("manzana"))  # Salida: 0.5
    print(hash_table.search("banana"))    # Salida: 0.3
    print(hash_table.search("naranja"))   # Salida: 0.8
    print(hash_table.search("pera"))      # Salida: None (no existe en la tabla)