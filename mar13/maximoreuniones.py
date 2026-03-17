lista_inicio = [1, 3, 2, 0, 5, 8, 5]
lista_final = [2, 4, 5, 6, 6, 9, 9]

def seleccion_reuniones(lista_inicio, lista_final):
    reuniones = list(zip(lista_inicio, lista_final))
    lista_resultado = []
    contador = 0
    ultima_finalizacion = 0
    while reuniones:
        inicio, fin = reuniones.pop(0)
        if inicio >= ultima_finalizacion:
            lista_resultado.append((inicio, fin))
            contador += 1
            ultima_finalizacion = fin
    return lista_resultado

if __name__ == "__main__":
    lista_resultado = seleccion_reuniones(lista_inicio, lista_final)
    print("El número de reuniones sin solapamiento es:", len(lista_resultado))
    print("Las reuniones seleccionadas son:", lista_resultado)