def nreinas_backtracking(n):
    def es_valida(tablero, fila, columna):
        # Verificar la columna
        for i in range(fila):
            if tablero[i] == columna or \
               tablero[i] - i == columna - fila or \
               tablero[i] + i == columna + fila:
                return False
        return True
    def resolver_nreinas(tablero, fila):
        if fila == n:
            resultado.append(tablero[:])
            return
        for columna in range(n):
            if es_valida(tablero, fila, columna):
                tablero[fila] = columna
                resolver_nreinas(tablero, fila + 1)
    resultado = []
    tablero = [-1] * n
    resolver_nreinas(tablero, 0)
    return resultado

if __name__ == "__main__":
    n = 8
    soluciones = nreinas_backtracking(n)
    print(f"Soluciones para {n} reinas:")
    for solucion in soluciones:
        print(solucion)