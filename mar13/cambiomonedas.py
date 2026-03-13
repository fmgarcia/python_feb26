def devolucion_minima_monedas(lista_monedas : list[int], cantidad_devolver : int) -> list[int]:
    """
    Devuelve el mínimo número de monedas necesarias para devolver una cantidad específica, dado un conjunto de monedas disponibles. La función ordena la lista de monedas de mayor a menor y luego itera por ella, restando el valor de cada moneda a la cantidad restante por devolver hasta que se alcance la cantidad solicitada o se agoten las monedas disponibles. Si no es posible devolver exactamente la cantidad solicitada con las monedas disponibles, se lanza una excepción.
    Es un ejemplo de Algorítmo voraz, ya que en cada paso se toma la decisión que parece ser la mejor en ese momento (tomar la moneda más grande disponible) con la esperanza de que esta decisión conduzca a una solución óptima para el problema.
    Args:
        lista_monedas (list[int]): Conjunto de monedas disponibles para devolver la cantidad solicitada.
        cantidad_devolver (int): Cantidad que se desea devolver.

    Raises:
        ValueError: Si no es posible devolver exactamente la cantidad solicitada con las monedas disponibles.

    Returns:
        list[int]: Lista de monedas necesarias para devolver la cantidad solicitada.
    """    
    # Ordenamos la lista de monedas de mayor a menor para intentar devolver la cantidad con el menor número de monedas posible.
    lista_monedas.sort(reverse=True)
    
    # Inicializamos una lista vacía para almacenar las monedas que se devolverán y una variable para llevar un seguimiento de la cantidad restante por devolver.
    monedas_devolver = []
    i = 0
    while cantidad_devolver > 0 and i < len(lista_monedas):
        moneda = lista_monedas[i] # Tomamos la moneda más grande disponible.
        
        if moneda <= cantidad_devolver:
            monedas_devolver.append(moneda) # Si la moneda es menor o igual a la cantidad restante, la añadimos a la lista de monedas a devolver.
            cantidad_devolver -= moneda # Restamos el valor de la moneda a la cantidad restante por devolver.
        else:
            i += 1 # Si la moneda es mayor que la cantidad restante, la descartamos y pasamos a la siguiente moneda más grande.

    # Si después de iterar por todas las monedas, la cantidad restante es mayor que cero, significa que no se puede devolver exactamente la cantidad solicitada con las monedas disponibles, por lo que lanzamos una excepción.
    if cantidad_devolver > 0:
        raise ValueError("No se puede devolver exactamente la cantidad solicitada con las monedas disponibles.")
    
    return monedas_devolver

if __name__ == "__main__":
    lista_monedas = [10, 50, 100, 500]
    cantidad_devolver = 870
    try:
        resultado = devolucion_minima_monedas(lista_monedas, cantidad_devolver)
        print(f"Monedas a devolver para la cantidad {cantidad_devolver}: {resultado} son {len(resultado)} monedas.")
    except ValueError as e:
        print(e)